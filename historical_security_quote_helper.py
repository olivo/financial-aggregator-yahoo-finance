import csv
from historical_security_quote import HistoricalSecurityQuote
import urllib2

__historical_security_quote_request_url_template = '''
http://ichart.yahoo.com/table.csv?s={0}&a={1}&b={2}&c={3}&d={4}&e={5}&f={6}&g={7}&ignore=.csv
'''

def request_security_historical_quotes(symbol, startDay, startMonth, startYear, endDay, endMonth, endYear, frequency):
    request_url = __historical_security_quote_request_url_template.format(symbol, startMonth - 1, startDay, startYear, \
                                                                          endMonth - 1, endDay, endYear, frequency)
    reader = csv.reader(urllib2.urlopen(request_url))

    historical_security_quotes = []

    reader.next()

    for quote in reader:
        historical_security_quote_data = __construct_historical_security_quote_data(symbol, quote)
        historical_security_quote = HistoricalSecurityQuote(historical_security_quote_data)
        historical_security_quotes.append(historical_security_quote)

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