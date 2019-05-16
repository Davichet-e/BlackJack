"""
Class created to implement a casino player in Python
Author: David García Morillo
"""


class Player:
    """
    This class implements a casino player in python\n
    
    Parameters
    ----------
    name: str\n
    initial_money: int
    """

    def __init__(self, name: str, initial_money: int):
        assert isinstance(name, str), "The type of 'name' must be str"
        assert isinstance(initial_money, int), "The type of 'initial_money' must be int"
        self._name: str = name
        self._initial_money: int = initial_money
        self._actual_money: int = initial_money
        self._actual_bet: int

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return (
            f"Player(name={self._name}, initial money={self._initial_money}, "
            f"actual money={self._actual_money}, actual bet={self._actual_bet})"
        )

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
        assert isinstance(money, int)
        self._actual_money = money

    @property
    def actual_bet(self) -> int:
        return self._actual_bet

    @actual_bet.setter
    def actual_bet(self, new_bet: int) -> None:
        assert isinstance(new_bet, int)
        self._actual_bet = new_bet
