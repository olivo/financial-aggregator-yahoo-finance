from security_helper import request_security, request_sp500_holdings
from historical_security_quote_helper import request_security_historical_quotes
from historical_security_quote_period import HistoricalSecurityQuotePeriod

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
start_day = 20
start_month = 3
start_year = 2016
end_day = 20
end_month = 3
end_year = 2017
frequency = "d"

apple_historical_quotes = request_security_historical_quotes(symbol, start_day, start_month, start_year, end_day, end_month, \
                                                             end_year, frequency)
apple_historical_security_quote_period = HistoricalSecurityQuotePeriod(apple_historical_quotes)

print apple_historical_security_quote_period

print "\n"

print "The healthcare stock with best average monthly return in the S&P 500 during 03/20/2016 - 03/20/2017 is: "
tech_historical_security_quotes = map(lambda x: HistoricalSecurityQuotePeriod(\
                                            request_security_historical_quotes(x, start_day, start_month, start_year, \
                                                                               end_day, end_month, end_year, frequency)) \
                                  , map(lambda x: x.symbol, healthcare_holdings))

print max(tech_historical_security_quotes, key = lambda x: x.returns_mean)