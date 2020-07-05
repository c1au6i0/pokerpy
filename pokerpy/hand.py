from pokerpy.consts import *


class HandRules:

    # the minOpen list is correct: 0 for Texas hold 'em, 1, 2 or 3 for Draw game (4 is always valid)
    _min_open: ('None', 'JJ', 'QQ', 'KK', '4/5 Outside Straight Flush')

    # don't do it static: italian + telesina = 2 instance
    # erase min and max players?

    def __init__(self):
        self._tradable_cards = 4
        self._shared_faced_down_cards = 0
        self._shared_faced_up_cards = 0
        self._shared_sequence = tuple()
        self._player_faced_down_cards = 5
        self._player_faced_up_cards = 0
        self._min_opening_index = 1

    # how many cards can trade a player? (default = 4 in draw game)
    @property
    def tradable_cards(self):
        return self._tradable_cards

    @tradable_cards.setter
    def tradable_cards(self, value):
        self._tradable_cards = value

    # for no-draw games
    # 5 in starting phase of Texas hold 'em
    @property
    def shared_faced_down_cards(self):
        return self._shared_faced_down_cards

    @shared_faced_down_cards.setter
    def shared_faced_down_cards(self, value):
        self._shared_faced_down_cards = value

    # 5 in ending phase of Texas hold 'em
    @property
    def shared_faced_up_cards(self):
        return self._shared_faced_up_cards

    @shared_faced_up_cards.setter
    def shared_faced_up_cards(self, value):
        self._shared_faced_up_cards = value

    @property
    def shared_cards(self):
        return self._shared_faced_down_cards + self._shared_faced_up_cards

    @property
    def player_faced_down_cards(self):
        return self._player_faced_down_cards

    @player_faced_down_cards.setter
    def player_faced_down_cards(self, value):
        self._player_faced_down_cards = value

    @property
    def player_faced_up_cards(self):
        return self._player_faced_up_cards

    @player_faced_up_cards.setter
    def player_faced_up_cards(self, value):
        self._player_faced_up_cards = value

    @property
    def player_cards(self):
        return self._player_faced_down_cards + self._player_faced_up_cards
