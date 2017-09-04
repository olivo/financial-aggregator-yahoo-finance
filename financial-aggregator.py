from beta_predictor import BetaPredictor
from composite_security import CompositeSecurity
from security_helper import request_security, request_sp500_holdings
from historical_security_quote_helper import *
from historical_security_quote_period import HistoricalSecurityQuotePeriod
from historical_composite_security_period_helper import expected_return_composite_securities_for_period, find_optimal_composite_security
from mean_variance_optimizer import *
from momentum_investing import *

__top_us_stock_market_indices = ['^DJI', '^GSPC', '^IXIC', '^RUA', '^RUT', '^RUI']
__top_us_tech_stocks = ['AAPL', 'AMZN', 'FB', 'GOOGL', 'MSFT']
__top_foreign_stock_market_indices = ['ACWX']
__top_bond_market_indices = ['AGG']

print "The information for the top US tech stocks is the following:"

for symbol in __top_us_tech_stocks:
    print request_security(symbol)

print ""

print "The information for the top US stock market indices is the following:"

for symbol in __top_us_stock_market_indices:
    print request_security(symbol)

print ""

print "The information for the top foreign stock market indices is the following:"

for symbol in __top_foreign_stock_market_indices:
    print request_security(symbol)

print ""

print "The information for the top bond market indices is the following:"

for symbol in __top_bond_market_indices:
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
start_month = 8
start_year = 2016
end_day = 20
end_month = 8
end_year = 2017

apple_historical_security_quote_period = request_security_historical_quote_period(symbol, start_day, start_month, \
                                                                                  start_year, end_day, end_month, \
                                                                                  end_year)

print apple_historical_security_quote_period

print "\n"

beta_linear_regression = BetaPredictor.LinearRegression(symbol, start_day, start_month, start_year, end_day, end_month, end_year)
print 'The beta of ' + symbol + ' according to linear regression is:' + str(beta_linear_regression[0])

tech_historical_quotes = []
print "The historical security quotes from the tech sector in the S&p 500 sorted by the Sharpe Ratio"
technology_symbols = ['AMZN', 'AAPL', 'GOOGL', 'AMD', 'NVDA', 'JD', 'SINA', 'VIPS', 'FB', 'MU', 'BABA', 'WB', 'LRCX', 'NFLX', 'PCLN', 'RE', 'BAC', 'JPM', 'BRK.B']

#for tech_holding in technology_holdings:
#    tech_historical_quote = request_security_historical_quote_period(tech_holding.symbol, start_day, start_month, \
#                                                                                  start_year, end_day, end_month, \
#                                                                                  end_year)
for technology_symbol in technology_symbols:
    tech_historical_quote = request_security_historical_quote_period(technology_symbol, start_day, start_month, \
                                                                                  start_year, end_day, end_month, \
                                                                                  end_year)
    if tech_historical_quote is not None:
        tech_historical_quotes.append(tech_historical_quote)

tech_historical_quotes.sort(key=lambda x: x.get_sharpe_ratio(), reverse=True)

for tech_historical_quote in tech_historical_quotes:
    print 'Security quotes for ' + tech_historical_quote.get_symbol()
    print tech_historical_quote

"""
sp_holdings = holdings.get_holdings()
stock_candidates = ['AAPL', 'AMZN', 'FB', 'GOOGL']
top_tech_holdings_composite_security = CompositeSecurity(filter(lambda x: x.symbol in stock_candidates, sp_holdings))

best_composite_security = find_optimal_composite_security(top_tech_holdings_composite_security, stock_candidates, 0, 100, \
                                                          start_day, start_month, start_year, end_day, end_month, end_year)

print "The best composite security is: "
print str(best_composite_security)

best_composite_security_expected_return = expected_return_composite_securities_for_period(best_composite_security, None, start_day, start_month, start_year, \
                                                                                          end_day, end_month, end_year)

print "The expected return per period for the best composite security is:", best_composite_security_expected_return
"""

fifty_day_moving_average = request_n_day_moving_average(symbol, 50, end_day, end_month, end_year)
print "The 50-day moving average for", symbol, "is", fifty_day_moving_average

two_hundred_day_moving_average = request_n_day_moving_average(symbol, 200, end_day, end_month, end_year)
print "The 200-day moving average for", symbol, "is", two_hundred_day_moving_average

print "Testing momentum investing"
test_dual_momentum_investing()

mean_variance_symbols = ['AAPL', 'AMZN']
print 'Starting mean variance optimization on:', str(mean_variance_symbols)
mean_variance_historical_quote_periods = deque()

for mean_variance_symbol in mean_variance_symbols:
    historical_quote_period = request_security_historical_quote_period(mean_variance_symbol, \
                                                                       start_day, start_month, start_year, \
                                                                       end_day, end_month, end_year)
    if historical_quote_period is not None:
        mean_variance_historical_quote_periods.append(historical_quote_period)

mean_variance_optimizer = MeanVarianceOptimizer(mean_variance_historical_quote_periods)
print 'The portfolio with the minimum variance has variance:', mean_variance_optimizer.minimize_function()