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
    print('- - - START TEST - - -')
    conv = CardRankConverter(7)
    Players = [Human("Dave"), Human("Claude")]
    deck = Deck(conv)
    deck.shuffle()
    referee = Evaluator(conv)
    Players[0].readMatchInfo(conv)
    Players[1].readMatchInfo(conv)
    # create the players cards obj
    Players[0].takeCards(deck.giveCards(8))
    Players[0].playerCards.calculateScore()
    Players[1].takeCards(deck.giveCards(9))
    Players[1].playerCards.calculateScore()
    print(Players[0].name, "'s score is", Players[0].playerCards.scoreName)
    Players[0].playerCards.showOnConsole()
    #
    print()
    print(Players[1].name, "'s score is", Players[1].playerCards.scoreName)
    Players[1].playerCards.showOnConsole()
    print()
    print(referee.headToheadWinner(Players[0], Players[1]))
