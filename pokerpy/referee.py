from pokerpy.players import Player
from pokerpy.cards_many import *
from pokerpy.rules import *


class Evaluator:

    # TO DO
    @classmethod
    def winners(cls, *player):
        # _best_score = player[0].score
        # _best_cards = player[0].cards.best_five
        _best_player = player[0]
        _winners = [_best_player]
        for n in range(1, len(player)-1):
            if player[n].score > _best_player.score:
                _winners.clear()
                _winners.append(player[n])
            elif player[n].score < _best_player.score:
                continue
            else:
                _reverse_range = list(range(5))
                _reverse_range.reverse()
                for c in _reverse_range:
                    if player[n].cards.best_five[c].kind > _best_player.cards.best_five[c].kind:
                        _winners.clear()
                        _winners.append(player[n])
                        break
                    elif player[n].cards.best_five[c].kind < _best_player.cards.best_five[c].kind:
                        break
                    else:
                        # Here add suitRule
                        if n == 0:
                            _winners.append(player[n])
                            break
        return _winners

    @classmethod
    def initialize(cls, kind_of_deck=AMERICAN_DECK):
        ScoreRules.initialize(kind_of_deck)

    @classmethod
    def head_to_head_winner(cls, player1: Player, player2: Player):
        _list = []
        if player1.score > player2.score:
            _list.append(player1)
            return _list
        elif player1.score < player2.score:
            _list.append(player2)
            return _list
        else:
            _reverse_range = list(range(5))
            _reverse_range.reverse()
            for n in _reverse_range:
                if player1.cards.best_five[n].kind > player2.cards.best_five[n].kind:
                    _list.append(player1)
                    break
                elif player1.cards.best_five[n].kind < player2.cards.best_five[n].kind:
                    _list.append(player2)
                    break
                else:
                    # Here add suitRule
                    if n == 0:
                        _list.append(player1)
                        _list.append(player2)
                        break
        return _list