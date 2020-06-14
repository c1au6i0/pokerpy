class Cash:
    # fiches (useless?)
    def __init__(self, currency='$', amount=0):
        self._amount = amount
        self._currency = currency

    def showOnConsole(self):
        return '{} {}'.format(self.currency, self.amount)


# you need a list of Pot for limit game
class Pot(Cash):

    def __init__(self):
        super().__init__()
        self._playersList = []

    def addPlayers(self, *players):
        self._playersList.append([p for p in players])
        print(self._playersList[0])

    def removePlayer(self, player):
        self._playersList.remove(player)

    def takeMoney(self, bet):
        self._amount = self._amount + bet

    def giveEverything(self):
        return self._amount

    def showPlayers(self):
        print([p for p in self._playersList])
