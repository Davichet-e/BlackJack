"""
Author: David García Morillo
"""


from blackjack_hand import BlackJackHand
from player import Player


class BlackJackPlayer(Player):
    """This class uses the 'Player' and 'BlackJackHand' classes 
    to create a BlackJack player model in python.
    """

    def __init__(self, name: str, initial_money: int):
        Player.__init__(self, name, initial_money)
        self._hand: BlackJackHand = BlackJackHand()

    @property
    def hand(self) -> BlackJackHand:
        return self._hand
