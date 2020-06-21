import pandas as pd
from pokerpy.deck import Deck



class Player:
    """"
    Player. So far someone with a name and hands.

     """

    def __init__(self, name):
        """

        :param name:
        :param role:
        :param possible_moves:
        :param seat:
        :param player_cards:
        """
        self.name = name
        # self.role = role
        # self.possible_moves = possible_moves
        # self.seat = seat
        self.hands = PlayerCards()


class PlayerCards(Deck):
    """
      Player cards are just a particular Deck, and we always start empty handed
    """

    def __init__(self):
        self.cards = pd.DataFrame()



if __name__ == '__main__':
    dave = Player(name='Dave')
    my_deck = Deck()
    print("my_deck and dave created!\n\nWe start shuffling the deck!\n\n")
    my_deck.shuffle()
    print("\n\nNow we take 5 cards from the deck and we give them to dave\n\n")
    extracted = my_deck.extract_cards(5)
    print(extracted)
    dave.hands.cards = extracted
    print("\n\nNow look in dave hands!")





# from pokerpy.deck import Deck
# my_deck = Deck()
# dave.hands.cards = my_deck.extract_cards(5)