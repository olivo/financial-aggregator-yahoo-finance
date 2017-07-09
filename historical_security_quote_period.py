from functools import reduce
from numpy import mean, var
import pandas

class HistoricalSecurityQuotePeriod:
    def __init__(self, symbol, historical_security_quotes):
        self.__symbol = symbol
        self.__historical_security_quotes = historical_security_quotes

    def get_close_prices(self):
        return self.__historical_security_quotes['Adj Close']

    def get_historical_security_quotes(self):
        return self.__historical_security_quotes

    def get_cumulative_returns(self):
        adjusted_close = self.__historical_security_quotes[['Adj Close']]
        return  adjusted_close.ix[-1, 0] / adjusted_close.ix[0, 0] - 1

    def get_price_mean(self):
        return self.__historical_security_quotes['Adj Close'].mean()

    def get_returns(self):
        adjusted_close = self.__historical_security_quotes[['Adj Close']]
        returns = adjusted_close.pct_change(fill_method = 'pad')
        returns.ix[0, 0] = 0

        return returns


    def get_returns_mean(self):
        returns = self.get_returns()

        return returns.mean().ix[0]

    def get_symbol(self):
        return self.__symbol

    def get_std(self):
        returns = self.get_returns()

        return returns.std().ix[0]

    def get_sharpe_sratio(self):
        return self.get_returns_mean() / self.get_std()

    def __str__(self):

        res = ""
        res += self.get_close_prices().to_string()
        res += "\n\n"
        res += "Return - Mean - Std Dev - Sharpe Ratio \n"
        res += str(self.get_cumulative_returns()) + " " + str(self.get_returns_mean()) + " " + str(self.get_std()) \
                + " " + str(self.get_sharpe_sratio()) + ""

        return res