# Temporary class and methods to help test, debug, etc.
# erase it at the end of the Project
import pokerpy.ManyCards as m
import pokerpy.Referee as r
from pokerpy.Converter import kindSymbol


def tEST1():
    # create the deck and shuffle it
    deck = m.Deck(7)
    deck.shuffle()
    # create the player cards obj
    player = m.PlayerCards()
    # the player take 5 cards from the deck and show 'em
    player.takeCards(deck.giveCards(5))
    player.showOnConsole()
    referee = r.MatchCounter()
    print(referee.pointChecker(player))
    print('Cuori rimanenti: {}'.format(deck.remainingSuit(3)))
    print(kindSymbol[-1])
    print('7 rimanenti: {}'.format(deck.remainingKind(5)))
