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


# from pokerpy.deck import Deck
# my_deck = Deck()
# dave.hands.cards = my_deck.extract_cards(5)