class Holding:
    def __init__(self, data):
        self.symbol = data['symbol']
        self.name = data['name']
        self.weight = data['weight']

    def __str__(self):
        return str(self.symbol) + " " + str(self.name) + " " + str(self.weight)