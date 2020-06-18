import pandas as pd
import numpy as np
from types import *


class Deck:
    """" Deck of cards a Pandas dataframe

    A dataframe called cards containing 3 columns, with each row representing a card:
        cardNumber :  numeric, J, Q, K, Ace are 11, 12, 13, 14
        suit :  1, 2, 3, 4, equivalent to clubs, diamonds, hearts, spades.
        fullCard : as it would be show in the console if playing with symbols for the suits and J, K, Q
                   {"Hearts":"♡", "Spades":"♠", "Diamonds":"♢", "Clubs":"♣"}

    Why 3 columns? so it is easier to sort order cards, and easier to check suits, but still you can report the card
    as a symbol. Finally, it since you don't work with 3 separate arrays, it is less prone to errors.

    Parameters:
        numCards : number of cards for each suit (default is 14). If less than for 14.
     """

    def __init__(self, numCards=13):
        start = 15 - numCards
        cardNumber = np.tile(np.arange(start, 15, 1), 4)
        suits = np.arange(1, 5, 1).repeat(cardNumber.size / 4)
        self.df = pd.DataFrame({'cardNumber': cardNumber, 'suits': suits})
        self.df['fullCard'] = self.df.cardNumber.astype(str).replace(
            {'15': "A", '14': "K", '13': "Q", '12': "J"}) + self.df.suits.astype(str).replace(
            {'1': "♠", '2': "♢", '3': "♣", '4': "♡"})

    def extract_cards(self, numExtract, fromPos='top'):
        """
        Extract cars from the deck.df
        :param numExtract: number of cards to extract
        :param fromPos: position one of ['top', 'bottom', 'random']
        :return: a slice of the deck
        """

        # assert type(numExtract) != int, "id is not an integer: %r" % numExtract
        # assert fromPos not in ['top', 'bottom', 'random'], "fromPos is ['top', 'bottom', 'random']: %r" % numExtract

        if fromPos == 'top':
            to_extract = np.arange(self.df.index[0], self.df.index[0] + numExtract, 1)
        elif fromPos == 'bottom':
            to_extract = np.arange(self.df.shape[0] - numExtract, self.df.shape[0], 1)
        elif fromPos == 'random':
            to_extract = np.random.choice(self.df.index, numExtract, replace=False)

        extracted_cards = self.df.loc[to_extract]
        self.df = self.df.drop(to_extract, axis=0)
        return extracted_cards

    def shuffle(self):
        """
        Shuffle the deck.df
        :return: deck.df
        """
        self.df = self.df.sample(frac=1).reset_index(drop=True)
        print("Deck shuffled, Amigo!")
