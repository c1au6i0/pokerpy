# Temporary class and methods to help test, debug, etc.
# erase it at the end of the Project
import pokerpy.ManyCards as m
import pokerpy.Referee as r
from pokerpy.Converters import RankConverter


def tEST1():
    # create the deck and shuffle it
    conv = RankConverter(7)
    deck = m.Deck(conv)
    deck.shuffle()
    referee = r.MatchCounter(conv)
    # create the players cards obj
    player1 = m.PlayerCards(conv)
    player2 = m.PlayerCards(conv)
    # the players take 5 cards from the deck and show 'em
    player1.takeCards(deck.giveCards(5))
    player2.takeCards(deck.giveCards(7))
    print('Deck')
    deck.showOnConsole()
    print('Cuori rimanenti: {}'.format(deck.remainingSuit(3)))
    print('Assi rimanenti: {}'.format(deck.remainingKind(7)))
    print()
    print('Player 1')
    player1.showOnConsole()
    print(referee.pointChecker(player1))
    print()
    print('Player 2')
    player2.showOnConsole()
    print(referee.pointChecker(player2))
