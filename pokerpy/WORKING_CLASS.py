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
    Players = [Human("Dave"), Human("Claude")]
    for _player in Players:
        _player.importDeck(deck)
    #referee = Evaluator(conv)
    # create the players cards obj
    sharedCards = Cardlist()
    sharedCards.extend(deck.give(3))
    Players[0].takeCards(deck.give(5))
    Players[1].takeCards(deck.give(5))
    Players[0].takeCards(sharedCards)
    Players[1].takeCards(sharedCards)
    Players[0].cards.calculateScore()
    Players[1].cards.calculateScore()
    print(Players[0].name, "'s score is", Players[0].cards.scoreName)
    print(Players[0].cards)
    #
    print()
    print(Players[1].name, "'s score is", Players[1].cards.scoreName)
    Players[1].cards.sort()
    print(Players[1].cards)
    print()
    #print(referee.headToheadWinner(Players[0], Players[1]))
