from pokerpy.players import *
from pokerpy.consts import *


class Dealer:

    """The Dealer control the cards,
        giving and taking them for then deck, the shared cards and the players"""

    lowest_kind: int

    @classmethod
    def set_rules(cls, kind_of_deck=AMERICAN_DECK, number_cards_shared=0, number_cards_for_player=5):
        cls._kind_of_deck = kind_of_deck
        cls._number_cards_shared = number_cards_shared
        cls._number_cards_for_player = number_cards_for_player
        cls.players = []

    @classmethod
    def start_hand(cls):

        """ Reset all the groups of cards (player, shared, rejects)
            Create, fill and shuffle the deck
            Choose shared_cards
            Give the cards and a copy of the deck to all the players """

        if len(cls.players) == 0:
            return False
        else:
            if cls._kind_of_deck == AMERICAN_DECK:
                cls.lowest_kind = 2
            else:
                cls.lowest_kind = 11 - len(cls.players)
            cls.deck = ListOfCards()
            cls.deck.create_deck(cls.lowest_kind)
            cls.deck.shuffle()
            cls.rejects = ListOfCards()
            for _player in cls.players:
                _player.cards = PlayerCards()
                _player.import_deck(cls.deck)
            cls.shared_cards = ListOfCards()
            cls.shared_cards.extend(cls.deck.give(cls._number_cards_shared))
            for _player in cls.players:
                _player.take_cards(cls.deck.give(cls._number_cards_for_player))
            return True

    @classmethod
    def add_players(cls, *players):
        """Add the players"""
        cls.players.extend(players)

    @classmethod
    def face_up_shared_cards(cls, num=1):
        _shared_cards = cls.shared_cards.give(num)
        for _player in cls.players:
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