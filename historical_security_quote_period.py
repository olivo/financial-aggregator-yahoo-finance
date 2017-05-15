from functools import reduce
from numpy import mean, var

class HistoricalSecurityQuotePeriod:
    def __init__(self, historical_security_quotes):
        self.historical_security_quotes = historical_security_quotes
        self.start_date = historical_security_quotes[-1].date
        self.end_date = historical_security_quotes[0].date
        self.returns = HistoricalSecurityQuotePeriod.__compute_returns(historical_security_quotes)
        returns_list = HistoricalSecurityQuotePeriod.__returns_list(historical_security_quotes)
        self.returns_mean = mean(returns_list)
        self.returns_variance = var(returns_list)
        self.sharpe_ratio = self.returns / self.returns_variance

    def get_close_price_list(self):
        res = []
        for historical_quote in self.historical_security_quotes:
            res.append(float(historical_quote.adjusted_close))

        return res

    def get_historical_security_quotes(self):
        return self.historical_security_quotes

    def get_returns(self):
        return self.returns

    def get_returns_mean(self):
        return self.returns_mean

    @staticmethod
    def __compute_returns(historical_security_quotes):
        if len(historical_security_quotes) == 0:
            return 0.0

        return 100*(float(historical_security_quotes[-1].adjusted_close) - float(historical_security_quotes[0].open)) \
                    / float(historical_security_quotes[0].open)

    @staticmethod
    def __returns_list(historical_security_quotes):
        if len(historical_security_quotes) == 0:
            return []

        res = []
        start_price = float(historical_security_quotes[0].open)
        for historical_quote in historical_security_quotes:
            res.append(100 * (float(historical_quote.adjusted_close) - start_price) / start_price)
            start_price = float(historical_quote.adjusted_close)

        return res

    def __str__(self):

        res = ""
        res += "Symbol - Date - Open - High - Low - Close - Volume - Adjusted Close - Change" + "\n"

        for quote in self.historical_security_quotes:
            res += str(quote) + "\n"

        return res + "\n" \
               + "Start Date - End Date - Returns Mean - Returns - Returns Variance - Sharpe Ratio \n" + \
               str(self.start_date) + " " + str(self.end_date) + " " \
               + str(self.returns_mean) + "% " + str(self.returns) + "% " + str(self.returns_variance) + "% " \
               + str(self.sharpe_ratio) + "\n"