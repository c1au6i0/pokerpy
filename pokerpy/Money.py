class Cash:
    # fiches (useless?)
    def __init__(self, currency='$', amount=1000):
        self._amount = amount
        self._currency = currency

    def showOnConsole(self):
        return '{} {}'.format(self.currency, self.amount)


# you need a list of Pot for limit game
class Pot(Cash):
    # playersList
    # addPlayer
    # removePlayer
    # takeMoney
    # giveMoney
    pass