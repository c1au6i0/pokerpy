from pokerpy.players import Player
from pokerpy.cards_many import *
from pokerpy.rules import *


class Evaluator:

    @classmethod
    def initialize(cls, kind_of_deck=AMERICAN_DECK):
        ScoreRules.initialize(kind_of_deck)

    @classmethod
    def winners(cls, players):
        _winners = [players[0]]
        _best_player = players[0]
        for n in range(1, len(players)):
            if players[n].score > _best_player.score:
                _winners = [players[n]]
                _best_player = players[n]
            elif players[n].score < _best_player.score:
                continue
            else:
                _reverse_range = list(range(5))
                _reverse_range.reverse()
                for c in _reverse_range:
                    if players[n].cards.best_five[c].kind > _best_player.cards.best_five[c].kind:
                        _winners = [players[n]]
                        _best_player = players[n]
                        break
                    elif players[n].cards.best_five[c].kind < _best_player.cards.best_five[c].kind:
                        break
                    else:
                        # Here add suitRule
                        # If last card (c==0) is still equal there is more than a winner
                        if c == 0:
                            _winners.append(players[n])
                            break
        return _winners
