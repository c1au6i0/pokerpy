from pokerpy.ManyCards import *


class Player:
    name = ''
    # possibleMoves: collection
    # role: type
    # bankroll: money
    # seat: int
    cards: SetOfCards
    # the player doesn't know the real status of the real deck
    personalDeck: Deck
    def __init__(self):
        pass


# Pointer... or Talker?
class Pointer:
    # check)
    # call()
    # rise()
    # fold()
    # checkRise()
    # blind()
    # bigBlind()
    pass


class Human(Player):
    # orderRules
    pass


class Cyborg(Player):
    # speed
    # AI
    # maybe the next line is for another class
    # potentialGoodCards
    pass
