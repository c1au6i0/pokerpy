from abc import ABC
import pandas as pd


class SetOfCards:
    """This is a group of cards
        PlayerCards, Deck and Flop are SetOfCards"""
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


class Deck(SetOfCards, pd.DataFrame, ABC):
    """Deck is Deck"""
    # def __init__(self):
    # giveCards()
    # shuffle()
    # create(numberOfPlayers, gameRules)
    pass


class OrderRules:
    # random
    # insert
    # primaGliScarti
    # Sort()
    pass


