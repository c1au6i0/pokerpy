class GameRules:

    def __init__(self):
        # default options is for American Draw Game
        self._lowestCard = 2
        self._tradableCards = 4
        self._minPlayers = 3
        self._maxPlayers = 6
        self._facedDownCards = 0
        self._facedUpCards = 0
        self._playerFacedDownCards = 5
        self._playerFacedUpCards = 0

    # the lowest number of a card in the deck
    # generally from 5 to 8 in italian draw game
    # 2 in american game
    @property
    def lowest_card(self):
        return self._lowestCard

    @lowest_card.setter
    def lowest_card(self, value):
        self._lowestCard = value

    # number_of_cards_for_suit * 4 = number of cards in the deck
    @property
    def number_of_cards_for_suit(self):
        return 15 - self._lowestCard

    # how many cards can trade a player? (default = 4 in draw game)
    @property
    def tradable_cards(self):
        return self._tradableCards

    @tradable_cards.setter
    def tradable_cards(self, value):
        self._tradableCards = value

    # for no-draw games
    # 5 in starting phase of Texas hold 'em
    @property
    def faced_down_cards(self):
        return self._facedDownCards

    @faced_down_cards.setter
    def faced_down_cards(self, value):
        self._facedDownCards = value

    # 5 in ending phase of Texas hold 'em
    @property
    def faced_up_cards(self):
        return self._facedUpCards

    @faced_up_cards.setter
    def faced_up_cards(self, value):
        self._facedUpCards = value

    @property
    def board_cards(self):
        return self._facedDownCards + self._facedUpCards

    @property
    def player_faced_down_cards(self):
        return self._playerFacedDownCards

    @player_faced_down_cards.setter
    def player_faced_down_cards(self, value):
        self._playerFacedDownCards = value

    @property
    def player_faced_up_cards(self):
        return self._playerFacedUpCards

    @player_faced_up_cards.setter
    def player_faced_up_cards(self, value):
        self._playerFacedUpCards = value

    @property
    def board_cards(self):
        return self._facedDownCards + self._facedUpCards

    # just the minimum number of players
    # draw game = 3, texas and others = 2
    @property
    def min_players(self):
        return self._minPlayers

    @min_players.setter
    def min_players(self, value):
        self._minPlayers = value

    # just the maximum number of players
    # draw game = 6, texas and others = 10 ?
    @property
    def max_players(self):
        return self._maxPlayers

    @max_players.setter
    def max_players(self, value):
        self._maxPlayers = value
