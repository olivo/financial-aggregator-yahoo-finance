import pandas
import re
import requests
import StringIO
import sys

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

    string_buffer = StringIO.StringIO(raw_response)

    dataframe = pandas.read_csv(string_buffer, index_col = 0, parse_dates = True)

    start_date = str(start_year) + "-" + str(start_month) + "-" + str(start_day)
    end_date = str(end_year) + "-" + str(end_month) + "-" + str(end_day)

    sliced_dataframe = dataframe.ix[start_date : end_date]

    return sliced_dataframe