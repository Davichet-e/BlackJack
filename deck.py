"""
This module implements the standard 52-card deck and its correspondents cards
"""

from random import shuffle


class Card():
    """This class implements the cards of the standard 52-card deck"""

    def __init__(self, name: str, suit: str, value: int):
        self.__name = name
        self.__suit = suit
        self.__value = value

    def __str__(self):
        return f"{self.__name} of {self.__suit}"

    def get_name(self) -> str:
        """Returns the name of the card"""
        return self.__name

    def get_value(self) -> int:
        """Returns the value of the card"""
        return self.__value

    def get_suit(self) -> str:
        """Returns the suit of the card"""
        return self.__suit


class Deck():
    '''This class implements the standard 52-card deck'''

    SUITS = ("♣", "♥", "♠", "♦")
    __CARDS = dict(ACE=11,
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
                   KING=10)
    #A copy of the cards, created for prevent a player to change or add any element
    PUBLIC_CARDS = __CARDS.copy()

    def __init__(self):
        self.__deck = []
        for suit in self.SUITS:
            for card in self.__CARDS.items():
                self.__deck.append(Card(card[0], suit, card[1]))
        shuffle(self.__deck)

    def __str__(self):
        cards_repr = ""
        for card in self.__deck:
            cards_repr += f"\n{card.__str__()}"
        return f"Deck cards:\n{cards_repr}"

    def __len__(self):
        return len(self.__deck)

    def deal_card(self) -> Card:
        """Returns a random card of the deck."""
        top = self.__deck[0]
        self.__deck.remove(top)
        return top

    def get_initial_cards(self) -> list:
        """Returns 2 random cards of the deck"""
        initial_cards = self.__deck[0:2]
        for i in initial_cards:
            self.__deck.remove(i)
        return initial_cards

    @staticmethod
    def sum_points(cards: list) -> int:
        """Sum the points of the list of cards which are received as a parameter"""
        points = 0
        for card in cards:
            points += card.get_value()
        return points
