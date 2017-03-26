class CompositeSecurity:
    def __init__(self, holdings):
        self.holdings = dict()

        for holding in holdings:
            self.holdings[holding.symbol] = holding

    def get_holdings_by_sector(self, sector):
        return filter(lambda h: h.sector == sector, self.holdings.values())

    def get_holdings(self):
        return self.holdings.values()

    def set_weight(self, symbol, weight):
        if (symbol in self.holdings):
            self.holdings[symbol].weight = weight

    def __str__(self):
        res = ""
        for holding in self.holdings.values():
            res += str(holding) + "\n"

        return res
