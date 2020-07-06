from pokerpy.card_single import Card
from pokerpy.score import *
from pokerpy.consts import *
from random import shuffle, randint


class ListOfCards(list):

    """ListOfCards is a group of cards.
        Inheriting from list class
        i.e. Deck is a ListOfCards
    """

    lowest_kind: int

    def __str__(self):
        """Return all the cards name in the list"""
        if not self:
            return 'No card in this group'
        else:
            _text = ''
            for _card in self:
                _text = _text + _card.name + ' '
            return _text

    def sorted(self):
        """Return the Sorted PlayerCards list"""
        _sorted_list = self
        _sorted_list.sort()
        return _sorted_list

    def create_deck(self, lowest_kind=2, decks=1):
        """Create the deck, starting with choosed lowest_kind to Ace
            Args:
                lowest_kind: default is 2, American deck
                decks: default is 1, Poker deck, but you could have 2 decks for Blackjack
        """
        if lowest_kind == 2:
            ScoreIndex.initialize(AMERICAN_DECK)
            ScoreRules.initialize(AMERICAN_DECK)
        else:
            ScoreIndex.initialize(ITALIAN_DECK)
            ScoreRules.initialize(ITALIAN_DECK)
        ListOfCards.lowest_kind = lowest_kind
        for k in range(lowest_kind, 15):
            for s in range(4):
                for d in range(decks):
                    _card = Card(k, s)
                    self.append(_card)

    def shuffle(self):
        """Shuffle the deck"""
        shuffle(self)

    def cut(self):
        """Cut the deck"""
        _number_of_cards = randint(2, (len(self)-1))
        _cutted_cards = self[0:_number_of_cards]
        for _card in _cutted_cards:
            self.remove(_card)
        self.extend(_cutted_cards)

