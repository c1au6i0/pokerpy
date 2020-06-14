# Temporary class and methods to help test, debug, etc.
# erase it at the end of the Project
# import array as arr
from pokerpy.Converters import CardRankConverter
from pokerpy.Players import Human
from pokerpy.Referee import Evaluator
from pokerpy.ManyCards import *


def tEST1():
    # create the deck and shuffle it
    print()
    print('- - - TERESA TEST - - -')
    conv = CardRankConverter(7)
    Players = [Human("Dave"), Human("Claude")]
    deck = Deck(conv)
    deck.shuffle()
    referee = Evaluator(conv)
    Players[0].startHand(conv)
    Players[1].startHand(conv)
    # create the players cards obj
    commonCards = SetOfCards(conv)
    commonCards.takeCards(deck.giveCards(3))
    Players[0].takeCards(deck.giveCards(5))
    Players[1].takeCards(deck.giveCards(5))
    Players[0].takeCards(commonCards.cards)
    Players[1].takeCards(commonCards.cards)
    Players[0].playerCards.calculateScore()
    Players[1].playerCards.calculateScore()
    print(Players[0].name, "'s score is", Players[0].playerCards.scoreName)
    Players[0].playerCards.showOnConsole()
    #
    print()
    print(Players[1].name, "'s score is", Players[1].playerCards.scoreName)
    Players[1].playerCards.showOnConsole()
    print()
    print(referee.headToheadWinner(Players[0], Players[1]))
