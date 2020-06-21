from pokerpy.cards_many import *
from pokerpy.players import Player


class Evaluator:
    def __init__(self, conv: CardConverter):
        self._conv = conv

    def winner(self, *player):
        #player.index(0)
        pass

    def headToheadWinner(player1: Player, player2: Player):
        _list = []
        if player1.score > player2.score:
                _list.append(player1)
                return _list
        elif player1.score < player2.score:
                _list.append(player2)
                return _list
        else:
            _reverseRange = list(range(5))
            _reverseRange.reverse()
            for n in _reverseRange:
                if player1.cards.bestFiveCards[n].kind > player2.cards.bestFiveCards[n].kind:
                    _list.append(player1)
                    break
                elif player1.cards.bestFiveCards[n].kind < player2.cards.bestFiveCards[n].kind:
                    _list.append(player2)
                    break
                else:
                    # Here add suitRule
                    if n == 0:
                        _list.append(player1)
                        _list.append(player2)
                        break
        return _list
