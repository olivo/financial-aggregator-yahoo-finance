from functools import reduce
from numpy import mean, var

class HistoricalCompositeSecurityPeriod:
    def __init__(self, historical_composite_securities):
            self.historical_composite_securities = historical_composite_securities

            self.start_date = historical_composite_securities[-1].date
            self.end_date = historical_composite_securities[0].date
            #returns_list = HistoricalSecurityQuotePeriod.__returns_list(historical_security_quotes)
            #self.returns_mean = mean(returns_list)
            #self.returns_variance = var(returns_list)

            #apple_historical_security_quote_period = request_security_historical_quote_period(symbol, start_day,
            #                                                                                  start_month, \
            #                                                                                  start_year, end_day,
            #                                                                                  end_month, \
            #                                                                                  end_year, frequency)