# Give and Select methods
    # useless?
    def select_card(self, index=0):
        """Select a card
            Args:
                index: default is 0, the first card of the list
        """
        self[index].selected = True

    # useless?
    def unselect_card(self, index=0):
        """Unselect a card
            Args:
                index: default is 0, the first card of the list
        """
        self[index].selected = False

    def give(self, number_of_cards=5):
        """Remove some cards from this ListOfCards
            Return these Cards objects
            Args:
                number_of_cards: default is 5
        """
        # number cannot be lower than zero
        number_of_cards = max(0, number_of_cards)
        # number cannot be higher than cards
        number_of_cards = min(number_of_cards, len(self))
        for i in range(number_of_cards):
            self[i].selected = True
        return self.give_selected()

    def give_selected(self):
        """Return the list of the selected cards (and unselect them)"""
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
        self.score = 0
        self.partial_straight = 0
        self.best_five = []
        self.kind_cards = []
        self.straight_cards = []
        self.suit_cards = []
        self.exist_outside_straight_draw = False

    # Kind part
    def _kind_group(self, number_of_equal_cards: int):
        """Return the list of the groups of cards with same kind"""
        _list = []
        for k in range(self.lowest_kind, 15):
            _kind_list = [_card for _card in self.sorted() if _card.kind == k]
            if len(_kind_list) == number_of_equal_cards:
                _list.append(_kind_list)
        return _list

    def _create_kind_cards(self):
        """Return the kind score index (HighCard/Pair/TwoPair/ThreeOfKind/FullHouse/FourOfKind)"""
        _score = ScoreIndex.HighCard
        self.kind_cards = []
        _fours = self._kind_group(4)

        if len(_fours) >= 1:
            self.kind_cards.extend(_fours[-1])
            _score = ScoreIndex.FourOfKind
        else:
            _pairs = self._kind_group(2)
            _threes = self._kind_group(3)
            # There could be more than one 'three', if player's got more than five cards
            if len(_threes) >= 1:
                if len(_threes) > 1:
                    _pair_from_three = _threes[-2]
                    _pair_from_three.__delitem__(0)
                    _pairs.append(_pair_from_three)
                    _pairs.sort()
                if len(_pairs) >= 1:
                    self.kind_cards.extend(_pairs[-1])
                    self.kind_cards.extend(_threes[-1])
                    _score = ScoreIndex.FullHouse
                else:
                    self.kind_cards.extend(_threes[0])
                    _score = ScoreIndex.ThreeOfKind
            elif len(_pairs) > 1:
                self.kind_cards.extend(_pairs[-2])
                self.kind_cards.extend(_pairs[-1])
                _score = ScoreIndex.TwoPair
            elif len(_pairs) == 1:
                self.kind_cards.extend(_pairs[0])
                _score = ScoreIndex.Pair
            else:
                _score = ScoreIndex.HighCard
        # Extending kind_cards with sorted _kickers
        self.kind_cards = self._kickers() + self.kind_cards
        _number_of_kind_cards = len(self.kind_cards)
        # Taking just the last 5 cards
        if _number_of_kind_cards > 5:
            self.kind_cards = self.kind_cards[(_number_of_kind_cards-5):_number_of_kind_cards]
        return _score

    def _kickers(self):
        """Return the _kickers rekated to Pair/TwoPair/ThreeOfKind/FourOfKind"""
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
    def _create_suit_cards(self, prefer_highest_suit=False):
        """Return the Suit score index (HighCard/Flush/RoyalFlush)"""
        _score = ScoreIndex.HighCard
        # Starting with the lowest card
        _highest_card = Card(self.lowest_kind, 0)
        for s in range(4):
            _suit_list = PlayerCards([_card for _card in self.sorted() if _card.suit == s])
            _count = len(_suit_list)
            if _count >= 5:
                _list = _suit_list
                # Straight and Royal flush
                if _list._create_straight_cards() == ScoreIndex.Straight:
                    # Different rules: sometimes _highestSuit is better than _highest_card
                    if _list[-1] >= _highest_card or prefer_highest_suit:
                        _highest_card = _list[-1]
                        self.suit_cards = _list.straight_cards
                        if self.suit_cards[-1].kind == 15:
                            _score = ScoreIndex.RoyalFlush
                        else:
                            _score = ScoreIndex.StraightFlush
                else:
                    # Flush
                    # Different rules: sometimes _highestSuit is better than _highest_card (TO DO: r u sure?)
                    if _list[-1] >= _highest_card or prefer_highest_suit:
                        _highest_card = _list[-1]
                        # Taking just the last 5 cards
                        self.suit_cards = _list[(_count-5):_count]
                        _score = ScoreIndex.Flush
        return _score

    # TO DO: test it
    def _exist_outside_straight_flush_draw(self):
        _reversed_suit_list = list(range(4))
        _reversed_suit_list.reverse()
        for s in _reversed_suit_list:
            _suit_list = PlayerCards([_card for _card in self.sorted() if _card.suit == s])
            # TO DO: create straight draw?
            if _suit_list._create_straight_draw_cards() == ScoreIndex.partial_straight.OutsideStraightDraw:
                # self.best_five = _suit_list
                return True
        return False

