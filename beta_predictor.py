from scipy import stats
from security_helper import request_security, request_sp500_holdings
from historical_security_quote_helper import *

class BetaPredictor:
    __SP500_symbol = 'SPY'

    @staticmethod
    def LinearRegression(symbol, start_day, start_month, start_year, end_day, end_month, end_year):

        stock_historical_security_quote_period = request_security_historical_quote_period(symbol, start_day, start_month, \
                                                                                    start_year, end_day, end_month, \
                                                                                    end_year)

        stock_historical_returns = stock_historical_security_quote_period.get_returns()

        market_historical_security_quote_period = request_security_historical_quote_period(BetaPredictor.__SP500_symbol, start_day, start_month, \
                                                                                           start_year, end_day, end_month, \
                                                                                           end_year)

        market_historical_returns = market_historical_security_quote_period.get_returns()

        return stats.linregress(market_historical_returns, stock_historical_returns)

