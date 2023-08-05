import numpy as np
import math

from .Utils import *
from .Logger import *


class StocksAllocator:

    def __init__(self, logger = Logger("PPFT")) -> None:
        self._logger = logger

    def _AllocateGreedy(self, weights, prices, total, silent):
        """Allocates the given amount of money to the given stocks using the given weights using a greedy algorithm"""

        if len(weights) != len(prices):
            raise RuntimeError("Weights and prices must be of same size")

        # allocate the money to the stocks
        allocated = [0] * len(weights)
        for i in range(len(weights)):
            allocated[i] = total * weights[i] / prices[i]

        # round the allocations to the nearest integer
        allocated = [int(math.floor(x)) for x in allocated]

        # calculate the total allocated
        totalAllocated = sum([allocated[i] * prices[i] for i in range(len(weights))])
        """
        # if the total allocated is less than the total, then allocate the remaining money to the stock with the highest weight
        if totalAllocated < total:
            remaining = total - totalAllocated
            # move from the stock with the highest weight to lowest weight
            # and check if the remaining money is enough to allocate to the stock
            # allocate the max posible stocks of that stock then move to the next stock

            weightsWithIndex = [(weights[i], i) for i in range(len(weights))]
            weightsWithIndex.sort(key=lambda x: x[0])
            weightsWithIndex.reverse()
            minPrice = min(prices)
            while remaining > minPrice:
                for weight, index in weightsWithIndex:
                    if remaining > prices[index]:
                        allocated[index] += 1
                        remaining -= prices[index]
                    else:
                        break

        totalAllocated = sum([allocated[i] * prices[i] for i in range(len(weights))])
        """

        result =  Object()
        result.allocated = allocated
        result.prices = prices
        result.totalAllocated = totalAllocated
        result.fundsLeft = total - totalAllocated
        return result

    def _AllocateRandom(self, weights, prices, total, silent):
        """Allocates the given amount of money to the given stocks using the given weights using a random algorithm"""
        # randomize the weights
        weights = [np.random.uniform(0, 1) for x in range(len(weights))]
        weights = [x / sum(weights) for x in weights]
        return self._AllocateGreedy(weights, prices, total, silent)

    def Allocate(self, weights, prices, total, method = "greedy", silent = False):
        """Allocates the given amount of money to the given stocks using the given weights"""
        if method == "greedy":
            return self._AllocateGreedy(weights, prices, total, silent)
        elif method == "random":
            return self._AllocateRandom(weights, prices, total, silent)
        else:
            raise RuntimeError(f'Unknown allocation method {method}')


