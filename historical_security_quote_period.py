class HistoricalSecurityQuotePeriod:
    def __init__(self, historicalSecurityQuotes):
        self.historicalSecurityQuotes = historicalSecurityQuotes
        self.startDate = historicalSecurityQuotes[-1].date
        self.endDate = historicalSecurityQuotes[0].date

    def __str__(self):

        res = ""
        for quote in self.historicalSecurityQuotes:
            res += str(quote) + "\n"

        return str(self.startDate) + " - " + str(self.endDate) + "\n" \
               + res;