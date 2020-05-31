# Temporary class and methods to help test, debug, etc.
# erase it at the end of the Project
import pokerpy.ManyCards as m


def tEST1():
    d1 = m.Deck(10)
    d2 = m.Deck(10)
    d2.takeCards(d1.giveCards(5))
    # d2.takeCards(d1.giveSingleCard(5))
    # print(d.giveCards(51))
    d1.showOnConsole()
    d2.showOnConsole()