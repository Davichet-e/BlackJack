"""
This module implements the standard 52-card deck and its correspondents cards
Author: David García Morillo
"""

import random
from typing import ClassVar, Dict, List, NamedTuple, Tuple


class Card(NamedTuple):
    """Implement a playing card"""

    name: str
    suit: str

    def __str__(self) -> str:
        return f"{self.name} of {self.suit}"

    @property
    def value(self) -> int:
        return Deck.CARDS[self.name]


class Deck:
    """Implement the standard 52-card deck.

    The number of cards that contains is defined
    by 52 times the `n_decks` parameter"""

    SUITS: ClassVar[Tuple[str, ...]] = ("♣", "♥", "♠", "♦")
    CARDS: ClassVar[Dict[str, int]] = dict(
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

    def __init__(self, n_decks: int):
        self._deck: List[Card] = [
            Card(card_name, suit)
            for suit in Deck.SUITS
            for card_name in Deck.CARDS
            for _ in range(n_decks)
        ]
        random.shuffle(self._deck)

    def __len__(self):
        return len(self._deck)

    def __getitem__(self, position: int) -> Card:
        return self._deck[position]

    def deal_card(self) -> Card:
        """Returns a random card of the deck."""
        # If the deck is empty, initialize it
        if not self._deck:
            raise ValueError("The deck is empty. GAME OVER.")
        return self._deck.pop()

    def get_initial_cards(self) -> List[Card]:
        """Returns 2 random cards of the deck"""
        return [self._deck.pop(), self._deck.pop()]
