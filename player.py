"""
Class created to implement a casino player in Python
Author: David García Morillo
"""


class Player:
    """
    TODO
    """

    def __init__(self, name: str, initialMoney: int):
        assert isinstance(name, str) and isinstance(initialMoney, int)
        self._name: str = name
        self._initialMoney: str = initialMoney
        self._actualMoney: int = initialMoney
        self._actualBet: int = 0

    def __repr__(self) -> str:
        return self._name

    @property
    def initial_money(self) -> int:
        return self._initialMoney

    @property
    def actual_money(self) -> int:
        return self._actualMoney

    @actual_money.setter
    def actual_money(self, money: int) -> None:
        assert isinstance(money, int)
        self._actualMoney = money

    @property
    def actual_bet(self) -> int:
        return self._actualBet

    @actual_bet.setter
    def actual_bet(self, new_bet: int) -> None:
        assert isinstance(new_bet, int)
        self._actualBet = new_bet
