from composite_security import CompositeSecurity
from security_helper import request_security, request_sp500_holdings
from historical_security_quote_helper import request_security_historical_quotes, request_security_historical_quote_period
from historical_security_quote_period import HistoricalSecurityQuotePeriod
from historical_composite_security_period_helper import expected_return_composite_securities_for_period

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

print holdings

print ""

print "The holdings of S&P 500 from the technology sector are:"
technology_holdings = holdings.get_holdings_by_sector("Information Technology")
for holding in technology_holdings:
    print holding

print ""

print "The holdings of S&P 500 from the financial sector are:"
financial_holdings = holdings.get_holdings_by_sector("Financials")
for holding in financial_holdings:
    print holding

print ""

print "The holdings of S&P 500 from the healthcare sector are:"
healthcare_holdings = holdings.get_holdings_by_sector("Health Care")
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

apple_historical_security_quote_period = request_security_historical_quote_period(symbol, start_day, start_month, \
                                                                                  start_year, end_day, end_month, \
                                                                                  end_year, frequency)

print apple_historical_security_quote_period

print "\n"

#print "The healthcare stock with best average monthly return in the S&P 500 during 03/20/2016 - 03/20/2017 is: "
#healthcare_historical_security_quotes = map(lambda x: HistoricalSecurityQuotePeriod(\
#                                            request_security_historical_quotes(x, start_day, start_month, start_year, \
#                                                                               end_day, end_month, end_year, frequency)) \
#                                        , map(lambda x: x.symbol, healthcare_holdings))

#print max(healthcare_historical_security_quotes, key = lambda x: x.returns_mean)

sp_holdings = holdings.get_holdings()
top_tech_holdings_composite_security = CompositeSecurity(filter(lambda x: x.symbol in __top_us_tech_stocks, sp_holdings))

top_tech_holdings_composite_security.set_weight('AAPL', 1.0)
top_tech_holdings_composite_security.set_weight('AMZN', 0.0)
top_tech_holdings_composite_security.set_weight('GOOGL', 0.0)
top_tech_holdings_composite_security.set_weight('FB', 0.0)
top_tech_holdings_composite_security.set_weight('MSFT', 0.0)

print "The expected average return of a composite security of top tech stocks (AAPL, AMZN, GOOGL, FB, MSFT) is: "

expected_return_composite_security = expected_return_composite_securities_for_period(top_tech_holdings_composite_security \
                                                                                     , start_day, start_month, start_year, \
                                                                                     end_day, end_month, end_year, frequency)
print expected_return_composite_security

