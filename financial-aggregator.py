from composite_security import CompositeSecurity
from security_helper import request_security, request_sp500_holdings
from historical_security_quote_helper import *
from historical_security_quote_period import HistoricalSecurityQuotePeriod
from historical_composite_security_period_helper import expected_return_composite_securities_for_period, find_optimal_composite_security

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
start_day = 1
start_month = 1
start_year = 2016
end_day = 12
end_month = 5
end_year = 2017

apple_historical_security_quote_period = request_security_historical_quote_period(symbol, start_day, start_month, \
                                                                                  start_year, end_day, end_month, \
                                                                                  end_year)

print apple_historical_security_quote_period

print "\n"

"""
sp_holdings = holdings.get_holdings()
stock_candidates = ['AAPL', 'AMZN', 'FB', 'GOOGL']
top_tech_holdings_composite_security = CompositeSecurity(filter(lambda x: x.symbol in stock_candidates, sp_holdings))

best_composite_security = find_optimal_composite_security(top_tech_holdings_composite_security, stock_candidates, 0, 100, \
                                                          start_day, start_month, start_year, end_day, end_month, end_year, frequency)

print "The best composite security is: "
print str(best_composite_security)

best_composite_security_expected_return = expected_return_composite_securities_for_period(best_composite_security, None, start_day, start_month, start_year, \
                                                                                          end_day, end_month, end_year, frequency)

print "The expected return per period for the best composite security is:", best_composite_security_expected_return
"""

fifty_day_moving_average = request_n_day_moving_average(symbol, 50, end_day, end_month, end_year)
print "The 50-day moving average for", symbol, " is", fifty_day_moving_average

two_hundred_day_moving_average = request_n_day_moving_average(symbol, 200, end_day, end_month, end_year)
print "The 200-day moving average for", symbol, " is", two_hundred_day_moving_average