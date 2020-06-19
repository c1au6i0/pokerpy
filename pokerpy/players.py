import pandas as pd
from pokerpy.deck import Deck


class Player:
    """"
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
        # self.player_cards = player_cards


class PlayerCards(Deck):

    def __init__(self):
        self.cards = pd.DataFrame()



if __name__ == '__main__':
    dave = PlayerCards()
