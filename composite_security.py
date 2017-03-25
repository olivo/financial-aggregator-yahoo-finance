class CompositeSecurity:
    def __init__(self, holdings):
        self.holdings = holdings

    def get_holdings_by_sector(self, sector):
        return filter(lambda h: h.sector == sector, self.holdings)

    def __str__(self):
        res = ""
        for holding in self.holdings:
            res += str(holding) + "\n"

        return res
