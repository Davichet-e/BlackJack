"""
Author: David García Morillo
"""
from typing import List

from deck import Card, Deck

my_deck: Deck = Deck()


class BlackJackHand:
    """
    TODO
    """

    def __init__(self):
        self._cards: List[Card] = my_deck.get_initial_cards()
        self._points: int = Deck.sum_points(self._cards)
        self._aces: int = 0
        for card in self._cards:
            self._count_aces(card)
        self._check_ace_points()

    def __repr__(self) -> str:
        return ", ".join(map(repr, self._cards)) + "."

    @property
    def cards(self) -> List[Card]:
        return self._cards

    @property
    def points(self) -> int:
        return self._points

    def initialize_attributes(self):
        if issubclass(self.__class__, BlackJackHand):
            # Checks if the class is being inherited. If so,
            # calls only the __init__ method of this class
            BlackJackHand.__init__(self)
        else:
            self.__init__()

    def deal_card(self):
        card: Card = my_deck.deal_card()
        self._count_aces(card)
        self._cards.append(card)
        self._update_points(card)
        self._check_if_lose()

    def _count_aces(self, card: Card):
        assert isinstance(card, Card), "The 'card' type must be Card"
        if card.name == "ACE":
            self._aces += 1

    def _check_ace_points(self):
        while self._points > 21 and self._aces:
            self._points -= 10
            self._aces -= 1

    def _check_if_lose(self):
        if self._points > 21:
            self._points = 0

    def _update_points(self, card: Card):
        assert isinstance(card, Card), "The 'card' type must be Card"
        self._points += card.value
        self._check_ace_points()


def get_my_deck() -> Deck:
    return my_deck

