import pandas as pd
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

        # create a diff array, sort it and drop na
        cards_diff = self.cards.cardNumber.sort_values().diff(1)
        cards_diff = cards_diff.dropna().reset_index(drop=True)

        straight_point = []

        # summ all the 4 values, if 4 then straight
        if sum(cards_diff) == 4:
            straight_point.append("straight")
            return straight_point

        # it should be minus 3 but we have already removed and NA
        for i in range(cards_diff.size - 2):
            snippet = cards_diff.iloc[i: i + 3]
            if sum(snippet) == 4:
                straight_point.append("incastro")
            if sum(snippet) == 3:
                straight_point.append("bilaterale")
        # print(straight_point)
        return straight_point

    # with this we get also the index so from that we can check the flush
    # p_diff = prova.sort_values().diff(1).dropna()
    # straight = []
    # ids = []
    #
    # for i in range(p_diff.size - 2):
    #     x = p_diff.iloc[i: i + 3]
    #     if sum(x) == 4:
    #         straight.append("incastro")
    #         ids.append(x.index)
    #     if sum(x) == 3:
    #         straight.append("bilaterale")
    #         ids.append(x.index)
    #
    # ids = list(map(lambda x: np.append(x[0] - 1, x), ids))
    # # ids = [np.append(x[0] - 1 , x) for x in ids]




if __name__ == '__main__':
    dave = Player(name='Dave')
    my_deck = Deck()
    print("my_deck and dave created!\n\nWe start shuffling the deck!\n\n")
    my_deck.shuffle()
    print("\n\nNow we take 5 cards from the deck and we give them to dave\n\n")
    extracted = my_deck.give_cards(5)
    print(extracted)
    dave.hand.cards = extracted
    print("\n\nNow look in dave hands!")

# import pdb
# pdb.set_trace()

# from pokerpy.deck import Deck
# my_deck = Deck()




























