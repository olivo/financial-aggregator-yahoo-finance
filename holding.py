class Holding:
    def __init__(self, data):
        self.symbol = data['symbol']
        self.name = data['name']
        self.weight = data['weight']
        self.sector = data['sector']

    def clone(self):
        data = dict()
        data['symbol'] = self.symbol
        data['name'] = self.name
        data['weight'] = self.weight
        data['sector'] = self.sector

        return Holding(data)

    def __str__(self):
        return str(self.symbol) + " " + str(self.name) + " " + str(self.weight) + " " + str(self.sector)