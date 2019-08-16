"""
Class created to implement a BlackJack player in Python
Author: David García Morillo
"""
from hand import Hand


class Player:
    """This class implements a BlackJack player in python"""

    def __init__(self, name: str, initial_money: int):
        if not isinstance(name, str):
            raise ValueError("Must assign to a string value")

        if not isinstance(initial_money, int):
            raise ValueError("Must assign to a integer value")

        self._hand: Hand = Hand()

        self._name: str = name
        self._initial_money: int = initial_money
        self._actual_money: int = initial_money
        self._actual_bet: int

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f"Player(name={self._name}, initial money={self._initial_money}"

    @property
    def hand(self) -> Hand:
        return self._hand

    @property
    def name(self) -> str:
        return self._name

    @property
    def initial_money(self) -> int:
        return self._initial_money

    @property
    def actual_money(self) -> int:
        return self._actual_money

    @actual_money.setter
    def actual_money(self, money: int) -> None:
        if not isinstance(money, int):
            raise ValueError("Must assign to a integer value")

        self._actual_money = money

    @property
    def actual_bet(self) -> int:
        return self._actual_bet

    @actual_bet.setter
    def actual_bet(self, new_bet: int) -> None:
        if not isinstance(new_bet, int):
            raise ValueError("Must assign to a integer value")

        self._actual_bet = new_bet
