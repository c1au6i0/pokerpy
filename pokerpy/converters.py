# move to ScoreRules?
class CardRankConverter:

    suit = (chr(9824), chr(9827), chr(9830), chr(9829))
    _lowestScores = ('High card', 'Pair', 'Two pair', 'Three of a kind', 'Straight')
    _highestScores = ('Four of a kind', 'Straight flush', 'Royal flush')
    kind = []
    score = ()

    # why don't you use a __new__stetement?
    def __init__(self, lowestKind=2, kindLanguage='', suitLanguage=''):
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


# WIP
class Translator:

    def __init__(self, kindLanguage='', suitLanguage=''):
        self._kindLanguage = kindLanguage

    def __highestKindList(language: str):
        if language == '':
            _highestCards = ('J', 'Q', 'K', 'A')
        elif language == 'eng':
            _highestCards = ('Jack', 'Queen', 'King', 'Ace')
        elif language == 'ita':
            _highestCards = ('Jack', 'Donna', 'Cappa', 'Asso')
        return _highestCards

    def __suitList(self, language: str):
        if language == '':
            return chr(9824), chr(9827), chr(9830), chr(9829)
        elif language == 'eng':
            return 'Spades', 'Clubs', 'Diamonds', 'Hearts'
        elif language == 'ita':
            return 'Picche', 'Fiori', 'Quadri', 'Cuori'