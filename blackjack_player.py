"""
Author: David García Morillo
"""
from hand import BlackJackHand
from player import Player


class BlackJackPlayer(Player, BlackJackHand):
    """
    TODO
    """

    def __init__(self, name: str, initial_money: int):
        assert isinstance(name, str), "The type of 'name' must be str"
        assert isinstance(initial_money, int), "The type of 'initial_money' must be str"
        Player.__init__(self, name, initial_money)
        BlackJackHand.__init__(self)
