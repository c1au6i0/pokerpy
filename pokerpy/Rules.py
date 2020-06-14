class HandRules:

    def __init__(self):
        self.activePlayers = []
        self._minPlayers = 3
        self._maxPlayers = 6
        # the minOpen list is correct: 0 for Texas hold 'em, 1, 2 or 3 for Draw game (4 is always valid)
        # minOpen: (None, JJ, QQ, KK, 4/5 Royal straight)


# move to CommonCards: SetOfCards?
class CardsRules:

    def __init__(self):
        self._tradableCards = 4
        self._facedDownCards = 0
        self._facedUpCards = 0
        self._playerFacedDownCards = 5
        self._playerFacedUpCards = 0

    # how many cards can trade a player? (default = 4 in draw game)
    @property
    def tradableCards(self):
        return self._tradableCards

    @tradableCards.setter
    def tradableCards(self, value):
        self._tradableCards = value

    # for no-draw games
    # 5 in starting phase of Texas hold 'em
    @property
    def facedDownCards(self):
        return self.FacedDownCards

    @facedDownCards.setter
    def facedDownCards(self, value):
        self.facedDownCards = value

    # 5 in ending phase of Texas hold 'em
    @property
    def facedUpCards(self):
        return self.facedUpCards

    @facedUpCards.setter
    def facedUpCards(self, value):
        self.facedUpCards = value

    @property
    def boardCards(self):
        return self.facedDownCards # self.FacedUpCards

    @property
    def playerFacedDownCards(self):
        return self._playerFacedDownCards

    @playerFacedDownCards.setter
    def playerFacedDownCards(self, value):
        self._playerFacedDownCards = value

    @property
    def playerFacedUpCards(self):
        return self._playerFacedUpCards

    @playerFacedUpCards.setter
    def playerFacedUpCards(self, value):
        self._playerFacedUpCards = value

    @property
    def boardCards(self):
        return self.FacedDownCards + self.FacedUpCards

    # just the minimum number of players
    # draw game = 3, texas and others = 2
    @property
    def minPlayers(self):
        return self._minPlayers

    @minPlayers.setter
    def minPlayers(self, value):
        self._minPlayers = value

    # just the maximum number of players
    # draw game = 6, texas and others = 10 ?
    @property
    def maxPlayers(self):
        return self._maxPlayers

    @maxPlayers.setter
    def maxPlayers(self, value):
        self._maxPlayers = value


class ScoreRules:

    # name?

    def __init__(self):
        # default values (American Draw Game)
        self._lowestCard = 2
        self._ignoreSuit = True
        self._minRoyalBeatsMaxRoyal = False
        self._suitPriorityInFlush = False
        # Why property and not just variables?

    # the lowest number of a card in the deck
    # generally from 5 to 8 in italian draw game, 2 in american game
    @property
    def lowestCard(self):
        return self._lowestCard

    @lowestCard.setter
    def lowestCard(self, value):
        self._lowestCard = value

    # numberOfCardsForSuit * 4 = number of cards in the deck
    @property
    def numberOfCardsForSuit(self):
        return 15 - self._lowestCard

    @property
    def ignoreSuit(self):
        return self._ignoreSuit

    @ignoreSuit.setter
    def ignoreSuit(self, value):
        self._ignoreSuit = value

    @property
    def suitPriorityInFlush(self):
        return self._suitPriorityInFlush

    @suitPriorityInFlush.setter
    def suitPriorityInFlush(self, value):
        self._suitPriorityInFlush = value

    @property
    def minRoyalBeatsMaxRoyal(self):
        return self._minRoyalBeatsMaxRoyal

    @minRoyalBeatsMaxRoyal.setter
    def minRoyalBeatsMaxRoyal(self, value):
        self._minRoyalBeatsMaxRoyal = value

    # fullVsFlush: bool (useless?)


class MoneyRules:
        # minBet:
        # maxBet: minBet * n
        # maxRise:
        # richiestaPoste
        # dealerBet
        # incrementType
        # incrementTime
        # setBlind: [notAllowed, due, allowed]
        # small  blind, big blind, over
        # minBetType: [check, blind]
        # resti / no limits
        # obbligo di prendere posta
        # allowLowerBets
        pass