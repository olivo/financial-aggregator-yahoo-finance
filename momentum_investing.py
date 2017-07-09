from datetime import date
from historical_security_quote_helper import *

__sp_500_symbol = 'SPY'
__acwi_ex_us_symbol = 'ACWX'
__bloomberg_barclays_us_aggregate_bond_symbol = 'AGG'

def dual_momentum_investing(end_day, end_month, end_year):
    start_day = end_day
    start_month = end_month
    start_year = end_year - 1

    sp_500_historical_security_quote_period = request_security_historical_quote_period(__sp_500_symbol, start_day, start_month, start_year, \
                                                                                             end_day, end_month, end_year)

    if sp_500_historical_security_quote_period != None:
        print 'S&P 500 return', sp_500_historical_security_quote_period.get_cumulative_returns()
    else:
        print 'Could not retrieve returns for S&P 500'

    acwi_ex_us_historical_security_quote_period = request_security_historical_quote_period(__acwi_ex_us_symbol, start_day,
                                                                                       start_month, start_year, \
                                                                                       end_day, end_month, end_year)

    if acwi_ex_us_historical_security_quote_period != None:
        print 'ACWI ex-US return', acwi_ex_us_historical_security_quote_period.get_cumulative_returns()
    else:
        print 'Could not retrieve returns for ACWI ex-US'

    bloomgerg_barclays_us_aggregate_bond_historical_security_quote_period = request_security_historical_quote_period(__bloomberg_barclays_us_aggregate_bond_symbol,
                                                                                           start_day,
                                                                                           start_month, start_year, \
                                                                                           end_day, end_month, end_year)

    if bloomgerg_barclays_us_aggregate_bond_historical_security_quote_period != None:
        print 'Bloomberg Barclays US Aggregate Bond return', bloomgerg_barclays_us_aggregate_bond_historical_security_quote_period.get_cumulative_returns()
    else:
        print 'Could not retrieve returns for Bloomberg Barclays US Aggregate Bond'

    if sp_500_historical_security_quote_period != None and \
            (acwi_ex_us_historical_security_quote_period == None or \
            sp_500_historical_security_quote_period.get_cumulative_returns() > acwi_ex_us_historical_security_quote_period.get_cumulative_returns()):
        if sp_500_historical_security_quote_period != None and \
            (bloomgerg_barclays_us_aggregate_bond_historical_security_quote_period == None or \
            sp_500_historical_security_quote_period.get_cumulative_returns() > bloomgerg_barclays_us_aggregate_bond_historical_security_quote_period.get_cumulative_returns()):
                return __sp_500_symbol
        else:
                return __bloomberg_barclays_us_aggregate_bond_symbol
    else:
        if acwi_ex_us_historical_security_quote_period != None and \
            (bloomgerg_barclays_us_aggregate_bond_historical_security_quote_period == None or \
             acwi_ex_us_historical_security_quote_period.get_cumulative_returns() > bloomgerg_barclays_us_aggregate_bond_historical_security_quote_period.get_cumulative_returns()):
                return __acwi_ex_us_symbol
        else:
                return __bloomberg_barclays_us_aggregate_bond_symbol



def test_dual_momentum_investing():
    today_date = date.today()

    best_momentum_symbol = dual_momentum_investing(today_date.day, today_date.month, today_date.year)
    print 'The recommended symbol according to momentum investing is:', best_momentum_symbol



