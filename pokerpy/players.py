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
        self._deck = ListOfCards()
        # possibleMoves: collection
        # roleInHand: type
        self.bankroll: Cash = None
        self.seat: int = None

    def __str__(self):
        return self.name

    def take_cards(self, list_of_cards: ListOfCards):
        self.cards.extend(list_of_cards)
        for _card in list_of_cards:
            self._deck.remove(_card)

    def import_deck(self, deck: ListOfCards):
        self._deck = ListOfCards()
        self._deck.extend(deck)
        self._deck.sort()

    @property
    def score(self):
        return self.cards.score

    @property
    def highest_card(self):
        return self.cards.best_five[4]

    def showdown(self):
        self.cards.calculate_score()
        print('{}{} {}'.format(self.name, "'s score is", self.cards.score_name))
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
