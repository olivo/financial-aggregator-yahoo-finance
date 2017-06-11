from historical_security_quote_helper import *

__sp_500_symbol = 'SPY'
__acwi_ex_us_symbol = 'ACWX'
__bloomberg_barclays_us_aggregate_bond_symbol = 'AGG'

def dual_momentum_investing(start_day, start_month, start_year):
    end_day = start_day
    end_month = start_month
    end_year = str(int(start_year) + 1)

    sp_500_historical_security_quote_period = request_security_historical_quote_period(__sp_500_symbol, start_day, start_month, start_year, \
                                                                                             end_day, end_month, end_year)

    if sp_500_historical_security_quote_period != None:
        print 'S&P 500 return', sp_500_historical_security_quote_period.get_returns()
    else:
        print 'Could not retrieve returns for S&P 500'

    acwi_ex_us_historical_security_quote_period = request_security_historical_quote_period(__acwi_ex_us_symbol, start_day,
                                                                                       start_month, start_year, \
                                                                                       end_day, end_month, end_year)

    if acwi_ex_us_historical_security_quote_period != None:
        print 'ACWI ex-US return', acwi_ex_us_historical_security_quote_period.get_returns()
    else:
        print 'Could not retrieve returns for ACWI ex-US'

    bloomgerg_barclays_us_aggregate_bond_historical_security_quote_period = request_security_historical_quote_period(__bloomberg_barclays_us_aggregate_bond_symbol,
                                                                                           start_day,
                                                                                           start_month, start_year, \
                                                                                           end_day, end_month, end_year)

    if bloomgerg_barclays_us_aggregate_bond_historical_security_quote_period != None:
        print 'Bloomberg Barclays US Aggregate Bond return', bloomgerg_barclays_us_aggregate_bond_historical_security_quote_period
    else:
        print 'Could not retrieve returns for Bloomberg Barclays US Aggregate Bond'


def test_dual_momentum_investing():
    start_day = '9'
    start_month = '6'
    start_year = '2016'

    dual_momentum_investing(start_day, start_month, start_year)




