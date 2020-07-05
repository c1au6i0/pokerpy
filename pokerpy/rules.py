from pokerpy.consts import *


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
    def max_players(self, value):
        self._max_players = value


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
