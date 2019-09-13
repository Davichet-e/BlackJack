"""
Class created to implement a BlackJack player in Python
Author: David García Morillo
"""
from hand import Hand
from deck import Deck, Card
from typing import List, Optional, Tuple


class Player:
    """This class implements a BlackJack player in python"""

    def __init__(self, name: str, initial_money: int, deck: Deck):
        if not isinstance(name, str):
            raise ValueError("Parameter `name` must be a string value")

        if not isinstance(initial_money, int):
            raise ValueError("Parameter `initial_money` must be a integer value")

        self._deck = deck
        self._hands: List[Hand] = [Hand(self._deck)]

        self._name: str = name
        self._initial_money: int = initial_money
        self._actual_money: int = initial_money
        self._actual_bet: int = 0

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f"Player(name={self._name}, initial money={self._initial_money}"

    @property
    def hands(self) -> List[Hand]:
        return self._hands

    @property
    def name(self) -> str:
        return self._name

    @property
    def initial_money(self) -> int:
        return self._initial_money

    @property
    def actual_money(self) -> int:
        return self._actual_money

    @property
    def actual_bet(self) -> int:
        return self._actual_bet

    @actual_bet.setter
    def actual_bet(self, new_bet: int) -> None:
        if not isinstance(new_bet, int):
            raise ValueError("Must assign to a integer value")

        self._actual_bet = new_bet

    def reset_hands(self) -> None:
        for hand in self._hands:
            hand.initialize_attributes()

    def hit(self, hand_index: int) -> None:
        """TODO"""
        self._hands[hand_index].deal_card()

    def double(self) -> Optional[str]:
        """TODO"""
        error_message: Optional[str] = None
        if self.actual_bet * 2 > self.actual_money:
            error_message = "Cannot double because you have not enough money!"
        elif len(self._hands[0].cards) != 2:
            error_message = "Cannot double because you have already hit!"
        elif len(self._hands) == 2:
            error_message = "Cannot double because you have already splitted!"
        else:
            self._actual_bet *= 2

        return error_message

    def surrender(self) -> Optional[str]:
        """TODO"""
        error_message: Optional[str] = None
        if len(self.hands[0].cards) != 2:
            error_message = "Cannot surrender because you have already hit!"
        elif len(self.hands) == 2:
            error_message = "Cannot surrender because you have already splitted!"
        else:
            self.actual_bet /= 2
            self.hands[0]._points = 0
        return error_message

    def split(self) -> Optional[str]:
        """TODO"""
        error_message: Optional[str] = None

        first_hand_cards: List[Card] = self.hands[0].cards
        if self.actual_bet * 2 > self.actual_money:
            error_message = "Cannot split because you have not enough money!"

        elif len(self.hands) == 2:
            error_message = "Cannot split because you have already splitted!"

        elif len(first_hand_cards) != 2:
            error_message = "Cannot split because you have already hit!"

        elif first_hand_cards[0].name != first_hand_cards[1].name:
            error_message = "Cannot split because your cards are not the same!"

        else:
            self.actual_bet *= 2

            cards: List[Card] = [first_hand_cards.pop(), self._deck.deal_card()]
            self._hands.append(Hand(deck=self._deck, from_cards=cards))

            first_hand_cards.deal_card()

        return error_message

    def win(self) -> int:
        """Update the money with the earnings and returns them"""
        earnings: int = self._actual_bet

        # If it has a blackjack, the earnings increments 1.5 times
        for hand in self._hands:
            if hand.has_blackjack():
                earnings *= 1.5

        self._actual_money += earnings
        return earnings

    def lose(self) -> None:
        """Update the money substracting the actual bet"""
        self._actual_money -= self._actual_bet

