import pandas as pd


class Player:
    """"
     """

    def __init__(self, name, role, possible_moves, seat, player_cards=pd.DataFrame()):
        """

        :param name:
        :param role:
        :param possible_moves:
        :param seat:
        :param player_cards:
        """
        self.name = name
        self.role = role
        self.possible_moves = possible_moves
        self.seat = seat
        self.player_cards = player_cards



