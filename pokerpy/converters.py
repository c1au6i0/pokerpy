class CardConverter:

    suit = (chr(9824), chr(9827), chr(9830), chr(9829))
    kind = []

    # why don't you use a __new__stetement?
    def __init__(self, lowest_kind=2):
        self.kind = [str(k) for k in range(lowest_kind, 11)]
        self.kind.extend(('J', 'Q', 'K', 'A'))
        self.kind = tuple(self.kind)

    def __len__(self):
        return len(self.kind)

    @property
    def ace_rank(self):
        return len(self.kind) - 1


# move to ScoreRules?
class ScoreConverter:

    # almostScore=(puntoIntermedio,scalaAdIncastro,scalaBilaterale,4/5 colore,4/5 ScalaReale,4/5 ScalaReale bilaterale)

    _Flush: int
    _FullHouse: int

    def __init__(self, lowest_kind=2):
        _lowest_scores = ('High card', 'Pair', 'Two pair', 'Three of a kind', 'Straight')
        _highest_scores = ('Four of a kind', 'Straight flush', 'Royal flush')
        if lowest_kind == 2:
            ScoreConverter._Flush = 5
            ScoreConverter._FullHouse = 6
            ScoreConverter.rank = _lowest_scores + ('Flush', 'Full house')
        else:
            ScoreConverter._FullHouse = 5
            ScoreConverter._Flush = 6
            ScoreConverter.rank = _lowest_scores + ('Full house', 'Flush')
        ScoreConverter.rank = ScoreConverter.rank + _highest_scores
        self.partial_straight = PartialStraight()
        self.partial_flush = PartialFlush()

    @property
    def HighCard(self):
        return 0

    @property
    def Pair(self):
        return 1

    @property
    def TwoPair(self):
        return 2

    @property
    def ThreeOfKind(self):
        return 3

    @property
    def Straight(self):
        return 4

    @property
    def Flush(self):
        return ScoreConverter._Flush

    @property
    def FullHouse(self):
        return ScoreConverter._FullHouse

    @property
    def FourOfKind(self):
        return 7

    @property
    def StraightFlush(self):
        return 8

    @property
    def RoyalFlush(self):
        return 9


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

