# Temporary class and methods to help test, debug, etc.
# erase it at the end of the Project
# import array as arr
from pokerpy.converters import CardConverter
from pokerpy.players import *
from pokerpy.referee import *
from pokerpy.cards_many import *
from pokerpy.money import Pot
from pokerpy.dealer import Croupier


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
    print()
    croupier = Croupier(lowestKind=7, numShared=3)
    Players = [Human("Dave"), Human("Claude")]
    croupier.addPlayers(Players[0], Players[1])
    croupier.startDeck()
    croupier.giveStartingCards()
    print('Shared cards:', croupier.sharedCards)
    print()
    croupier.showSharedCards(3)
    for _player in Players:
        _player.slowdown()
    _winner = Evaluator.headToheadWinner(Players[0], Players[1])
    _winnerNames = ''
    for _player in _winner:
        _winnerNames = _winnerNames + _player.name + ' '
    print('{}{}'.format(_winnerNames, 'wins'))

