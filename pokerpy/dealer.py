from pokerpy.cards_many import Cardlist


class Croupier:
    deck = Cardlist()
    rejects = Cardlist()


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