

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
