from pokerpy.cards_many import *
from pokerpy.converters import *
from pokerpy.money import Cash


class Player:

    # conv is the same for every Player
    # you can do the same with Rules and other stuff
    # useless?
    conv: CardConverter

    def __init__(self, name: str):
        self.name = name
        self.cards = PlayerCards()
        self._deck = Cardlist()
        # possibleMoves: collection
        # roleInHand: type
        self.bankroll: Cash = None
        self.seat: int = None

    def __str__(self):
        return self.name

    def takeCards(self, cardsList: Cardlist):
        self.cards.extend(cardsList)
        for _card in cardsList:
            self._deck.remove(_card)

    def importDeck(self, deck: Cardlist):
        self._deck = Cardlist()
        self._deck.extend(deck)
        self._deck.sort()

    @property
    def score(self):
        return self.cards.score

    @property
    def highestCard(self):
        return self.cards.bestCards[4]

    def slowdown(self):
        self.cards.calculateScore()
        print('{}{} {}'.format(self.name, "'s score is", self.cards.scoreName))
        print(' from: {}'.format(self.cards))
        print()


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
