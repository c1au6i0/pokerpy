class HandRules:

    # don't do it static: italian + telesina = 2 instance

    def __init__(self):
        self._min_players = 2
        self._max_players = 6
        self._tradable_cards = 4
        self._shared_faced_down_cards = 0
        self._shared_faced_up_cards = 0
        self._player_faced_down_cards = 5
        self._player_faced_up_cards = 0
        # the minOpen list is correct: 0 for Texas hold 'em, 1, 2 or 3 for Draw game (4 is always valid)
        # minOpen: (None, JJ, QQ, KK, 4/5 Royal straight)

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
    def board_cards(self):
        return self.faced_down_cards # self.faced_up_cards

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
    def board_cards(self):
        return self._shared_faced_down_cards + self._shared_faced_up_cards

    # just the minimum number of players
    # draw game = 3, texas and others = 2
    @property
    def min_players(self):
        return self._min_players

    @min_players.setter
    def min_players(self, value):
        self._min_players = value

    # just the maximum number of players
    # draw game = 6, texas and others = 10 ?
    @property
    def max_players(self):
        return self._max_players

    @max_players.setter
    def maxPlayers(self, value):
        self.max_players = value


class ScoreRules:

    # name?

    def __init__(self):
        # default values (American Draw Game)
        self._lowest_card = 2
        self._ignore_suit = True
        self._min_royal_beats_max_royal = False
        self._suit_priority_in_flush = False
        # Why property and not just variables?

    # the lowest number of a card in the deck
    # from 5 to 9 in italian draw game, 2 in american game
    @property
    def lowest_card(self):
        return self._lowest_card

    @lowest_card.setter
    def lowest_card(self, value):
        self._lowest_card = value

    # number_of_cards_for_suit * 4 = number of cards in the deck
    @property
    def number_of_cards_for_suit(self):
        return 15 - self._lowest_card

    @property
    def ignore_suit(self):
        return self._ignore_suit

    @ignore_suit.setter
    def ignore_suit(self, value):
        self._ignore_suit = value

    @property
    def suit_priority_in_flush(self):
        return self._suit_priority_in_flush

    @suit_priority_in_flush.setter
    def suit_priority_in_flush(self, value):
        self._suit_priority_in_flush = value

    @property
    def min_royal_beats_max_royal(self):
        return self._min_royal_beats_max_royal

    @min_royal_beats_max_royal.setter
    def min_royal_beats_max_royal(self, value):
        self._min_royal_beats_max_royal = value

    # fullVsFlush: bool (useless?)


class MoneyRules:
        # minBet:
        # maxBet: minBet * n
        # maxRise:
        # richiestaPoste
        # dealerBet
        # incrementType
        # incrementTime
        # modalitaIncremento=(nullo,a tempo,giri,eliminazioneGiocatore)
        # setBlind: [notAllowed, due, allowed]
        # small  blind, big blind, over
        # minBetType: [check, blind]
        # resti / no limits
        # obbligo di prendere posta
        # allowLowerBets
        pass