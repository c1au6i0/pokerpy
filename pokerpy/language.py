

# WIP
class Translator:

    def __init__(self, _language=''):
        self._language = _language

    def _highest_kind_list(self, language: str):
        if language == '':
            _highest_cards = ('J', 'Q', 'K', 'A')
        elif language == 'eng':
            _highest_cards = ('Jack', 'Queen', 'King', 'Ace')
        elif language == 'ita':
            _highest_cards = ('Jack', 'Donna', 'Cappa', 'Asso')
        return _highest_cards

    def _suit_list(self, language: str):
        if language == '':
            return chr(9824), chr(9827), chr(9830), chr(9829)
        elif language == 'eng':
            return 'Spades', 'Clubs', 'Diamonds', 'Hearts'
        elif language == 'ita':
            return 'Picche', 'Fiori', 'Quadri', 'Cuori'
