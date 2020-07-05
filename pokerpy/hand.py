from pokerpy.consts import *


class HandRules:

    # the minOpen list is correct: 0 for Texas hold 'em, 1, 2 or 3 for Draw game (4 is always valid)
    _min_open: ('None', 'JJ', 'QQ', 'KK', '4/5 Outside Straight Flush')

    # don't do it static: italian + telesina = 2 instance
    # erase min and max players?

    def __init__(self, kind_of_game=AMERICAN_DRAW_GAME):
        if kind_of_game == AMERICAN_DRAW_GAME or kind_of_game == ITALIAN_DRAW_GAME:
            self._player_faced_down_cards = 5
            self._player_faced_up_cards = 0
            self._player_sequence = tuple(5)
            self._tradable_cards = 4
            self._shared_faced_down_cards = 0
            self._shared_faced_up_cards = 0
            self._shared_sequence = tuple()
            self._min_opening_index = 1
        elif kind_of_game == TEXAS_HOLD_EM:
            self._tradable_cards = 0
            self._player_faced_down_cards = 2
            self._player_faced_up_cards = 0
            self._player_sequence = tuple(2)
            self._shared_faced_down_cards = 5
            self._shared_faced_up_cards = 0
            self._shared_sequence = tuple(3, 1, 1)
            self._min_opening_index = 0
        elif kind_of_game == TELESINA:
            self._player_faced_down_cards = 1
            self._player_faced_up_cards = 4
            self._player_sequence = tuple(2, 1, 1, 1)
            self._tradable_cards = 0
            self._shared_faced_down_cards = 0
            self._shared_faced_up_cards = 0
            self._shared_sequence = tuple(1, 1, 1)
            self._min_opening_index = 0


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


# TO DO: every step is a CardDistribution?
class CardsDistribution:

    def __init__(self, shared=False, faced_down=5, faced_up=0):
        self.shared = shared
        self.faced_down = faced_down
        self.faced_up = faced_up
