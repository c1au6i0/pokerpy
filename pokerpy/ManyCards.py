import pandas as pd
from pokerpy.SingleCard import Card


class SetOfCards:
    """This is a group of cards
        PlayerCards, Deck and Flop are SetOfCards"""
    def __init__(self):
        print('starting init')
        # create the list of cards, that is empty
        self.cards = []
        # try append
        # self.cards.append(Card(4, 1))
        # self.cards.append(Card(2, 3))
        print('ending init')

    def showOnConsole(self):
        if self.cards == []:
            print('There is no card in this group')
        else:
            for card in self.cards:
                print(card.name)
    # numberOfCards: int
    # faceDownCards: int(?)
    # faceUpCards: int(?)
    # selectedCards: collection(?)
    # giveSelected()
    # change()
    # get()
    # selectCard()
    # show()


class PlayerCards(SetOfCards):
    """look at the class name, it's not so hard"""
    # numberPoint
    # selectBestCollections
    # sort()
    # change()
    # show()
    # typePoint()


# class Deck(SetOfCards, pd.DataFrame):
# I remove DataFrame due to problems with import abc
class Deck(SetOfCards):
    """Deck is Deck"""
    # This is the constructor
    def __init__(self):
        super().__init__()
        # fulfill the cards list
        for n in range(13):
            for s in range(4):
                self.cards.append(Card(n, s))
        # create the rejects list (empty at start)
        rejects = []
    # giveCards()
    # shuffle()
    # create(numberOfPlayers, gameRules)


class OrderRules:
    # random
    # insert
    # primaGliScarti
    # Sort()
    pass


