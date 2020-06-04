# Temporary class and methods to help test, debug, etc.
# erase it at the end of the Project
import pokerpy.ManyCards as m
import pokerpy.Referee as r
from pokerpy.Converters import RankConverter


def tEST1():
    # create the deck and shuffle it
    conv = RankConverter(7, 'ita')
    deck = m.Deck(conv)
    deck.shuffle()
    # create the player cards obj
    player = m.PlayerCards(conv)
    # the player take 5 cards from the deck and show 'em
    player.takeCards(deck.giveCards(5))
    deck.showOnConsole()
    player.showOnConsole()
    referee = r.MatchCounter(conv)
    print(referee.pointChecker(player))
    print('Cuori rimanenti: {}'.format(deck.remainingSuit(3)))
    print('Assi rimanenti: {}'.format(deck.remainingKind(7)))
