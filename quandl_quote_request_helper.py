from collections import deque
import csv
import urllib2

from historical_security_quote import HistoricalSecurityQuote

__quandl_historical_security_quote_request_url_template = '''
https://www.quandl.com/api/v3/datasets/WIKI/{0}.csv?start_date={1}-{2}-{3}&end_date={4}-{5}-{6}&order=desc
'''

def request_security_historical_quotes_from_quandl(symbol, start_day, start_month, start_year, end_day, end_month, end_year):
    request_url = __quandl_historical_security_quote_request_url_template.format(symbol, start_year, start_month, start_day, \
                                                                          end_year, end_month, end_day, end_year)
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
    data['adjusted_close'] = quote[11]

    return data