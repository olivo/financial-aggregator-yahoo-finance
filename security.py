class Security:
    def __init__(self, data):
        self.symbol = data['symbol']
        self.name = data['name']
        self.last_trade_price = data['last_trade_price']
        self.price_change = data['price_change']
        self.price_percent_change = data['price_percent_change']

    def __str__(self):
        return str(self.symbol) + " " + str(self.name) + " " + str(self.last_trade_price) + " " + \
               str(self.price_change) + " " + str(self.price_percent_change)
