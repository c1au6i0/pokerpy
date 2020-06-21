from pokerpy.converters import *
from pokerpy.cards_many import *
from pokerpy.players import Player


class Evaluator:
    def __init__(self, conv: CardConverter):
        self._conv = conv

    def winner(self, *player):
        #player.index(0)
        pass

    def headToheadWinner(self, player1: Player, player2: Player):
        if player1.score > player2.score:
            return player1.name + ' wins'
        elif player1.score < player2.score:
            return player2.name + ' wins'
        else:
            if player1.highestCard > player2.highestCard:
                return player1.name + ' wins'
            elif player1.highestCard < player2.highestCard:
                return player2.name + ' wins'
            else:
                return 'Pareggio'