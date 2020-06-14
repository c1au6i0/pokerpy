from pokerpy.ManyCards import *
from pokerpy.Converters import *
from pokerpy.Money import Cash


class Player:

    # conv is the same for every Player, so why don't you use a class attribute?
    # you can do the same with Rules and other stuff
    conv: CardRankConverter

    def __init__(self, name: str):
        self.name = name
        self.playerCards: PlayerCards = None
        self._deck: Deck = None
        self._conv: CardRankConverter = None
        # possibleMoves: collection
        # roleInHand: type
        self.bankroll: Cash = None
        self.seat: int = None

    def __repr__(self):
        return self.name

    def startHand(self, conv: CardRankConverter):
        # add role
        self._conv = conv
        self._deck = Deck(self._conv)
        self.playerCards = PlayerCards(self._conv)

    def takeCards(self, cardsList: list):
        self.playerCards.takeCards(cardsList)
        for _card in cardsList:
            self._deck.cards.remove(_card)

    @property
    def score(self):
        return self.playerCards.score

    @property
    def highestCard(self):
        return self.playerCards.bestCards[4]



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
