"""
Author: David García Morillo
"""
from typing import ClassVar, List

from deck import Card, Deck


class Hand:
    """
    This class represents a 21 BlackJack hand on python
    """

    DECK: ClassVar[Deck] = Deck()

    def __init__(self):
        self._cards: List[Card] = Hand.DECK.get_initial_cards()
        self._points: int = Hand.calculate_points(self._cards)
        self._aces: int = 0
        for card in self._cards:
            self._check_if_ace(card)
        self._check_ace_points()

    def __str__(self) -> str:
        return ", ".join([f"{card}" for card in self._cards]) + "."

    @property
    def cards(self) -> List[Card]:
        return self._cards

    @property
    def points(self) -> int:
        return self._points

    def initialize_attributes(self) -> None:
        self.__init__()

    def deal_card(self) -> None:
        card: Card = Hand.DECK.deal_card()
        self._check_if_ace(card)
        self._cards.append(card)
        self._update_points(card)
        if self._check_if_lost():
            self._points = 0

    def _check_if_ace(self, card: Card) -> None:
        if card.name == "ACE":
            self._aces += 1

    def _check_ace_points(self) -> None:
        while self._aces > 0 and self._check_if_lost():
            self._points -= 10
            self._aces -= 1

    def _check_if_lost(self) -> bool:
        return self._points > 21

    def _update_points(self, card: Card) -> None:
        self._points += card.value
        self._check_ace_points()

    @staticmethod
    def calculate_points(cards: List[Card]) -> int:
        """Calculate the points of the list of cards received as a parameter"""
        return sum([card.value for card in cards])
