from collections import deque
import csv
from historical_security_quote import HistoricalSecurityQuote
from historical_security_quote_period import HistoricalSecurityQuotePeriod
import urllib2

__historical_security_quote_request_url_template = '''
http://ichart.yahoo.com/table.csv?s={0}&a={1}&b={2}&c={3}&d={4}&e={5}&f={6}&g={7}&ignore=.csv
'''

def request_security_historical_quote_period(symbol, start_day, start_month, start_year, end_day, end_month, end_year, frequency):
    return HistoricalSecurityQuotePeriod(request_security_historical_quotes(symbol, start_day, start_month, start_year, end_day, end_month, end_year, frequency))

def request_security_historical_quotes(symbol, start_day, start_month, start_year, end_day, end_month, end_year, frequency):
    request_url = __historical_security_quote_request_url_template.format(symbol, start_month - 1, start_day, start_year, \
                                                                          end_month - 1, end_day, end_year, frequency)
    reader = csv.reader(urllib2.urlopen(request_url))

    historical_security_quotes = deque()

    reader.next()

    for quote in reader:
        historical_security_quote_data = __construct_historical_security_quote_data(symbol, quote)
        historical_security_quote = HistoricalSecurityQuote(historical_security_quote_data)
        historical_security_quotes.appendleft(historical_security_quote)

    return historical_security_quotes

def __construct_historical_security_quote_data(symbol, quote):
    data = dict()
    data['symbol'] = symbol
    data['date'] = quote[0]
    data['open'] = quote[1]
    data['high'] = quote[2]
    data['low'] = quote[3]
    data['close'] = quote[4]
    data['volume'] = quote[5]
    data['adjusted_close'] = quote[6]

    return data