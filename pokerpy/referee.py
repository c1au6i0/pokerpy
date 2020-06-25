from pokerpy.players import Player


class Evaluator:

    def winner(self, *player):
        #player.index(0)
        pass

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
