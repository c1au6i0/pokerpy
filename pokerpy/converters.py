class CardConverter:

    suit = (chr(9824), chr(9827), chr(9830), chr(9829))
    kind = []

    # why don't you use a __new__stetement?
    def __init__(self, lowestKind=2):
        self.kind = [str(k) for k in range(lowestKind, 11)]
        self.kind.extend(('J', 'Q', 'K', 'A'))
        self.kind = tuple(self.kind)

    def __len__(self):
        return len(self.kind)

    @property
    def aceRank(self):
        return len(self.kind) - 1


# move to ScoreRules?
class ScoreConverter:

    # almostScore=(puntoIntermedio,scalaAdIncastro,scalaBilaterale,4/5 colore,4/5 ScalaReale,4/5 ScalaReale bilaterale)

    _Flush: int
    _FullHouse: int

    def __init__(self, lowestKind=2):
        _lowestScores = ('High card', 'Pair', 'Two pair', 'Three of a kind', 'Straight')
        _highestScores = ('Four of a kind', 'Straight flush', 'Royal flush')
        if lowestKind == 2:
            ScoreConverter._Flush = 5
            ScoreConverter._FullHouse = 6
            ScoreConverter.rank = _lowestScores + ('Flush', 'Full house')
        else:
            ScoreConverter._FullHouse = 5
            ScoreConverter._Flush = 6
            ScoreConverter.rank = _lowestScores + ('Full house', 'Flush')
        ScoreConverter.rank = ScoreConverter.rank + _highestScores

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
    def ThreeKind(self):
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
    def FourKind(self):
        return 7

    @property
    def StraightFlush(self):
        return 8

    @property
    def RoyalFlush(self):
        return 9

