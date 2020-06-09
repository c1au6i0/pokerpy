# Temporary class and methods to help test, debug, etc.
# erase it at the end of the Project
# import array as arr
from pokerpy.Converters import CardRankConverter
from pokerpy.Players import Human
from pokerpy.Referee import MatchCounter
from pokerpy.ManyCards import *


def tEST1():
    # create the deck and shuffle it
    print('- - - START TEST - - -')
    conv = CardRankConverter(7)
    Players = [Human("Dave"), Human("Claude")]
    deck = Deck(conv)
    deck.shuffle()
    referee = MatchCounter(conv)
    Players[0].readMatchInfo(conv)
    Players[1].readMatchInfo(conv)
    # create the players cards obj
    Players[0].takeCards(deck.giveCards(5))
    Players[1].takeCards(deck.giveCards(5))
    # print('Deck')
    # deck.showOnConsole()
    # print('Cuori rimanenti: {}'.format(deck.remainingSuit(3)))
    # print('Assi rimanenti: {}'.format(deck.remainingKind(7)))
    # print()
    print(Players[0].name)
    Players[0].playerCards.showOnConsole()
    print(referee.scoreTester(Players[0].playerCards))
    print()
    print(Players[1].name)
    Players[1].playerCards.showOnConsole()
    print(referee.playerScore(Players[1]))
