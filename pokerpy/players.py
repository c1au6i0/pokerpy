import pandas as pd
import numpy as np
from pandas import DataFrame

from pokerpy.deck import Deck
# from pokerpy.referee import Referee


class Player():
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
        self.hand = PlayerCards()


class PlayerCards(Deck):
    """
      Player cards are just a particular Deck, and we always start empty handed
    """

    def __init__(self):
        self.cards = pd.DataFrame()

    def count_cards(self, what):
        """
        Calculate the number of occurrences of a card number or of a suit

        Args:
            what: one of  ['cardNumber', 'suits']

        Returns: a dataframe with  2 columns, the cardNumber or suits, and the number of occurrences.

        """
        assert what in ['cardNumber', 'suits'], print("The argument what is not one of ['cardNumber', 'suits']!")

        counted_cards = self.cards.groupby(self.cards[what]).count()
        counted_cards.rename(columns={counted_cards.columns[0]:'number_of'}, inplace=True)
        counted_cards = counted_cards.loc[:,['number_of']]
        return counted_cards

    def identify_straight(self):

        self.cards = self.cards.sort_values(by=['cardNumber'])
        # create a diff array, sort it and drop na
        cards_diff = self.cards.cardNumber.diff(1)
        cards_diff = cards_diff.dropna()

        straight_point = []
        ids_straight = []

        # summ all the 4 values, if 4 then straight
        if set(cards_diff) == set([1, 1, 1, 1]):
            straight_point.append("straight")
            ids_straight.append(self.cards.index)
            return straight_point, ids_straight


        # it should be minus 3 but we have already removed and NA
        for i in range(cards_diff.size - 2):
            snippet = cards_diff.iloc[i: i + 3]
            #this has a bug: we can have same card twice
            if set(snippet.values) == set([1, 1, 2]):
                straight_point.append("incastro")
                ids_straight.append(snippet.index)
            if set(snippet.values) == set([1, 1, 1]):
                straight_point.append("bilaterale")
                ids_straight.append(snippet.index)

        ids_straight = list(map(lambda x: np.append(x[0] - 1, x), ids_straight))
        # ids = [np.append(x[0] - 1 , x) for x in ids]
        # import pdb
        # pdb.set_trace()
        return straight_point, ids_straight



if __name__ == '__main__':
    dave = Player(name='Dave')
    my_deck = Deck()
    print("my_deck and dave created!\n\nWe start shuffling the deck!\n\n")
    my_deck.shuffle()
    print("\n\nNow we take 5 cards from the deck and we give them to dave")
    extracted = my_deck.give_cards(5)
    dave.hand.cards = extracted
    print("\n\nNow look in dave hands! He has a straight the MF!")
    dave.hand.cards.cardNumber = [3,4,5,6,10]
    print(dave.hand.cards)
    # dave.hand.identify_straight()


# import pdb
# pdb.set_trace()

# from pokerpy.deck import Deck
# my_deck = Deck()




























