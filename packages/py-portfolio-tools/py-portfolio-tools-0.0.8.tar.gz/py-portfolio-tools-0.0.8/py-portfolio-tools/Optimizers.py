from .Utils import *
from .Logger import *
from .Portfolio import *
from scipy.optimize import minimize

import copy
import random

class Optimizer:
    def __init__(self, portfolio, logger = Logger("PPFT")) -> None:
        self._portfolio = copy.deepcopy(portfolio)
        self._logger = logger
    
class MonteCarloOptimizer(Optimizer):
    def __init__(self, portfolio, logger = Logger("PPFT")) -> None:
        super().__init__(portfolio, logger)
    
    def Optimize(self, startDate, endDate, iterations, silent = False):
        """Generate a set of portfolios with random weights and return the best one"""
        self._minRisk = (10e10, -10e10, -10e10, None)
        self._maxReturn = (10e10, -10e10, -10e10, None)
        self._maxSharpe = (10e10, -10e10, -10e10, None)
        weightsCopy = []
        self._portfolio.NumericalAnalysis(startDate, endDate, True)
        if not silent:
            self._logger.Log(f'Running Monte Carlo Optimizer with {iterations} iterations')
        for i in range(iterations):
            # step 1 randomize the weights
            weightsCopy = [random.random() for _ in range(len(self._portfolio._weights))]
            # normalize the weights
            weightsCopySum = sum(weightsCopy)
            weightsCopy = [x / weightsCopySum for x in weightsCopy]
            # step 2 calculate the portfolio
            self._portfolio.SetWeights(weightsCopy)
            self._portfolio.CalculateRisk()
            self._portfolio.CalculateExpectedReturn()
            self._portfolio.CalculateSharpeRatio()
            # step 3 calculate the risk, return and sharpe ratio
            if self._portfolio._analysis.portfolioRisk < self._minRisk[0]:
                self._minRisk = (self._portfolio._analysis.portfolioRisk, self._portfolio._analysis.portfolioExpectedReturn, self._portfolio._analysis.portfolioSharpeRatio, weightsCopy)
            if self._portfolio._analysis.portfolioExpectedReturn > self._maxReturn[1]:
                self._maxReturn = (self._portfolio._analysis.portfolioRisk, self._portfolio._analysis.portfolioExpectedReturn, self._portfolio._analysis.portfolioSharpeRatio, weightsCopy)
            if self._portfolio._analysis.portfolioSharpeRatio > self._maxSharpe[2]:
                self._maxSharpe = (self._portfolio._analysis.portfolioRisk, self._portfolio._analysis.portfolioExpectedReturn, self._portfolio._analysis.portfolioSharpeRatio, weightsCopy)
        return [self._minRisk, self._maxReturn, self._maxSharpe]


class MeanVarianceOptimizer(Optimizer):
    def __init__(self, portfolio, logger = Logger("PPFT")) -> None:
        super().__init__(portfolio, logger)
    
    def _NegetiveSharpeRatio(self, weights):
        """Returns the negetive sharpe ratio of the portfolio"""
        self._portfolio.SetWeights(weights)
        self._portfolio.CalculateRisk()
        self._portfolio.CalculateExpectedReturn()
        return -self._portfolio.CalculateSharpeRatio()

    def Optimize(self, startDate, endDate, silent = False):
        """Optimize the portfolio using the mean variance optimizer"""
        self._portfolio.NumericalAnalysis(startDate, endDate, True)
        numAssets = len(self._portfolio._stocks)
        initialWeights = [1 / numAssets for _ in range(numAssets)]
        bounds = tuple((0, 1) for _ in range(numAssets))
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        if not silent:
            self._logger.Log(f'Running Mean Variance Optimizer with {numAssets} assets and method SLSQP to maximize Sharpe Ratio')
        optimized = minimize(self._NegetiveSharpeRatio, initialWeights, method='SLSQP', bounds=bounds, constraints=constraints)
        self._portfolio.SetWeights(optimized.x)
        self._portfolio.NumericalAnalysis(startDate, endDate, True)
        return [(self._portfolio._analysis.portfolioRisk, self._portfolio._analysis.portfolioExpectedReturn, self._portfolio._analysis.portfolioSharpeRatio, optimized.x)]


