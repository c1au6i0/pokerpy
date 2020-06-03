class RankConverter:
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

