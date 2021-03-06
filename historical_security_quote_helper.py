from collections import deque
from historical_security_quote_period import HistoricalSecurityQuotePeriod
from quandl_quote_request_helper import request_security_historical_quotes_from_quandl
from yahoo_quote_request_helper import request_security_historical_quotes_from_yahoo
import itertools
from numpy import mean
import sys

def request_security_historical_quote_period(symbol, start_day, start_month, start_year, end_day, end_month, end_year):
    try:
        security_historical_quotes = request_security_historical_quotes_from_yahoo(symbol, start_day, start_month, start_year, end_day, end_month, end_year)
        if security_historical_quotes is not None and len(security_historical_quotes.index) > 0:
            return HistoricalSecurityQuotePeriod(symbol, security_historical_quotes)
        elif security_historical_quotes == []:
            print 'WARNING: Found no historical quotes for', symbol, 'for the given period'
            return None
        else:
            print 'ERROR: Could not retrieve quotes for', symbol
            return None
    except Exception, e:
        print 'Exception while trying to request historical data for', symbol
        print str(e)
        return None

def request_n_day_moving_average(symbol, n, end_day, end_month, end_year):
    one_year_security_quote_period = request_security_historical_quote_period(symbol, end_day, end_month, end_year - 1, end_day, end_month, end_year)

    if one_year_security_quote_period != None:
        one_year_security_quotes = one_year_security_quote_period.get_historical_security_quotes()

        last_n_days_security_quotes = one_year_security_quotes.ix[:-n]
        last_n_days_security_quotes = HistoricalSecurityQuotePeriod(symbol, last_n_days_security_quotes)

        return last_n_days_security_quotes.get_price_mean()
    else:
        return None