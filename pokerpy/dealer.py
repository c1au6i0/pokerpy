from pokerpy.cards_many import *
from pokerpy.players import *


class Croupier:

    def __init__(self, lowestKind=2, numForPlayer=5, numShared=0):
        self.lowestKind = lowestKind
        self.players = []
        self.deck = Cardlist()
        self.rejects = Cardlist()
        self.sharedCards = Cardlist()
        self._numShared = numShared
        self._numForPlayer = numForPlayer

    def startDeck(self):
        if len(self.players) == 0:
            return False
        else:
            self.deck.createDeck(self.lowestKind)
            self.deck.shuffle()
            for _player in self.players:
                _player.importDeck(self.deck)
            return True

    def giveStartingCards(self):
        for _player in self.players:
            _player.takeCards(self.deck.give(self._numForPlayer))
        self.sharedCards.extend(self.deck.give(self._numShared))

    def addPlayer(self, player: Player):
        self.players.append(player)

    # TO DO: fix it
    def addPlayers(self, *players):
        self.addPlayer(*players)

    def showSharedCards(self, num=1):
        _sharedCards = self.sharedCards.give(num)
        for _player in self.players:
            _player.takeCards(_sharedCards)


class PlayingBoard:
    # placeCard
    # sharedCards: Cardlist()
    # pot(0, 1, 2....): pot
    # seat: place
    # setSharedCards()
    # showSharedCard()
    pass


class Director:
    # def assignHandRoles:
    # numberPlayers: int
    # turnsLeft
    # setDealer()
    # setTalk()
    # setPhase()
    # addPlayer()
    # removePlayer()
    # setTurns()
    pass


class HandPhase:
    # assign roles
    # playerRole=(mazziere,puntatore,cambiatore,buio,comtrobuio,over,eliminato,resti)
    # tipoApertura=(normale,di parola,nessuno aprì)
    # puntataIniziale e buio
    # distribuzioneCarte
    # puntata
    # cambioCarte
    # scopriCartaComune
    # mostraPunti
    # proclamaVincitore
    pass


class MatchPhase:
    # choose players
    # assign seats
    # Hands()
    # giri
    # ultima mano prima dei giri
    pass