# Temporary class and methods to help test, debug, etc.
# erase it at the end of the Project
# import array as arr
from pokerpy.converters import CardRankConverter
from pokerpy.players import Human
from pokerpy.referee import Evaluator
from pokerpy.cards_many import *
from pokerpy.money import Pot
from pokerpy.card_single import Card


def testPot():
    Players = [Human("Dave"), Human("Claude")]
    pot = Pot()
    pot.addPlayers(Players[0], Players[1])
    pot.showPlayers()
    pot.takeMoney(1000)
    pot.showOnConsole()
    pot.removePlayer(Players[1])
    pot.showPlayers()
    print(pot.giveEverything())
    pot.showOnConsole()


def testTeresa():
    # create the deck and shuffle it
    print()
    print('- - - TERESA TEST - - -')
    deck = Cardlist()
    deck.createDeck(7)
    deck.shuffle()
    deck.remove((0, 0))
    Players = [Human("Dave", deck), Human("Claude", deck)]
    #referee = Evaluator(conv)
    # create the players cards obj
    commonCards = Cardlist()
    commonCards.takeCards(deck.giveMany(3))
    Players[0].takeCards(deck.giveMany(5))
    Players[1].takeCards(deck.giveMany(5))
    Players[0].takeCards(commonCards)
    Players[1].takeCards(commonCards)
    Players[0].playerCards.calculateScore()
    Players[1].playerCards.calculateScore()
    print(Players[0].name, "'s score is", Players[0].playerCards.scoreName)
    print(Players[0].playerCards)
    #
    print()
    print(Players[1].name, "'s score is", Players[1].playerCards.scoreName)
    print(Players[1].playerCards)
    print()
    #print(referee.headToheadWinner(Players[0], Players[1]))
