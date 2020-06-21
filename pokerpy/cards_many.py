import pandas as pd
from pokerpy.card_single import Card
from random import shuffle, randint
from pokerpy.converters import *


class ListOfCards(list):

    """This is a group of cards.
        Inheriting from list class
        PlayerCards, Deck and Flop are ListOfCards"""

    conv: CardConverter
    score_converter: ScoreConverter

    def __str__(self):
        if not self:
            return 'No card in this group'
        else:
            _text = ''
            for _card in self:
                _text = _text + _card.name + ' '
            return _text

    @property
    def highest_card(self):
        _sorted = self
        _sorted.sort()
        return _sorted[len(self)-1]

    def create_deck(self, lowest_kind=2, decks=1):
        ListOfCards.score_converter = ScoreConverter(lowest_kind)
        ListOfCards.conv = CardConverter(lowest_kind)
        Card.conv = ListOfCards.conv
        for k in range(len(ListOfCards.conv.kind)):
            for s in range(4):
                for d in range(decks):
                    _card = Card(k, s)
                    self.append(_card)

    def shuffle(self):
        shuffle(self)

    def cut(self):
        _number_of_cards = randint(2, (len(self)-1))
        _cutted_cards = self[0:_number_of_cards]
        for _card in _cutted_cards:
            self.remove(_card)
        self.extend(_cutted_cards)

# Give and Select methods
    # useless?
    def select_card(self, index):
        self[index].selected = True

    # useless?
    def unselect_card(self, index: int):
        self[index].selected = False

    def give(self, number=5):
        # remove the first 'number' cards from this ListOfCards and return these Cards objects
        # number cannot be lower than zero
        number = max(0, number)
        # number cannot be higher than cards
        number = min(number, len(self))
        for i in range(number):
            self[i].selected = True
        return self.give_selected()

    # return selected cards list (and unselect them)
    def give_selected(self):
        _list = []
        _temp_list = list(self)
        for _card in _temp_list:
            if _card.selected:
                _card.selected = False
                _list.append(_card)
                self.remove(_card)
        return _list


class PlayerCards(ListOfCards):
    """The group of cards owned by the player
        plus the optional common cards
        Mainly, it's a ListOfCards with score evalutator and bestaCards list"""

    def __init__(self, *args):
        super().__init__(*args)
        #self.score = ListOfCards.score_converter.HighCard
        #self._partial_straight = ListOfCards.score_converter.partial_straight.Nothing
        self.score = 0
        self._partial_straight = 0
        self.best_five = []
        self.kind_cards = []
        self.straight_cards = []
        self._suit_cards = []

    def sorted(self):
        _list = self
        _list.sort()
        return _list

# Kind part
    # Return a list of list of 'num' cards with same kind
    def _kind_group(self, num: int):
        _list = []
        for k in range(len(ListOfCards.conv.kind)):
            _kind_list = [_card for _card in self.sorted() if _card.kind == k]
            if len(_kind_list) == num:
                _list.append(_kind_list)
        return _list

    # return score index (HighCard/Pair/TwoPair/ThreeOfKind/FullHouse/FourOfKind)
    def _create_kind_cards(self):
        _score = self.score_converter.HighCard
        self.kind_cards = []
        _fours = self._kind_group(4)

        if len(_fours) >= 1:
            self.kind_cards.extend(_fours[-1])
            _score = PlayerCards.score_converter.FourOfKind
        else:
            _pairs = self._kind_group(2)
            _threes = self._kind_group(3)
            # There could be more than one three, if player's got more than five cards
            if len(_threes) >= 1:
                if len(_threes) > 1:
                    _pair_from_three = _threes[-2]
                    _pair_from_three.__delitem__(0)
                    _pairs.append(_pair_from_three)
                    _pairs.sort()
                if len(_pairs) >= 1:
                    self.kind_cards.extend(_pairs[-1])
                    self.kind_cards.extend(_threes[-1])
                    _score = PlayerCards.score_converter.FullHouse
                else:
                    self.kind_cards.extend(_threes[0])
                    _score = PlayerCards.score_converter.ThreeOfKind
            elif len(_pairs) > 1:
                self.kind_cards.extend(_pairs[-2])
                self.kind_cards.extend(_pairs[-1])
                _score = PlayerCards.score_converter.TwoPair
            elif len(_pairs) == 1:
                self.kind_cards.extend(_pairs[0])
                _score = PlayerCards.score_converter.Pair
            else:
                _score = PlayerCards.score_converter.HighCard
        # Extending kind_cards with sorted _kickers
        self.kind_cards = self._kickers() + self.kind_cards
        _number_of_kind_cards = len(self.kind_cards)
        # Taking just the last 5 cards
        if _number_of_kind_cards > 5:
            self.kind_cards = self.kind_cards[(_number_of_kind_cards-5):_number_of_kind_cards]
        return _score

    def _kickers(self):
        _list = list(self)
        # Remove kind_cards from _kickers
        for _card in self.kind_cards:
            if _card in _list:
                _list.remove(_card)
            else:
                print(_card, ' is not in list')
        _list.sort()
        return _list

