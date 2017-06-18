from collections import deque
import csv
from datetime import date
import re
import requests
import sys
import urllib2

from historical_security_quote import HistoricalSecurityQuote

__older_yahoo_historical_security_quote_request_url_template = '''
http://ichart.yahoo.com/table.csv?s={0}&a={1}&b={2}&c={3}&d={4}&e={5}&f={6}&g={7}&ignore=.csv
'''

__yahoo_initial_historical_security_quote_request_url_template = '''
https://finance.yahoo.com/quote/{0}/history?p={0}
'''

__yahoo_final_historical_security_quote_request_url_template = '''
https://query1.finance.yahoo.com/v7/finance/download/{0}?period1={1}&period2={2}&interval=1d&events=history&crumb={3}
'''

def request_security_historical_quotes_from_yahoo(symbol, start_day, start_month, start_year, end_day, end_month, end_year):
    request_url = __yahoo_initial_historical_security_quote_request_url_template.format(symbol)

    session = requests.session()
    response = session.get(request_url)
    content = response.content

    m = re.search(r'(?<=\"CrumbStore\":{\"crumb\":\")([^"]+)(?=\"})', content)

    if m == None:
        print "ERROR: Could not retrieve request token while trying to download security quotes of", symbol
        return None

    cookie = m.group(0)

    period1 = 0
    period2 = sys.maxint

    request_url = __yahoo_final_historical_security_quote_request_url_template.format(symbol, period1, period2, cookie)
    raw_response = session.get(request_url).content
    response = raw_response.split('\n')
    reader = csv.reader(response)

    historical_security_quotes = deque()

    first_line = reader.next()

    for quote in reader:
        if len(quote) == 7 and quote[6] != 'null':
            historical_security_quote_data = __construct_historical_security_quote_data(symbol, quote)
            historical_security_quote = HistoricalSecurityQuote(historical_security_quote_data)
            historical_security_quotes.append(historical_security_quote)
        else:
            print 'WARNING: Potentially invalid quote was discarded:'
            print quote
            print '\n'

    filtered_historical_security_quotes = deque()
    start_date = date(start_year, start_month, start_day)
    end_date = date(end_year, end_month, end_day)

    for historical_security_quote in historical_security_quotes:
        if start_date <= historical_security_quote.get_date() and historical_security_quote.get_date() <= end_date:
            filtered_historical_security_quotes.append(historical_security_quote)

    return filtered_historical_security_quotes

def __construct_historical_security_quote_data(symbol, quote):
    data = dict()
    data['symbol'] = symbol
    data['date'] = __parsed_date(quote[0])
    data['open'] = quote[1]
    data['high'] = quote[2]
    data['low'] = quote[3]
    data['close'] = quote[4]
    data['adjusted_close'] = quote[5]
    data['volume'] = quote[6]

    return data

def __parsed_date(date_str):
    year, month, day = date_str.split('-')
    return date(int(year), int(month), int(day))