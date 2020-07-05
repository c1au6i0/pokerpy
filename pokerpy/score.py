from pokerpy.consts import *


class Referee:

    @classmethod
    def initialize(cls, kind_of_deck=AMERICAN_DECK):
        """ choose between american/italian deck"""
        ScoreRules.initialize(kind_of_deck)
        ScoreIndex.initialize(kind_of_deck)

    @classmethod
    def winners(cls, players):
        _winners = [players[0]]
        _best = players[0]
        for n in range(1, len(players)):
            # TO DO: Royal flush hearts vs. min Straight Flush spades
            if players[n].score > _best.score:
                _winners = [players[n]]
                _best = players[n]
            elif players[n].score < _best.score:
                continue
            else:
                if ScoreRules.suit_priority_in_flush:
                    if _best.score == ScoreIndex.Flush or _best.score == ScoreIndex.StraightFlush or _best.score == ScoreIndex.RoyalFlush:
                        if players[n].cards.best_five[4].kind > _best.cards.best_five[4].kind:
                            _winners = [players[n]]
                            _best = players[n]
                        elif players[n].score < _best.score:
                            continue
                _reverse_range = list(range(5))
                _reverse_range.reverse()
                for c in _reverse_range:
                    if players[n].cards.best_five[c].kind > _best.cards.best_five[c].kind:
                        _winners = [players[n]]
                        _best = players[n]
                        break
                    elif players[n].cards.best_five[c].kind < _best.cards.best_five[c].kind:
                        break
                    else:
                        if c == 0:
                            if ScoreRules.consider_suit:
                                for s in _reverse_range:
                                    if players[n].cards.best_five[s].suit > _best.cards.best_five[s].suit:
                                        _winners = [players[n]]
                                        _best = players[n]
                                        break
                                    elif players[n].cards.best_five[s].suit < _best.cards.best_five[s].suit:
                                        break
                            else:
                                # If last card (c==0) is still equal there is more than a winner
                                _winners.append(players[n])
                            break
        return _winners


    @classmethod
    def print_winners(cls, players):
        _winnerNames = ''
        _winners = cls.winners(players)
        _number_of_winners = len(_winners)
        for p in range(_number_of_winners):
            _winnerNames = _winnerNames + _winners[p].name + ' '
            if p < _number_of_winners - 1:
                _winnerNames = _winnerNames + 'and '
        if _number_of_winners == 1:
            print('{}{}'.format(_winnerNames, 'wins'))
        else:
            print('{}{}'.format(_winnerNames, 'win'))


class ScoreRules:

    consider_suit: bool
    suit_priority_in_flush: bool
    min_royal_beats_max_royal: bool

    @classmethod
    def initialize(cls, kind_of_deck=AMERICAN_DECK):
        if kind_of_deck == AMERICAN_DECK:
            cls.consider_suit = False
            cls.suit_priority_in_flush = False
            cls.min_royal_beats_max_royal = False
        else:
            cls.consider_suit = True
            cls.suit_priority_in_flush = True
            cls.min_royal_beats_max_royal = True


class ScoreIndex:

    HighCard = 0
    Pair = 1
    TwoPair = 2
    ThreeOfKind = 3
    Straight = 4
    Flush: int
    FullHouse: int
    FourOfKind = 7
    StraightFlush = 8
    RoyalFlush = 9

    @classmethod
    def initialize(cls, kind_of_deck=AMERICAN_DECK):
        cls._set_variabilies(kind_of_deck)
        cls._set_tuple(kind_of_deck)
        # TO DO: just 1 partial?
        cls.partial_straight = PartialStraight()
        cls.partial_flush = PartialFlush()

    @classmethod
    def _set_variabilies(cls, kind_of_deck=AMERICAN_DECK):
        if kind_of_deck == AMERICAN_DECK:
            cls.Flush = 5
            cls.FullHouse = 6
        else:
            cls.FullHouse = 5
            cls.Flush = 6

    @classmethod
    def _set_tuple(cls, kind_of_deck):
        _lowest_scores = ('High card', 'Pair', 'Two pair', 'Three of a kind', 'Straight')
        _highest_scores = ('Four of a kind', 'Straight flush', 'Royal flush')
        if kind_of_deck == AMERICAN_DECK:
            cls.rank = _lowest_scores + ('Flush', 'Full house')
        else:
            cls.rank = _lowest_scores + ('Full house', 'Flush')
        cls.rank = cls.rank + _highest_scores


class PartialStraight:

    @property
    def Nothing(self):
        return 0

    @property
    def InsideStraightDraw(self):
        return 1

    @property
    def OutsideStraightDraw(self):
        return 2


class PartialFlush:

    @property
    def Nothing(self):
        return 0

    @property
    def FlushDraw(self):
        return 1

    @property
    def InsideRoyalFlush(self):
        return 2

    @property
    def OutsideRoyalFlush(self):
        return 3

