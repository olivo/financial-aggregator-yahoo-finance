from security_helper import request_security, request_sp500_holdings

__top_us_stock_market_indices = ['^DJI', '^GSPC', '^IXIC', '^RUA', '^RUT', '^RUI']
__top_us_tech_stocks = ['AAPL', 'AMZN', 'FB', 'GOOGL', 'MSFT']

print "The information for the top US tech stocks is the following:"

for symbol in __top_us_tech_stocks:
    print request_security(symbol)

print ""

print "The information for the top US stock market indices is the following:"

for symbol in __top_us_stock_market_indices:
    print request_security(symbol)

print ""

holdings = request_sp500_holdings()

print "The holdings of S&P 500 (tracked by iShares Core S&P 500 ETF) are:"

for holding in holdings:
    print holding