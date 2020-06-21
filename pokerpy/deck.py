import pandas as pd
import numpy as np


class Deck:
    """" Deck of cards a Pandas dataframe

    A dataframe called cards containing 3 columns, with each row representing a card:
        cardNumber :  numeric, J, Q, K, Ace are 11, 12, 13, 14
        suit :  1, 2, 3, 4, equivalent to clubs, diamonds, hearts, spades.
        fullCard : as it would be show in the console if playing with symbols for the suits and J, K, Q
                   {"Hearts":"♡", "Spades":"♠", "Diamonds":"♢", "Clubs":"♣"}

    Why 3 columns? so it is easier to sort order cards, and easier to check suits, but still you can report the card
    as a symbol. Finally, since you don't work with 3 separate arrays, it is less prone to errors.


    Parameters:
        numCards : number of cards for each suit (default is 13).
     """

    def __init__(self, numCards=13):
        start = 15 - numCards
        cardNumber = np.tile(np.arange(start, 16, 1), 4)
        suits = np.arange(1, 5, 1).repeat(cardNumber.size / 4)
        self.cards = pd.DataFrame({'cardNumber': cardNumber, 'suits': suits})
        self.cards['fullCard'] = self.cards.cardNumber.astype(str).replace(
            {'15': "A", '14': "K", '13': "Q", '12': "J"}) + self.cards.suits.astype(str).replace(
            {'1': "♠", '2': "♢", '3': "♣", '4': "♡"})

    def take_cards(self, index_card):
        """
        Extract one or multiple card from a particular position
        this is used internally by extract_cards

        :param index: a single list with on of more int
        :return: subset of the deck
        """

        # check if there position is within df.shape
        assert np.array([index_card]).max() <= len(self.cards.index), print("One or more cards not present!")

        # check if there are duplicate indexes
        assert pd.Series(index_card).duplicated().sum() == 0, print("You can't use duplicate indexes")

        extracted_cards = self.cards.loc[index_card]
        self.cards = self.cards.drop(index_card, axis=0).reset_index(drop=True)
        return extracted_cards

    def extract_cards(self, numExtract, fromPos='top'):
        """
        Extract cars from the deck.df. it uses take_cards.
        :param numExtract: number of cards to extract
        :param fromPos: position one of ['top', 'bottom', 'random']
        :return: a slice of the deck
        """
        # import pdb
        # pdb.set_trace()

        assert type(numExtract) == int, print(f"id is not an integer the type is : {type(numExtract)}")
        assert fromPos in ['top', 'bottom', 'random'], print(f"fromPos is not one of ['top', 'bottom', 'random'] !")

        if fromPos == 'top':
            to_extract = np.arange(self.cards.index[0], self.cards.index[0] + numExtract, 1)
        elif fromPos == 'bottom':
            to_extract = np.arange(self.cards.shape[0] - numExtract, self.cards.shape[0], 1)
        elif fromPos == 'random':
            to_extract = np.random.choice(self.cards.index, numExtract, replace=False)

        extracted_cards = self.take_cards(to_extract)
        return extracted_cards

    def shuffle(self):
        """
        Shuffle the deck.df
        :return: deck.df
        """
        self.cards = self.cards.sample(frac=1).reset_index(drop=True)
        print("Deck shuffled, Gringo!")


if __name__ == '__main__':
    my_deck = Deck()

# import pdb
# pdb.set_trace()























