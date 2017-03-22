from functools import reduce
from numpy import mean, var

class HistoricalSecurityQuotePeriod:
    def __init__(self, historical_security_quotes):
        self.historical_security_quotes = historical_security_quotes
        self.start_date = historical_security_quotes[-1].date
        self.end_date = historical_security_quotes[0].date
        returns_list = HistoricalSecurityQuotePeriod.__returns_list(historical_security_quotes)
        self.returns_mean = mean(returns_list)
        self.returns_variance = var(returns_list)

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
               + "Start Date - End Date - Returns Mean - Returns Variance \n" + \
               str(self.start_date) + " " + str(self.end_date) + " " \
               + str(self.returns_mean) + "% " + str(self.returns_variance) + "% \n";