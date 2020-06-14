class CardRankConverter:

    suit = chr(9824), chr(9827), chr(9830), chr(9829)
    _lowestScores = ('High card', 'Pair', 'Two pair', 'Three of a kind', 'Straight')
    _highestScores = ('Four of a kind', 'Straight flush', 'Royal flush')

    # why don't you use a __new__stetement?
    def __init__(self, lowestKind=2, kindLanguage='', suitLanguage=''):
        self.kind = [str(k) for k in range(lowestKind, 11)]
        self.kind.extend(('J', 'Q', 'K', 'A'))
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
    pass


# CardRankConverterWithTranslator have to substite CardRankConverter. In alternative add translator
class CardRankConverterWithTranslator:
    def __init__(self, lowestKindInt=2, kindLanguage='', suitLanguage=''):
        self.kind = self.__lowestKindList(lowestKindInt) + self.__highestKindList(kindLanguage)
        self.suit = self.__suitList(suitLanguage)

    def __len__(self):
        return len(self.kind)

    def __lowestKindList(self, lowestKind: int):
        _lowestCard = [str(k) for k in range(lowestKind, 11)]
        return tuple(_lowestCard)

    def __highestKindList(self, language: str):
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