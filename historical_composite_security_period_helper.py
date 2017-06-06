from composite_security import CompositeSecurity
from historical_security_quote_helper import request_security_historical_quote_period

def expected_return_composite_securities_for_period(composite_security, historical_quote_period_by_symbol, start_day, start_month, start_year, \
                                                           end_day, end_month, end_year):

    if historical_quote_period_by_symbol is None:
        symbols = map(lambda x: x.symbol, composite_security.get_holdings())
        historical_quote_period_by_symbol = compute_historical_quote_period_by_symbol(symbols, \
                                                                                      start_day, start_month,
                                                                                      start_year, end_day, end_month,
                                                                                      end_year)

    expected_return = 0.0
    for holding in composite_security.get_holdings():
        expected_return += holding.weight * historical_quote_period_by_symbol[holding.symbol].returns_mean

    return expected_return

def compute_historical_composite_securities_for_period(composite_security, start_day, start_month, start_year, \
                                                       end_day, end_month, end_year):
    return 0.0

def compute_historical_quote_period_by_symbol(symbols, start_day, start_month, start_year, end_day, end_month, end_year):
    historical_quote_period_by_symbol = dict()
    for symbol in symbols:
        historical_quote_period_by_symbol[symbol] = request_security_historical_quote_period(symbol, \
                                                                                             start_day,
                                                                                             start_month, \
                                                                                             start_year,
                                                                                             end_day,
                                                                                             end_month, \
                                                                                             end_year)
    return historical_quote_period_by_symbol

def find_optimal_composite_security(composite_security, security_candidates, current_security_index, remaining_percentage, \
                                    start_day, start_month, start_year, end_day, end_month, end_year):

    symbols = map(lambda x: x.symbol, composite_security.get_holdings())
    historical_quote_period_by_symbol = compute_historical_quote_period_by_symbol(symbols, \
                                                                                  start_day, start_month, start_year, end_day, end_month, end_year)

    for holding in composite_security.get_holdings():
        composite_security.set_weight(holding.symbol, 0.0)

    best_composite_security = composite_security.clone()
    best_composite_security_expected_return = expected_return_composite_securities_for_period(best_composite_security, \
                                                                                historical_quote_period_by_symbol, \
                                                                                start_day, start_month, start_year, \
                                                                                end_day, end_month, end_year)

    print "START COMPOSITE SECURITY:"
    print str(best_composite_security)
    print "START RETURN:", best_composite_security_expected_return

    _find_optimal_composite_security_helper(composite_security, historical_quote_period_by_symbol, security_candidates, \
                                            current_security_index,
                                            remaining_percentage, \
                                            start_day, start_month, start_year, end_day, end_month, end_year, \
                                            best_composite_security)

    return best_composite_security

def _find_optimal_composite_security_helper(composite_security, historical_quote_period_by_symbol, \
                                            security_candidates, current_security_index, remaining_percentage, \
                                            start_day, start_month, start_year, end_day, end_month, end_year, \
                                            best_composite_security):

    if current_security_index == len(security_candidates) - 1:
        print "END OF BACKTRACKING"
        composite_security.set_weight(security_candidates[current_security_index], remaining_percentage / 100.00)
        composite_security_expected_return = expected_return_composite_securities_for_period(composite_security, \
                                                                                             historical_quote_period_by_symbol, \
                                                                                    start_day, start_month, start_year, \
                                                                                end_day, end_month, end_year)
        best_composite_security_expected_return = expected_return_composite_securities_for_period(best_composite_security, \
                                                                                                  historical_quote_period_by_symbol, \
                                                                                                  start_day, start_month,
                                                                                                  start_year, \
                                                                                                  end_day, end_month,
                                                                                                  end_year)

        print "CURRENT SECURITY:"
        print str(composite_security)
        print "CURRENT RETURN :", composite_security_expected_return, ", BEST RETURN:", best_composite_security_expected_return

        if composite_security_expected_return > best_composite_security_expected_return:
            print composite_security_expected_return, "is better than", best_composite_security_expected_return
            best_composite_security.copy(composite_security)
    else:
        for weight in range(0, remaining_percentage, 1):
            composite_security.set_weight(security_candidates[current_security_index], weight / 100.00)
            _find_optimal_composite_security_helper(composite_security, historical_quote_period_by_symbol, \
                                                    security_candidates, current_security_index + 1, remaining_percentage - weight, \
                                                    start_day, start_month, start_year, end_day, end_month, end_year, \
                                                    best_composite_security)