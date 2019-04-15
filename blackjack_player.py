'''
Author: David García Morillo
'''
from player import Player
from hand import BlackJackHand


class BlackJackPlayer(Player, BlackJackHand):
    """
    TODO
    """
    def __init__(self, name: str, initial_money: int):
        Player.__init__(self, name, initial_money)
        BlackJackHand.__init__(self)
