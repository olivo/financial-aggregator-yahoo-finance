from composite_security import CompositeSecurity

class HistoricalCompositeSecurity(CompositeSecurity):
    def __init__(self, date, holdings, holdings_return):
        CompositeSecurity.__init__(self, holdings)
        self.date = date
        self.holdings_return = holdings_return

    def __str__(self):
        return str(self.date) + " " + str(self.holdings_return) + "\n" + CompositeSecurity.__str__(self)