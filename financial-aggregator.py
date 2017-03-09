import json
import requests

top_us_stock_market_indices = ['^DJI', '^GSPC', '^IXIC', '^RUA', '^RUT', '^RUI']

top_us_tech_stocks = ['AAPL', 'AMZN', 'FB', 'GOOGL', 'MSFT']

request_url_template = '''
https://query.yahooapis.com/v1/public/yql?q=select * from yahoo.finance.quotes where symbol in ("{0}") 
&format=json&env=store://datatables.org/alltableswithkeys&callback=
'''

print "The information for the top US tech stocks is the following:"

for symbol in top_us_tech_stocks:
    request_url = request_url_template.format(symbol)
    json_response = requests.post(request_url).json()
    results = json_response['query']['results']['quote']
    print results['symbol'], results['Name'], results['LastTradePriceOnly'], results['Change_PercentChange']

print ""

print "The information for the top US stock market indices is the following:"

for symbol in top_us_stock_market_indices:
    request_url = request_url_template.format(symbol)
    json_response = requests.post(request_url).json()
    results = json_response['query']['results']['quote']
    print results['symbol'], results['Name'], results['LastTradePriceOnly'], results['Change_PercentChange']
