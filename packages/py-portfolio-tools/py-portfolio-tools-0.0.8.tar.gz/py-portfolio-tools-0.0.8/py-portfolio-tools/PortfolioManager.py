from .Utils import *
from .Logger import *
from .DataFetch import *
from .Portfolio import *
from .StocksAllocator import *
from .Optimizers import *
import pandas as pd
import numpy as np
import json
import os
import imgui

class PortfolioManager:

    def __init__(self, portfolio: Portfolio):
        self._portfolio = portfolio
        self._showWindow = True
        self._startDate = "2020-01-01"
        self._endDate = "2022-12-31"
        self._stockHistoryTextures = []
        self._stockHistoryComparisonTexture = None
        self._stocksBasedDistributionPlotTexture = None
        self._countryBasedDistributionPlotTexture = None
        self._sectorBasedDistributionPlotTexture = None
        self._allocator = StocksAllocator()
        self._allocatedWithStocks = None
        self._allocatorTotalBudget = 100000
        self._optimizedPortfolios = []
    
    def Show(self):
        """Show the portfolio in a imgui window"""
        if not self._showWindow:
            return
        
        windowExpanded, self._showWindow = imgui.begin(f"Portfolio {self._portfolio._name}", True)

        with imgui.begin_tab_bar("MainPortfolioTabBar") as tab_bar:
            if tab_bar.opened:
                with imgui.begin_tab_item("General") as item1:
                    if item1.selected:
                        self.ShowGeneralTab()

                with imgui.begin_tab_item("Analysis") as item2:
                    if item2.selected:
                        if not self._portfolio._hasAnalysis:
                            imgui.text("No analysis has been done yet")
                        else:
                            self.ShowAnalysisTab()

        imgui.end()
    
    def ShowGeneralTab(self):
        expanded, visible = imgui.collapsing_header("Portfolio Summary")
        if expanded:
            imgui.text(f"Name: {self._portfolio._name}")
            imgui.text(f"Stocks: ")
            for i in range(len(self._portfolio._stocks)):
                imgui.text(f"    {self._portfolio._stocks[i]}: {self._portfolio._weights[i]}")
            imgui.separator()
        
        expanded, visible = imgui.collapsing_header("Portfolio Analysis")
        if expanded:
            changed, self._startDate = imgui.input_text("Start Date", self._startDate, 10)
            changed, self._endDate = imgui.input_text("End Date", self._endDate, 10)
            if imgui.button("Analyse"):
                self._portfolio.Analyse(self._startDate, self._endDate)
                self.LoadAnalysis()
        
        expanded, visible = imgui.collapsing_header("Portfolio Allocation")
        if expanded and self._portfolio._hasAnalysis:
            if self._allocatedWithStocks == None:
                imgui.text("No allocation has been done yet")
            else:
                imgui.text("Allocated with stocks: ")
                for i in range(len(self._allocatedWithStocks.allocated)):
                    imgui.text(f"    {self._portfolio._stocks[i]} : {self._allocatedWithStocks.allocated[i]} ({self._allocatedWithStocks.prices[i]} each)")
                imgui.text(f"Funds Left: {self._allocatedWithStocks.fundsLeft}")
                imgui.text(f"Funds Used: {self._allocatedWithStocks.totalAllocated}")
            changed, self._allocatorTotalBudget = imgui.input_int("Total Budget", self._allocatorTotalBudget, 1)
            if imgui.button("Allocate Greedy"):
                prices = [self._portfolio._analysis.stockHistory[stock].iloc[-1] for stock in self._portfolio._stocks]
                self._allocatedWithStocks = self._allocator.Allocate(self._portfolio._weights, prices, self._allocatorTotalBudget, "greedy")
            imgui.same_line()
            if imgui.button("Allocate Random"):
                prices = [self._portfolio._analysis.stockHistory[stock].iloc[-1] for stock in self._portfolio._stocks]
                self._allocatedWithStocks = self._allocator.Allocate(self._portfolio._weights, prices, self._allocatorTotalBudget, "random")
        elif expanded:
            imgui.text("No analysis has been done yet")
        
        expanded, visible = imgui.collapsing_header("Portfolio Optimization")
        if expanded:
            if imgui.button("Optimize (Monte Carlo)"):
                optimizer = MonteCarloOptimizer(self._portfolio, self._portfolio._logger)
                self._optimizedPortfolios = optimizer.Optimize(self._startDate, self._endDate, 10000)
            imgui.same_line()
            if imgui.button("Optimize (Mean Variance)"):
                optimizer = MeanVarianceOptimizer(self._portfolio, self._portfolio._logger)
                self._optimizedPortfolios = optimizer.Optimize(self._startDate, self._endDate)
            if len(self._optimizedPortfolios) > 0:
                imgui.text("Optimized Portfolios:")
                with imgui.begin_child("##OptimizedPortfolios", 0, 300):
                    for i in range(len(self._optimizedPortfolios)):
                        imgui.text(f"Expected Return: {(self._optimizedPortfolios[i][1] * 100):.2f}%")
                        imgui.text(f"Risk: {(self._optimizedPortfolios[i][0] * 100):.2f}%")
                        imgui.text(f"Sharpe Ratio: {self._optimizedPortfolios[i][2]:.2f}")
                        imgui.text(f"Weights: " + str(self._optimizedPortfolios[i][3]))
                        if imgui.button("Load & Analyse##OptimizedPortfolio_" + str(i)):
                            self._portfolio._weights = self._optimizedPortfolios[i][3]
                            self._portfolio.Analyse(self._startDate, self._endDate)
                            self.LoadAnalysis()
                        imgui.separator()
            else:
                imgui.text("No optimization has been done yet")
        
    def ShowAnalysisTab(self):
        expanded, visible = imgui.collapsing_header("Stocks History")
        if expanded:
            imgui.push_id("StocksHistoryTab")
            for i in range(len(self._portfolio._stocks)):
                imgui.text(f"{self._portfolio._stocks[i]}")
                imgui.image(self._stockHistoryTextures[i].id, self._stockHistoryTextures[i].width, self._stockHistoryTextures[i].height)
                if imgui.button(f"Save {self._portfolio._stocks[i]} as File"):
                    SaveImageAsFile(self._stockHistoryTextures[i], ShowFileSaveWindow() + ".png")
                imgui.separator()
            
            imgui.text("Comparison")
            imgui.image(self._stockHistoryComparisonTexture.id, self._stockHistoryComparisonTexture.width, self._stockHistoryComparisonTexture.height)
            if imgui.button("Save Comparison as File"):
                SaveImageAsFile(self._stockHistoryComparisonTexture, ShowFileSaveWindow() + ".png")
            imgui.separator()
            imgui.pop_id()
        
        expanded, visible = imgui.collapsing_header("Portfolio Diversification")
        if expanded:
            imgui.text("Stocks Based Distribution")
            imgui.image(self._stocksBasedDistributionPlotTexture.id, self._stocksBasedDistributionPlotTexture.width, self._stocksBasedDistributionPlotTexture.height)
            if imgui.button("Save Stocks Based Distribution as File"):
                SaveImageAsFile(self._stocksBasedDistributionPlotTexture, ShowFileSaveWindow() + ".png")
            
            imgui.text("Country Based Distribution")
            imgui.image(self._countryBasedDistributionPlotTexture.id, self._countryBasedDistributionPlotTexture.width, self._countryBasedDistributionPlotTexture.height)
            if imgui.button("Save Country Based Distribution as File"):
                SaveImageAsFile(self._countryBasedDistributionPlotTexture, ShowFileSaveWindow() + ".png")
            
            imgui.text("Sector Based Distribution")
            imgui.image(self._sectorBasedDistributionPlotTexture.id, self._sectorBasedDistributionPlotTexture.width, self._sectorBasedDistributionPlotTexture.height)
            if imgui.button("Save Sector Based Distribution as File"):
                SaveImageAsFile(self._sectorBasedDistributionPlotTexture, ShowFileSaveWindow() + ".png")

        expanded, visible = imgui.collapsing_header("Numerical Analysis")
        if expanded:
            imgui.text("Variance: " + str(self._portfolio._analysis.portfolioVariance * 100) + "%")
            imgui.text("Risk: " + str(self._portfolio._analysis.portfolioRisk * 100) + "%")
            imgui.text("Return: " + str(self._portfolio._analysis.portfolioExpectedReturn * 100) + "%")
            imgui.text("Sharpe Ratio: " + str(self._portfolio._analysis.portfolioSharpeRatio))

    def UnloadAnalysis(self):
        for texture in self._stockHistoryTextures:
            DeleteGLTexture(texture.id)

        if self._stockHistoryComparisonTexture != None:
            DeleteGLTexture(self._stockHistoryComparisonTexture.id)
    
        if self._stocksBasedDistributionPlotTexture != None:
            DeleteGLTexture(self._stocksBasedDistributionPlotTexture.id)

        if self._countryBasedDistributionPlotTexture != None:
            DeleteGLTexture(self._countryBasedDistributionPlotTexture.id)
        
        if self._sectorBasedDistributionPlotTexture != None:
            DeleteGLTexture(self._sectorBasedDistributionPlotTexture.id)

    def LoadAnalysis(self):
        self.UnloadAnalysis()
        self._stockHistoryTextures = [ CreateGLTexture(self._portfolio._analysis.stockHistoryPlots[i]) for i in range(len(self._portfolio._stocks)) ]
        self._stockHistoryComparisonTexture = CreateGLTexture(self._portfolio._analysis.stockHistoryComparisonPlot)
        self._stocksBasedDistributionPlotTexture = CreateGLTexture(self._portfolio._analysis.stocksBasedDistributionPlot)
        self._countryBasedDistributionPlotTexture = CreateGLTexture(self._portfolio._analysis.countryBasedDistributionPlot)
        self._sectorBasedDistributionPlotTexture = CreateGLTexture(self._portfolio._analysis.sectorBasedDistributionPlot)