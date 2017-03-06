import json
import requests

symbols = ['AAPL', 'AMZN', 'FB', 'GOOGL', 'MSFT']

request_url_template = '''
https://query.yahooapis.com/v1/public/yql?q=select * from yahoo.finance.quotes where symbol in ("{0}") 
&format=json&env=store://datatables.org/alltableswithkeys&callback=
'''

for symbol in symbols:
    request_url = request_url_template.format(symbol)
    json_response = requests.post(request_url).json()
    results = json_response['query']['results']['quote']
    print results['symbol'], results['LastTradePriceOnly'], results['Change_PercentChange']
