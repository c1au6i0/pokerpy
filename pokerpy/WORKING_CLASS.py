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
    pot.add_players(Players[0], Players[1])
    pot.showPlayers()
    pot.take_money(1000)
    pot.show_on_console()
    pot.removePlayer(Players[1])
    pot.showPlayers()
    print(pot.giveEverything())
    pot.show_on_console()


def testTeresa():
    # create the deck and shuffle it
    print()
    print('- - - TERESA TEST - - -')
    print()
    croupier = Croupier(lowest_kind=7, number_cards_shared=3)
    Players = [Human("Dave"), Human("Claude")]
    croupier.add_players(Players[0], Players[1])
    croupier.start_deck()
    croupier.give_starting_cards()
    print('Shared cards:', croupier.shared_cards)
    print()
    croupier.show_shared_cards(3)
    for _player in Players:
        _player.showdown()
    _winner = Evaluator.head_to_head_winner(Players[0], Players[1])
    _winnerNames = ''
    for _player in _winner:
        _winnerNames = _winnerNames + _player.name + ' '
    print('{}{}'.format(_winnerNames, 'wins'))

