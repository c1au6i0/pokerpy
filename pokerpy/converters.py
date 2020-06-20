# move to ScoreRules?
class CardRankConverter:

    suit = (chr(9824), chr(9827), chr(9830), chr(9829))
    _lowestScores = ('High card', 'Pair', 'Two pair', 'Three of a kind', 'Straight')
    _highestScores = ('Four of a kind', 'Straight flush', 'Royal flush')
    kind = []
    score = ()

    # why don't you use a __new__stetement?
    def __init__(self, lowestKind=2):
        self.kind = [str(k) for k in range(lowestKind, 11)]
        self.kind.extend(('J', 'Q', 'K', 'A'))
        self.kind = tuple(self.kind)
        if lowestKind == 2:
            self.score = self._lowestScores + ('Flush', 'Full house')
        else:
            self.score = self._lowestScores + ('Full house', 'Flush')
        self.score = self.score + self._highestScores

    def __len__(self):
        return len(self.kind)

    @property
    def aceRank(self):
        return len(self.kind) - 1

    # almostScore=(puntoIntermedio,scalaAdIncastro,scalaBilaterale,4/5 colore,4/5 ScalaReale,4/5 ScalaReale bilaterale)


class Score:

    _Flush: int
    _FullHouse: int

    def __init__(self, lowestKind=2):
        if lowestKind == 2:
            Score._Flush = 5
            Score._FullHouse = 6
        else:
            Score._FullHouse = 5
            Score._Flush = 6

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
        return Score._Flush

    @property
    def FullHouse(self):
        return Score._FullHouse

    @property
    def FourKind(self):
        return 7

    @property
    def RoyalFlush(self):
        return 8

