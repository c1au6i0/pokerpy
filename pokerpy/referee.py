import pandas as pd


class Referee:

  @staticmethod
  def count_cards (self):
      counted_cards = self.hands.cards.groupby(self.hands.cards['cardNumber']).count().rename(columns={'suit': 'number_of'})
      return counted_cards


# from pokerpy.deck import Deck
# my_deck = Deck()
# dave.hands.cards = my_deck.extract_cards(5)