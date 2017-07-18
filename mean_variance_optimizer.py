import scipy.optimize as spo
import numpy as np

class MeanVarianceOptimizer:

    def __init__(self, historical_security_quote_periods):
        self.historical_security_quote_periods = historical_security_quote_periods

    def volatility_minimization(self, weights):
        volatility = 0.0

        for index in range(0, len(self.historical_security_quote_periods)):
            volatility += self.historical_security_quote_periods[index].get_returns_std() * weights[index]

        return volatility

    @staticmethod
    def elements_sum_constraint(x):
        sum = np.sum(x)

        if 1.0 <= sum and sum <= 2.0:
            return 0
        else:
            return 1

    @staticmethod
    def elements_are_non_negative_constraint(x):
        for num in x:
            if num < 0.0:
                return 1
        return 0

    def minimize_function(self):
        weights = []
        for index in range(0, len(self.historical_security_quote_periods)):
            weights.append(1.0)

        constraints = [{'type' : 'eq', 'fun' : MeanVarianceOptimizer.elements_are_non_negative_constraint},
                       {'type': 'eq', 'fun': MeanVarianceOptimizer.elements_sum_constraint}]

        min_result = spo.minimize(self.volatility_minimization, weights, method = 'SLSQP', constraints = constraints)

        print min_result

