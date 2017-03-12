import json
import requests
from security import Security

__security_request_url_template = '''
https://query.yahooapis.com/v1/public/yql?q=select * from yahoo.finance.quotes where symbol in ("{0}") 
&format=json&env=store://datatables.org/alltableswithkeys&callback=
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
