from historical_security_quote_helper import request_security_historical_quote_period

def expected_return_composite_securities_for_period(composite_security, start_day, start_month, start_year, \
                                                           end_day, end_month, end_year, frequency):
    historical_quote_period_by_symbol = dict()
    for holding in composite_security.get_holdings():
        historical_quote_period_by_symbol[holding.symbol] = request_security_historical_quote_period(holding.symbol, \
                                                                                                     start_day,
                                                                                                     start_month, \
                                                                                                     start_year, end_day,
                                                                                                     end_month, \
                                                                                                     end_year, frequency)

    expected_return = 0.0
    for holding in composite_security.get_holdings():
        expected_return += holding.weight * historical_quote_period_by_symbol[holding.symbol].returns_mean

    return expected_return

def compute_historical_composite_securities_for_period(composite_security, start_day, start_month, start_year, \
                                                       end_day, end_month, end_year, frequency):
    return 0.0