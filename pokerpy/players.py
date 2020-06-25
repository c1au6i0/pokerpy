import pandas as pd
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

        Returns: a dataframe with  2 columns, the cardNumber or suits, and the number of occurrances.

        """
        assert what in ['cardNumber', 'suits'], print("The argument what is not one of ['cardNumber', 'suits']!")

        counted_cards = self.cards.groupby(self.cards[what]).count()
        counted_cards.rename(columns={counted_cards.columns[0]:'number_of'}, inplace=True)
        counted_cards = counted_cards.loc[:,['number_of']]
        return counted_cards




if __name__ == '__main__':
    dave = Player(name='Dave')
    my_deck = Deck()
    print("my_deck and dave created!\n\nWe start shuffling the deck!\n\n")
    my_deck.shuffle()
    print("\n\nNow we take 5 cards from the deck and we give them to dave\n\n")
    extracted = my_deck.extract_cards(5)
    print(extracted)
    dave.hand.cards = extracted
    print("\n\nNow look in dave hands!")





# from pokerpy.deck import Deck
# my_deck = Deck()
# dave.hands.cards = my_deck.extract_cards(5)