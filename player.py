"""
Class created to implement a casino player in Python
Author: David García Morillo
"""


class Player():
    """
        TODO
    """

    def __init__(self, name: str, initialMoney: int):
        self.__name = name
        self.__initialMoney = initialMoney
        self.__actualMoney = initialMoney
        self.__actualBet = 0

    def __str__(self) -> str:
        return self.__name

    def get_initial_money(self) -> int:
        return self.__initialMoney

    def get_actual_money(self) -> int:
        return self.__actualMoney

    def update_actual_money(self, money: int):
        self.__actualMoney += money

    def get_actual_bet(self) -> int:
        return self.__actualBet

    def set_actual_bet(self, newBet: int):
        self.__actualBet = newBet
