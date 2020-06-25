from pokerpy.consts import *


class Score:

    # almostScore=(puntoIntermedio,scalaAdIncastro,scalaBilaterale,4/5 colore,4/5 ScalaReale,4/5 ScalaReale bilaterale)

    @classmethod
    def set_rules(cls, kind_of_deck=AMERICAN_DECK):
        cls._set_variabilies(kind_of_deck)
        cls._set_tuple(kind_of_deck)
        cls.partial_straight = PartialStraight()
        cls.partial_flush = PartialFlush()

    @classmethod
    def _set_variabilies(cls, kind_of_deck=AMERICAN_DECK):
        cls.HighCard = 0
        cls.Pair = 1
        cls.TwoPair = 2
        cls.ThreeOfKind = 3
        cls.Straight = 4
        if kind_of_deck == AMERICAN_DECK:
            cls.Flush = 5
            cls.FullHouse = 6
        else:
            cls.FullHouse = 5
            cls.Flush = 6
        cls.FourOfKind = 7
        cls.StraightFlush = 8
        cls.RoyalFlush = 9

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

