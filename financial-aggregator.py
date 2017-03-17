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

print ""

print "The holdings of S&P 500 from the technology sector are:"
technology_holdings = filter(lambda h: h.sector == "Information Technology", holdings)
for holding in technology_holdings:
    print holding

print ""

print "The holdings of S&P 500 from the financial sector are:"
financial_holdings = filter(lambda h: h.sector == "Financials", holdings)
for holding in financial_holdings:
    print holding

print ""

print "The holdings of S&P 500 from the healthcare sector are:"
healthcare_holdings = filter(lambda h: h.sector == "Health Care", holdings)
for holding in healthcare_holdings:
    print holding