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
    as a symbol. Finally, it since you don't work with 3 separate arrays, it is less prone to errors.

    Parameters:
        numCards : number of cards for each suit (default is 13). If less than for 13, cards will be removed starting from
             2 and up.
     """

    def __init__(self, numCards=13):
        start = 15 - numCards
        cardNumber = np.arange(start, 15, 1).repeat(4)
        suits = np.arange(1, 5, 1).repeat(cardNumber.size / 4)
        self.df = pd.DataFrame({'cardNumber': cardNumber, 'suits': suits})
        self.df['fullCard'] = self.df.cardNumber.astype(str).replace({'1': "A", '14': "K", '13': "Q", '12': "J"}) + self.df.suits.astype(str).replace({'1': "♣", '2': "♢", '3': "♠", '4': "♡"})
        # return self.df

    # df.head(5), df.tail(5), df.sample(5, replace = false)
    # import pandas as pd
    # import numpy as np
    # np.random.seed(10)
    #
    # remove_n = 1
    # df = pd.DataFrame({"a":[1,2,3,4], "b":[5,6,7,8]})
    # drop_indices = np.random.choice(df.index, remove_n, replace=False)
    # df_subset = df.drop(drop_indices)
    #
    #
    #
