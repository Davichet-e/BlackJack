"""
This module implements the standard 52-card deck and its correspondents cards
Author: David García Morillo
"""

from random import shuffle
from typing import Dict, List, Tuple, NamedTuple


class Card(NamedTuple):
    """This class implements the cards of the standard 52-card deck"""

    name: str
    value: int
    suit: str

    def __str__(self) -> str:
        return f"{self.name} of {self.suit}"


class Deck:
    """This class implements the standard 52-card deck"""

    _SUITS: Tuple[str, ...] = ("♣", "♥", "♠", "♦")
    _CARDS: Dict[str, int] = dict(
        ACE=11,
        TWO=2,
        THREE=3,
        FOUR=4,
        FIVE=5,
        SIX=6,
        SEVEN=7,
        EIGHT=8,
        NINE=9,
        TEN=10,
        JACK=10,
        QUEEN=10,
        KING=10,
    )

    def __init__(self):
        self._deck: List[Card] = [
            Card(card_name, card_value, suit)
            for suit in self._SUITS
            for card_name, card_value in self._CARDS.items()
        ]
        shuffle(self._deck)

    def __str__(self) -> str:
        cards_repr: str = "\n".join([f"{card}" for card in self._deck])
        return f"Deck cards:\n\n{cards_repr}"

    def __repr__(self) -> str:
        return f"Deck(deck={self._deck})"

    def __len__(self):
        return len(self._deck)

    def __getitem__(self, position: int) -> Card:
        return self._deck[position]

    @property
    def suits(self) -> Tuple[str, ...]:
        """Returns the suits of the deck"""
        return self._SUITS

    @property
    def cards(self) -> Dict[str, int]:
        """Returns a dictionary with the cards and its correspondant values"""
        return self._CARDS

    def deal_card(self) -> Card:
        """Returns a random card of the deck."""
        card: Card = self._deck.pop()
        return card

    def get_initial_cards(self) -> List[Card]:
        """Returns 2 random cards of the deck"""
        initial_cards: List[Card] = [self._deck.pop(), self._deck.pop()]
        return initial_cards

    @staticmethod
    def sum_points(cards: List[Card]) -> int:
        """Sum the points of the list of cards which are received as a parameter"""
        return sum([card.value for card in cards])
