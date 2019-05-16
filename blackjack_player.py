"""
Author: David García Morillo
"""
from hand import BlackJackHand
from player import Player


class BlackJackPlayer(Player, BlackJackHand):
    """This class uses the 'Player' and 'BlackJackHand' classes 
    to create a BlackJack player model in python.\n

    Parameters
    ----------
    name: str\n
    initial_money: int
    """

    def __init__(self, name: str, initial_money: int):
        Player.__init__(self, name, initial_money)
        BlackJackHand.__init__(self)

    @property
    def hand(self):
        return BlackJackHand.__repr__(self)
