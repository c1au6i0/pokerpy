from pokerpy.ManyCards import *
from pokerpy.Converters import *
from pokerpy.Money import Cash


class Player:

    def __init__(self, name: str):
        self.name = name
        self.playerCards: PlayerCards
        self._deck: Deck
        self._conv: CardRankConverter
        # possibleMoves: collection
        # roleInHand: type
        self.bankroll: Cash
        self.seat: int

    def readMatchInfo(self, conv: CardRankConverter):
        # add role
        self._conv = conv

    def takeCards(self, cardsList: list):
        self._deck = Deck(self._conv)
        self.playerCards = PlayerCards(self._conv)
        self.playerCards.takeCards(cardsList)
        for _card in cardsList:
            self._deck.cards.remove(_card)


class Talker:
    # check()
    # call()
    # rise()
    # fold()
    # checkRise()
    # blind()
    # bigBlind()
    pass


class Human(Player):
    # orderRules
    pass


class Cyborg(Player):
    # speed
    # AI
    # maybe the next line is for another class
    # potentialGoodCards
    pass
