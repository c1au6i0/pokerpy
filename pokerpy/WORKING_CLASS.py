from pokerpy.players import *
from pokerpy.score import *
from pokerpy.money import Pot
from pokerpy.dealer import Dealer
from pokerpy.consts import *


def testPot():
    Players = [Human("Dave"), Human("Claude")]
    pot = Pot()
    pot.add_players(Players[0], Players[1])
    pot.show_players()
    pot.take_money(1000)
    pot.show_on_console()
    pot.remove_player(Players[1])
    pot.show_players()
    print(pot.give_everything())
    pot.show_on_console()


def testTeresa():
    # create the deck and shuffle it
    print()
    print('- - - TERESA TEST - - -')
    print()
    Dealer.set_rules(kind_of_deck=ITALIAN_DECK, number_cards_shared=3)
    Players = [Human("Dave"), Human("Claude"), Human("Bill"), Human("Jack")]
    # TO DO: change next method to accept a list?
    Dealer.add_players(Players[0], Players[1], Players[2], Players[3])
    Dealer.start_hand()
    print('Shared cards:', Dealer.shared_cards)
    print()
    Dealer.face_up_shared_cards(3)
    for _player in Players:
        _player.showdown()
    Referee.initialize(ITALIAN_DECK)
    _winner = Referee.winners(Players)
    _winnerNames = ''
    _number_of_winners = len(_winner)
    for p in range(_number_of_winners):
        _winnerNames = _winnerNames + _winner[p].name + ' '
        if p < _number_of_winners-1:
            _winnerNames = _winnerNames + 'and '
    if _number_of_winners == 1:
        print('{}{}'.format(_winnerNames, 'wins'))
    else:
        print('{}{}'.format(_winnerNames, 'win'))

