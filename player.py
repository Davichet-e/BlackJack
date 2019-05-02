"""
Class created to implement a casino player in Python
Author: David García Morillo
"""


class Player:
    """
    TODO
    """

    def __init__(self, name: str, initial_money: int):
        assert isinstance(name, str) and isinstance(initial_money, int)
        self._name: str = name
        self._initial_money: int = initial_money
        self._actual_money: int = initial_money
        self._actual_bet: int = 0

    def __repr__(self) -> str:
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def initial_money(self) -> int:
        return self._initial_money

    @property
    def actual_money(self) -> int:
        return self._actual_money

    @actual_money.setter
    def actual_money(self, money: int) -> None:
        assert isinstance(money, int)
        self._actual_money = money

    @property
    def actual_bet(self) -> int:
        return self._actual_bet

    @actual_bet.setter
    def actual_bet(self, new_bet: int) -> None:
        assert isinstance(new_bet, int)
        self._actual_bet = new_bet
