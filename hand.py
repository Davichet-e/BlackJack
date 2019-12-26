"""
Author: David García Morillo
"""
from typing import List, Optional

from deck import Card, Deck


class Hand:
    """Represent a 21 BlackJack hand.

    :param: `deck` -> `Deck` where to get the cards
    
    :param: `from_cards` -> If given, create a `Hand` based on those cards."""

    def __init__(self, deck: Deck, *, from_cards: Optional[List[Card]] = None) -> None:
        self._deck = deck

        if from_cards:
            self._cards: List[Card] = from_cards

        else:
            self._cards = self._deck.get_initial_cards()

        self._points: int = Hand.calculate_points(self._cards)
        self._aces = 0
        for card in self._cards:
            self._check_if_ace(card)
        self._check_ace_points()

    def __repr__(self) -> str:
        cards_as_str: List[str] = [f"{card}" for card in self._cards]
        points: int = self._points
        return (
            f"{', '.join(cards_as_str)}. ({points if points != 0 else '> 21'} points)"
        )

    @property
    def cards(self) -> List[Card]:
        return self._cards

    @property
    def points(self) -> int:
        return self._points

    def initialize_attributes(self) -> None:
        """Resets all the attributes of the instance"""
        self.__init__(self._deck)

    def deal_card(self) -> None:
        """Deal a card of the deck and add it to the list of cards"""
        card: Card = self._deck.deal_card()
        self._cards.append(card)

        self._check_if_ace(card)
        self._update_points()

        if self._points > 21:
            self._points = 0

    def has_blackjack(self) -> bool:
        """Return whether the Hand has a blackjack or not"""
        return len(self._cards) == 2 and self._points == 21

    def _check_if_ace(self, card: Card) -> None:
        if card.name == "ACE":
            self._aces += 1

    def _check_ace_points(self) -> None:
        while self._aces > 0 and self._points > 21:
            self._points -= 10
            self._aces -= 1

    def _update_points(self) -> None:
        self._points = Hand.calculate_points(self.cards)
        self._check_ace_points()

    @staticmethod
    def calculate_points(cards: List[Card]) -> int:
        """Calculate the points of the list of cards received as a parameter"""
        return sum([card.value for card in cards])
