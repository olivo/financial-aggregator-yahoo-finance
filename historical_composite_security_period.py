from functools import reduce
from numpy import mean, var

class HistoricalCompositeSecurityPeriod:
    def __init__(self, historical_composite_securities):
            self.historical_composite_securities = historical_composite_securities

            self.start_date = historical_composite_securities[-1].date
            self.end_date = historical_composite_securities[0].date