from pokerpy.cards_many import *
from pokerpy.players import *


class Croupier:

    def __init__(self, lowest_kind=2, number_cards_for_player=5, number_cards_shared=0):
        self.lowest_kind = lowest_kind
        self.players = []
        self.deck = ListOfCards()
        self.rejects = ListOfCards()
        self.shared_cards = ListOfCards()
        self._number_cards_shared = number_cards_shared
        self._number_cards_for_player = number_cards_for_player

    def start_deck(self):
        if len(self.players) == 0:
            return False
        else:
            self.deck.create_deck(self.lowest_kind)
            self.deck.shuffle()
            for _player in self.players:
                _player.import_deck(self.deck)
            return True

    def give_starting_cards(self):
        for _player in self.players:
            _player.take_cards(self.deck.give(self._number_cards_for_player))
        self.shared_cards.extend(self.deck.give(self._number_cards_shared))

    def add_players(self, *players):
        self.players.extend(players)

    def show_shared_cards(self, num=1):
        _shared_cards = self.shared_cards.give(num)
        for _player in self.players:
            _player.take_cards(_shared_cards)


class PlayingBoard:
    # place_card
    # shared_cards: ListOfCards()
    # pot(0, 1, 2....): pot
    # seat: place
    # setshared_cards()
    # showSharedCard()
    pass


class Director:
    # def assignHandRoles:
    # numberPlayers: int
    # turnsLeft
    # setDealer()
    # setTalk()
    # setPhase()
    # add_player()
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