from collections import deque
from historical_security_quote_period import HistoricalSecurityQuotePeriod
from quandl_quote_request_helper import request_security_historical_quotes_from_quandl

import itertools
from numpy import mean
import sys

__yahoo_historical_security_quote_request_url_template = '''
http://ichart.yahoo.com/table.csv?s={0}&a={1}&b={2}&c={3}&d={4}&e={5}&f={6}&g={7}&ignore=.csv
'''

def request_security_historical_quote_period(symbol, start_day, start_month, start_year, end_day, end_month, end_year):
    try:
        security_historical_quotes = request_security_historical_quotes_from_quandl(symbol, start_day, start_month, start_year, end_day, end_month, end_year)
        return HistoricalSecurityQuotePeriod(security_historical_quotes)
    except Exception:
        print 'Exception while trying to request historical data for', symbol
        print sys.exc_info()[0]
        return None

def request_n_day_moving_average(symbol, n, end_day, end_month, end_year):
    one_year_security_quote_period = request_security_historical_quote_period(symbol, end_day, end_month, end_year - 1, end_day, end_month, end_year)

    if one_year_security_quote_period != None:
        one_year_security_quotes = one_year_security_quote_period.get_historical_security_quotes()

        last_two_hundred_days_security_quotes = deque(itertools.islice(one_year_security_quotes, len(one_year_security_quotes) - n, None))
        last_two_hundred_days_security_quotes = HistoricalSecurityQuotePeriod(last_two_hundred_days_security_quotes)

        return mean(last_two_hundred_days_security_quotes.get_close_price_list())
    else:
        return None