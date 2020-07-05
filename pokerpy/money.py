class Cash:
    # fiches (useless?)
    def __init__(self, currency='$', amount=0):
        self._amount = amount
        self._currency = currency

    def show_on_console(self):
        return '{} {}'.format(self._currency, self._amount)


# you need a list of Pot for limit game
class Pot(Cash):

    def __init__(self):
        super().__init__()
        self._players_list = []

    def add_players(self, *players):
        self._players_list.extend([p for p in players])

    def remove_player(self, player):
        self._players_list.remove(player)

    def take_money(self, bet):
        self._amount = self._amount + bet

    def give_everything(self):
        return self._amount

    def show_players(self):
        print([p for p in self._players_list])


class MoneyRules:
    # minBet:
    # maxBet: minBet * n
    # maxRise:
    # richiestaPoste
    # dealerBet
    # incrementType
    # incrementTime
    # modalitaIncremento=(nullo,a tempo,giri,eliminazioneGiocatore)
    # setBlind: [notAllowed, due, allowed]
    # small  blind, big blind, over
    # minBetType: [check, blind]
    # resti / no limits
    # obbligo di prendere posta
    # allowLowerBets
    pass

