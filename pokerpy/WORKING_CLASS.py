# Temporary class and methods to help test, debug, etc.
# erase it at the end of the Project
# import array as arr
from pokerpy.converters import CardRankConverter
from pokerpy.players import Human
from pokerpy.referee import Evaluator
from pokerpy.cards_many import *
from pokerpy.money import Pot
from pokerpy.card_single import Card


def testCardList():
    conv = CardRankConverter(7)
    c1 = Card(conv, (1, 1))
    c2 = Card(conv, (0, 1))
    CardList.importConverter(conv)
    deck = CardList()
    print(deck)
    deck.extend((c1, c2))
    print(deck)


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
    conv = CardRankConverter(7)
    Players = [Human("Dave"), Human("Claude")]
    deck = Deck(conv)
    deck.shuffle()
    referee = Evaluator(conv)
    Players[0].startHand(conv)
    Players[1].startHand(conv)
    # create the players cards obj
    commonCards = CommonCards(conv)
    commonCards.takeCards(deck.giveCards(3))
    Players[0].takeCards(deck.giveCards(5))
    Players[1].takeCards(deck.giveCards(5))
    Players[0].takeCards(commonCards.cards)
    Players[1].takeCards(commonCards.cards)
    Players[0].playerCards.calculateScore()
    Players[1].playerCards.calculateScore()
    print(Players[0].name, "'s score is", Players[0].playerCards.scoreName)
    Players[0].playerCards.showOnConsole()
    #
    print()
    print(Players[1].name, "'s score is", Players[1].playerCards.scoreName)
    Players[1].playerCards.showOnConsole()
    print()
    print(referee.headToheadWinner(Players[0], Players[1]))


def testTexas():
    # create the deck and shuffle it
    print()
    print('- - - TEXAS TEST - - -')
    conv = CardRankConverter(2)
    Players = [Human("Dave"), Human("Claude")]
    deck = Deck(conv)
    deck.shuffle()
    referee = Evaluator(conv)
    Players[0].startHand(conv)
    Players[1].startHand(conv)
    # create the players cards obj
    flop = CommonCards(conv)
    turn = CommonCards(conv)
    river = CommonCards(conv)
    Players[0].takeCards(deck.giveCards(2))
    Players[1].takeCards(deck.giveCards(2))
    flop.takeCards(deck.giveCards(3))
    turn.takeCards(deck.giveCards(1))
    river.takeCards(deck.giveCards(1))
    Players[0].playerCards.calculateScore()
    Players[1].playerCards.calculateScore()
    print(Players[0].name, "'s score is", Players[0].playerCards.scoreName)
    print(Players[1].name, "'s score is", Players[1].playerCards.scoreName)
    print()
    print('Flop: ')
    flop.showOnConsole()
    Players[0].takeCards(flop.cards)
    Players[1].takeCards(flop.cards)
    Players[0].playerCards.calculateScore()
    Players[1].playerCards.calculateScore()
    print(Players[0].name, "'s score is", Players[0].playerCards.scoreName)
    print(Players[1].name, "'s score is", Players[1].playerCards.scoreName)
    print()
    print('Turn: ')
    turn.showOnConsole()
    Players[0].takeCards(turn.cards)
    Players[1].takeCards(turn.cards)
    Players[0].playerCards.calculateScore()
    Players[1].playerCards.calculateScore()
    print(Players[0].name, "'s score is", Players[0].playerCards.scoreName)
    print(Players[1].name, "'s score is", Players[1].playerCards.scoreName)
    print()
    print('River')
    river.showOnConsole()
    Players[0].takeCards(river.cards)
    Players[1].takeCards(river.cards)
    Players[0].playerCards.calculateScore()
    Players[1].playerCards.calculateScore()
    print(Players[0].name, "'s score is", Players[0].playerCards.scoreName)
    print(Players[1].name, "'s score is", Players[1].playerCards.scoreName)
    #
    print()
    print(referee.headToheadWinner(Players[0], Players[1]))