# Straight part
    def _all_straight_list(self):
        """Return a list of straights and straight draw's"""
        _list_of_lists = []
        # _no_duplicates_list is the list of the Cards with no pair
        _no_duplicates_list = self.no_duplicates_list()
        if len(_no_duplicates_list) > 0:
            if _no_duplicates_list[-1].kind == 15:
                _list = [_no_duplicates_list[-1]]
                _no_duplicates_list = _list + _no_duplicates_list
            _list = [_no_duplicates_list[0]]
            # Looping all cards, starting from the second
            for n in range(1, len(_no_duplicates_list)):
                _cardDifference = _no_duplicates_list[n].kind - _no_duplicates_list[n-1].kind
                # cardDifference == 1 means than the cards are 'near'
                # cardDifference == 15 means that the cards are the lowest and an ace
                if _cardDifference == 1 or _no_duplicates_list[n-1].kind == 15:
                    _list.append(_no_duplicates_list[n])
                else:
                    # Cards are not near so I have to close the _list
                    _list_of_lists.append(_list)
                    _list = [_no_duplicates_list[n]]
            # After the loop I have to add the 'open' list to the list of lists
            _list_of_lists.append(_list)
        return _list_of_lists

    def no_duplicates_list(self):
        """Return the PlayerCards list woth no kind duplicates"""
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

    def _create_straight_cards(self):
        """Create the best complete straight cards list
            and return index score (HighCard/Straight)
            """
        self.straight_cards = []
        # From _all_straight_list take only the complete lists (len>=5)
        _straight_list = [_list for _list in self._all_straight_list() if len(_list) >= 5]
        if len(_straight_list) == 0:
            _score = ScoreIndex.HighCard
        else:
            _count = len(_straight_list[-1])
            self.straight_cards.extend(_straight_list[-1])
            self.straight_cards = self.straight_cards[(_count-5):_count]
            _score = ScoreIndex.Straight
        return _score

    # TO DO: never tested
    def _create_straight_draw_cards(self):
        """Create the list of the straight draw's
            and return an index score
            (HighCard/OutsideStraightDraw/InsideStraightDraw)"""
        # From _all_straight_list take only the straight draw (len<5)
        _draw_list = list()
        _draw_list = [_list for _list in self._all_straight_list() if len(_list) < 5]
        _draw_list = PlayerCards(_draw_list)
        _score = 0
        if len(_draw_list) == 0:
            _score = ScoreIndex.partial_straight.Nothing
        else:
            _reversed_index = list(range(len(_draw_list)))
            _reversed_index.reverse()
            # Looping all cards, starting from the highest
            for n in _reversed_index:
                _count = len(_draw_list[n])
                # If straight's lenght is 4, you just need to understand if it's an outside or an inside straight
                if _count == 4:
                    # Choosing between inside/outside StraightDraw
                    if _draw_list[n][0].kind != 15 and _draw_list[n][-1].kind != 15:
                        _score = ScoreIndex.partial_straight.OutsideStraightDraw
                        break
                    else:
                        _score = ScoreIndex.partial_straight.InsideStraightDraw
                        break
                else:
                    # Looking for inside StraightDraw
                    if _score == ScoreIndex.partial_straight.Nothing:
                        # I need this "if" or I will have problems with "n+1"
                        if n < len(_draw_list)-1:
                            _partialCount = _count + len(_draw_list[n+1])
                            if _partialCount >= 4:
                                # I check the difference between highest card of lowest straight
                                # and lowest card of highest straight
                                if _draw_list[n+1][0].kind - _draw_list[n][-1].kind == 2:
                                    _score = ScoreIndex.partial_straight.InsideStraightDraw
        return _score

# ScoreIndexFinder part
    def calculate_score(self):
        """Calculate the score and fill the the best_five cards list"""
        self.score = max(self._create_kind_cards(), self._create_suit_cards(ScoreRules.consider_suit), self._create_straight_cards())
        if self.score == ScoreIndex.Straight:
            self.best_five = self.straight_cards
        elif self.score == ScoreIndex.Flush or self.score == ScoreIndex.StraightFlush or self.score == ScoreIndex.RoyalFlush:
            self.best_five = self.suit_cards
        else:
            self.best_five = self.kind_cards
        if self._exist_outside_straight_flush_draw():
            # TO DO: looking for 4/5 StraightFlush
            # partial_straight
            # self.best_five = self.kind_cards
            print('_exist_outside_straight_flush_draw')

    @property
    def score_name(self):
        _name = ScoreIndex.rank[self.score]
        _name = _name + ':'
        for _card in self.best_five:
            _name = _name + ' ' + _card.name
        return _name
    # change()
