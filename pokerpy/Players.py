from pokerpy.ManyCards import *
from pokerpy.Converters import *


class Player:
    _playerCards: SetOfCards
    _deck: Deck
    _conv: CardRankConverter
    # possibleMoves: collection
    # roleInHand: type
    bankroll = 0
    seat: int

    def __init__(self, name: str):
        self.name = name

    def readMatchInfo(self, conv: CardRankConverter):
        # add role
        self._conv = conv

    def takeCards(self, cardsList: list):
        self._deck = Deck(self._conv)
        self._playerCards = SetOfCards(self._conv)
        self._playerCards.takeCards(cardsList)
        for _card in cardsList:
            self._deck.cards.remove(_card)


class Talker:
    # check)
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
