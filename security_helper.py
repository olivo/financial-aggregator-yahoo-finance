import csv
from holding import Holding
import requests
from security import Security
import urllib2

__security_request_url_template = '''
https://query.yahooapis.com/v1/public/yql?q=select * from yahoo.finance.quotes where symbol in ("{0}") 
&format=json&env=store://datatables.org/alltableswithkeys&callback=
'''

__ishares_core_sp500_holdings_url = '''
https://www.ishares.com/us/products/239726/ishares-core-sp-500-etf/1467271812596.ajax?fileType=csv&fileName=IVV_holdings&dataType=fund
'''

def request_security(symbol):
    request_url = __security_request_url_template.format(symbol)
    json_response = requests.post(request_url).json()
    security_data = construct_security_data_from_response(json_response)
    return Security(security_data)
    
def construct_security_data_from_response(json_response):
    response_payload = json_response['query']['results']['quote']
    security_data = dict()
    security_data['symbol'] = response_payload['symbol']
    security_data['name'] = response_payload['Name']
    security_data['last_trade_price'] = response_payload['LastTradePriceOnly']
    
    if response_payload['Change_PercentChange'] != None:
        price_change = response_payload['Change_PercentChange'].split(" - ")
        security_data['price_change'] = price_change[0]
        security_data['price_percent_change'] = price_change[1]
    else:
        security_data['price_change'] = response_payload['Change_PercentChange']
        security_data['price_percent_change'] = response_payload['Change_PercentChange']

    return security_data

def request_sp500_holdings():
    holdings = []
    reader = csv.reader(urllib2.urlopen(__ishares_core_sp500_holdings_url))

    while reader.next() != ['\xc2\xa0']:
        continue

    reader.next()
    for csv_row in reader:
        if csv_row != ['\xc2\xa0']:
            holding_data = construct_sp500_holding_data_from_csv_row(csv_row)
            holdings.append(Holding(holding_data))

    return holdings

def construct_sp500_holding_data_from_csv_row(csv_row):
    holding_data = dict()
    holding_data['symbol'] = csv_row[0]
    holding_data['name'] = csv_row[1]
    holding_data['weight'] = csv_row[3]
    holding_data['sector'] = csv_row[8]

    return holding_data