# Suit part
    # return index score (HighCard/Flush/RoyalFlush)
    def _create_suit_cards(self, prefer_highest_suit=False):
        _score = PlayerCards.score_converter.HighCard
        _highest_card = Card(0, 0)
        for s in range(4):
            _suit_list = PlayerCards([_card for _card in self.sorted() if _card.suit == s])
            _count = len(_suit_list)
            if _count >= 5:
                _list = _suit_list
                # Straight and Royal flush
                if _list._create_straight_cards() == PlayerCards.score_converter.Straight:
                    # Different rules: sometimes _highestSuit is better than _highest_card
                    if _list.highest_card >= _highest_card or prefer_highest_suit:
                        _highest_card = _list.highest_card
                        self._suit_cards = _list.straight_cards
                        if self._suit_cards[-1].kind == PlayerCards.conv.ace_rank:
                            _score = PlayerCards.score_converter.RoyalFlush
                        else:
                            _score = PlayerCards.score_converter.StraightFlush
                    # TO DO: use self._partial_straight to recognize partial straight
                else:
                    # Flush
                    # Different rules: sometimes _highestSuit is better than _highest_card
                    if _list.highest_card >= _highest_card or prefer_highest_suit:
                        _highest_card = _list.highest_card
                        # Taking just the last 5 cards
                        self._suit_cards = _list[(_count-5):_count]
                        _score = PlayerCards.score_converter.Flush
        return _score

# Straight part
    # Return a list of list of 'partial' straight
    def _straight_list(self):
        _list_of_lists = []
        # _no_duplicates_list is the list of the reversed Cards with no pair
        _no_duplicates_list = self.no_duplicates_list()
        if _no_duplicates_list[-1].kind == self.conv.ace_rank:
            _list = [_no_duplicates_list[-1]]
            _no_duplicates_list = _list + _no_duplicates_list
        _list = [_no_duplicates_list[0]]
        # Looping all cards, starting from the second
        for n in range(1, len(_no_duplicates_list)):
            _cardDifference = _no_duplicates_list[n].kind - _no_duplicates_list[n-1].kind
            if _cardDifference == 1 or _cardDifference == -self.conv.ace_rank:
                _list.append(_no_duplicates_list[n])
            else:
                _list_of_lists.append(_list)
                _list = [_no_duplicates_list[n]]
            if n == len(_no_duplicates_list)-1:
                _list_of_lists.append(_list)
        return _list_of_lists

    def no_duplicates_list(self):
        _list = PlayerCards(self)
        _list.sort()
        _erase_list = []
        for n in range(len(_list)-1):
            if _list[n].kind == _list[n+1].kind:
                _erase_list.append(n)
        _erase_list.reverse()
        for n in _erase_list:
            _list.remove(_list[n])
        return _list

    # return index score (HighCard or Straight)
    def _create_straight_cards(self):
        _score = PlayerCards.score_converter.HighCard
        self._partial_straight = self.score_converter.partial_straight.Nothing
        self.straight_cards = []
        _straight_list = self._straight_list()
        _reversed_index = list(range(len(_straight_list)))
        _reversed_index.reverse()
        # Looping all cards, starting from the highest
        for n in _reversed_index:
            _count = len(_straight_list[n])
            if _count >= 5:
                # Complete straight finded
                self.straight_cards.extend(_straight_list[n])
                self.straight_cards = self.straight_cards[(_count-5):_count]
                _score = PlayerCards.score_converter.Straight
                break
            elif _count == 4:
                # Looking for inside/outside StraightDraw
                if _straight_list[n][0].kind != self.conv.ace_rank and _straight_list[n][-1].kind != self.conv.ace_rank:
                    self._partial_straight = self.score_converter.partial_straight.OutsideStraightDraw
                else:
                    self._partial_straight = self.score_converter.partial_straight.InsideStraightDraw
            else:
                #
                if self._partial_straight == self.score_converter.partial_straight.Nothing:
                    if n < len(_straight_list)-1:
                        _partialCount = _count + len(_straight_list[n+1])
                        if _partialCount >= 4:
                            self._partial_straight = self.score_converter.partial_straight.InsideStraightDraw
        return _score

# ScoreFinder part
    def calculate_score(self):
        self.score = max(self._create_kind_cards(), self._create_suit_cards(), self._create_straight_cards())
        if self.score == self.score_converter.Straight:
            self.best_five = self.straight_cards
        elif self.score == self.score_converter.Flush or self.score == self.score_converter.StraightFlush or self.score == self.score_converter.RoyalFlush:
            self.best_five = self._suit_cards
        else:
            self.best_five = self.kind_cards

    @property
    def score_name(self):
        _name = self.score_converter.rank[self.score]
        _name = _name + ':'
        for _card in self.best_five:
            _name = _name + ' ' + _card.name
        return _name
    # change()
