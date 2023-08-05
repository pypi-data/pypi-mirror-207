from .Utils import *
from .Logger import *
from .DataFetch import *
import pandas as pd
import numpy as np
import json
import os
import io
import imgui
import matplotlib.pyplot as plt

class Portfolio:
    """Portfolio is a class that handles the portfolio"""

    def __init__(self, name, stocks, weights = None, predictor = None, dataFetch = DataFetch(), logger = Logger("PPFT")):
        """Initialise the portfolio with the given name, stocks, weights, predictor, dataFetch and logger"""
        self._name = name
        self._stocks = stocks
        if len(stocks) == 0:
            raise RuntimeError("Stocks size cannot be zero")
        if weights == None or len(stocks) != len(weights):
            weights = [1.0 / len(stocks)] * len(stocks)
        self._weights = weights
        self._predictor = predictor
        self._dataFetch = dataFetch
        self._logger = logger
        self._analysis = None
        self._hasAnalysis = False
        self._stockHistory = None
        self._hasStockHistory = False
        self._isCompoundingReturns = False
        self._logReturns = False
        self._riskFreeRate = 0.02
        self._forceReCalculate = False
    
    def SetWeights(self, weights):
        """Set the weights of the portfolio"""
        if len(weights) != len(self._stocks):
            raise RuntimeError("Weights size does not match stocks size")
        self._weights = weights
    
    def FetchStockHistory(self, startDate, endDate, silent = False):
        # is endDate is None, then set it to today
        if endDate == None:
            endDate = str(datetime.now().strftime("%Y-%m-%d"))
        # check if end date after today
        requirePrediction = False
        finalEndDate = endDate
        if datetime.strptime(endDate, "%Y-%m-%d") > datetime.now():
            self._logger.Log(f'End date {endDate} is after today')
            self._logger.Log(f'Using predictor to predict rest of the data')
            requirePrediction = True
            finalEndDate = str(datetime.now().strftime("%Y-%m-%d"))
        # get the stock history till today
        self._logger.Log(f'Loading stock history from {startDate} to {finalEndDate}')
        self._stockHistory = pd.DataFrame()
        for stock in self._stocks:
            self._stockHistory[stock] = self._dataFetch.GetStockHistory(stock, start = startDate, end = finalEndDate)["Close"]
        
        if requirePrediction:
            self._logger.Log(f'Predicting stock history from {finalEndDate} to {endDate}')
            if self._predictor == None:
                raise RuntimeError("Predictor is not set")
            self._stockHistory = self._predictor.Predict(self._stockHistory, finalEndDate, endDate)

        self._hasStockHistory = True

    def CalculateDailyReturns(self):
        # calculate the daily returns
        if self._analysis == None:
            raise RuntimeError("Analysis has not been done yet")
        if self._logReturns:
            self._analysis.dailyReturns = np.log(1 + self._stockHistory.pct_change()).dropna(how="all")
        else:
            self._analysis.dailyReturns = self._stockHistory.pct_change().dropna(how="all")
        return self._analysis.dailyReturns
        
    def CalculateDailyMeanReturns(self):
        # calculate the daily mean returns
        if self._analysis == None:
            raise RuntimeError("Analysis has not been done yet")
        if self._forceReCalculate:
            self.CalculateDailyReturns()
        if self._isCompoundingReturns:
            self._analysis.meanDailyReturns = (self._analysis.dailyReturns + 1).prod() ** (252 / self._analysis.dailyReturns.count) - 1
        else:
            self._analysis.meanDailyReturns = self._analysis.dailyReturns.mean() * 252
        return self._analysis.meanDailyReturns
       
    def CalculatePortfolioCovarianceMatrix(self):
        if self._analysis == None:
            raise RuntimeError("Analysis has not been done yet")
        if self._forceReCalculate:
            self.CalculateDailyReturns()
        # calculate the covariance matrix
        self._analysis.covarianceMatrix = self._analysis.dailyReturns.cov() * 252
        return self._analysis.covarianceMatrix 
    
    def CalculateRisk(self):
        # calculate the portfolio standard deviation
        if self._analysis == None:
            raise RuntimeError("Analysis has not been done yet")
        if self._forceReCalculate:
            self.CalculatePortfolioCovarianceMatrix()        
        # calculate the portfolio variance
        self._analysis.portfolioVariance = np.dot(self._weights, np.dot(self._analysis.covarianceMatrix, self._weights))
        # calculate the portfolio standard deviation
        self._analysis.portfolioStandardDeviation = np.sqrt(self._analysis.portfolioVariance)
        self._analysis.portfolioRisk = self._analysis.portfolioStandardDeviation
        return self._analysis.portfolioRisk

    def CalculateExpectedReturn(self):
        # calculate the portfolio expected return
        if self._analysis == None:
            raise RuntimeError("Analysis has not been done yet")
        self._analysis.portfolioExpectedReturn = np.dot(self._weights, self._analysis.meanDailyReturns)
        return self._analysis.portfolioExpectedReturn
    
    def CalculateSharpeRatio(self, riskFreeRate = 0.02):
        # calculate the portfolio sharpe ratio
        if self._analysis == None:
            raise RuntimeError("Analysis has not been done yet")
        if self._forceReCalculate:
            self.CalculateExpectedReturn()
            self.CalculateRisk()
        self._analysis.portfolioSharpeRatio = (self._analysis.portfolioExpectedReturn - riskFreeRate) / self._analysis.portfolioStandardDeviation
        return self._analysis.portfolioSharpeRatio
    
    def NumericalAnalysis(self, startDate, endDate, silent = False):
        """Do a numerical analysis of the portfolio"""

        if not silent:
            self._logger.Log(f"Starting numerical analysis of portfolio {self._name}")
            self._logger.Log(f"Stocks: {self._stocks}")
            self._logger.Log(f"Weights: {self._weights}")
        
        if not self._hasStockHistory:
            self.FetchStockHistory(startDate, endDate, silent)

        if self._analysis == None:
            self._analysis = Object()
            self._analysis.startDate = startDate
            self._analysis.endDate = endDate
            self._analysis.stockHistory = self._stockHistory.copy()

        self.CalculateDailyReturns() 
        self.CalculateDailyMeanReturns()
        self.CalculatePortfolioCovarianceMatrix()
        self.CalculateRisk()
        self.CalculateExpectedReturn()
        self.CalculateSharpeRatio(self._riskFreeRate)
   

    def Analyse(self, startDate, endDate):
        """Analyse the portfolio from the start date to the end date"""
        self._logger.Log(f'Calculating portfolio history from {startDate} to {endDate}')
        
        if not self._hasStockHistory:
            self.FetchStockHistory(startDate, endDate, False)
        
        if self._analysis == None:
            self._analysis = Object()
            self._analysis.startDate = startDate
            self._analysis.endDate = endDate
            self._analysis.stockHistory = self._stockHistory.copy()

        self._analysis.stockHistoryPlots = []
        
        # plot the stock history of individual stocks in individual graphs
        self._logger.Log(f'Plotting stock history of individual stocks')
        for stock in self._stocks:
            plt.plot(self._stockHistory[stock])
            plt.title(stock)
            buffer = io.BytesIO()
            plt.savefig(buffer, format = "png")
            self._analysis.stockHistoryPlots.append(buffer)
            plt.clf()

        # plot the stock history comparison chart
        self._logger.Log(f'Plotting stock history comparison chart')
        normalizedStockHistory = self._stockHistory.divide(self._stockHistory.iloc[0], axis=1)
        plt.plot(normalizedStockHistory)
        plt.title("Stock History Comparison")
        buffer = io.BytesIO()
        plt.savefig(buffer, format = "png")
        self._analysis.stockHistoryComparisonPlot = buffer
        plt.clf()
    
        # plot pie chart of portfolio weights with labels and percentages
        self._logger.Log(f'Plotting Portfolio Distribution')
        plt.pie(self._weights, labels = self._stocks, autopct='%1.1f%%')
        plt.title("Portfolio Distribution")
        buffer = io.BytesIO()
        plt.savefig(buffer, format = "png")
        self._analysis.stocksBasedDistributionPlot = buffer
        plt.clf()

        # load stock infos
        self._logger.Log(f'Loading stock infos')
        self._analysis.stockInfos = {}
        self._analysis.countryBasedDistribution = {}
        self._analysis.sectorBasedDistribution = {}
        for i in range(len(self._stocks)):
            stockInfo = self._dataFetch.GetStockInfo(self._stocks[i])
            self._analysis.stockInfos[self._stocks[i]] = stockInfo
            self._analysis.countryBasedDistribution[stockInfo["country"]] = self._analysis.countryBasedDistribution.get(stockInfo["country"], 0) + self._weights[i]
            self._analysis.sectorBasedDistribution[stockInfo["sector"]] = self._analysis.sectorBasedDistribution.get(stockInfo["sector"], 0) + self._weights[i]
        
        # plot pie chart of portfolio country based distribution with labels and percentages
        self._logger.Log(f'Plotting Country Based Distribution')
        plt.pie(self._analysis.countryBasedDistribution.values(), labels = self._analysis.countryBasedDistribution.keys(), autopct='%1.1f%%')
        plt.title("Country Based Distribution")
        buffer = io.BytesIO()
        plt.savefig(buffer, format = "png")
        self._analysis.countryBasedDistributionPlot = buffer
        plt.clf()

        # plot pie chart of portfolio sector based distribution with labels and percentages
        self._logger.Log(f'Plotting Sector Based Distribution')
        plt.pie(self._analysis.sectorBasedDistribution.values(), labels = self._analysis.sectorBasedDistribution.keys(), autopct='%1.1f%%')
        plt.title("Sector Based Distribution")
        buffer = io.BytesIO()
        plt.savefig(buffer, format = "png")
        self._analysis.sectorBasedDistributionPlot = buffer
        plt.clf()

        
        self.NumericalAnalysis(startDate, endDate, True)

        self._hasAnalysis = True
