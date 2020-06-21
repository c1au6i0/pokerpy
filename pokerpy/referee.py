from pokerpy.converters import *
from pokerpy.cards_many import *
from pokerpy.players import Player


class Evaluator:
    def __init__(self, conv: CardConverter):
        self._conv = conv

    def winner(self, *player):
        #player.index(0)
        pass

    def headToheadWinner(player1: Player, player2: Player):
        if player1.score > player2.score:
            return player1.name + ' wins'
        elif player1.score < player2.score:
            return player2.name + ' wins'
        else:
            _reverseRange = list(range(5))
            _reverseRange.reverse()
            for n in _reverseRange:
                if player1.cards.bestFiveCards[n].kind > player2.cards.bestFiveCards[n].kind:
                    return player1.name + ' wins'
                elif player1.cards.bestFiveCards[n].kind < player2.cards.bestFiveCards[n].kind:
                    return player2.name + ' wins'
                else:
                    # Here add suitRule
                    if n == 4:
                        return 'Pareggio'
