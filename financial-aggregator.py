from security_helper import request_security, request_sp500_holdings
from historical_security_quote_helper import request_security_historical_quotes

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

print ""

print "The historical quotes for Apple are:"
symbol = "AAPL"
startDay = 3
startMonth = 1
startYear = 2017
endDay = 3
endMonth = 3
endYear = 2017
frequency = "d"

apple_historical_quotes = request_security_historical_quotes(symbol, startDay, startMonth, startYear, endDay, endMonth, \
                                                             endYear, frequency)
print "Symbol - Date - Open - High - Low - Close - Volume - Adjusted Close"

for quote in apple_historical_quotes:
    print quote