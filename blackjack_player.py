'''
Author: David García Morillo
'''
from deck import Card, Deck
from player import Player

my_deck = Deck()


class BlackJackPlayer(Player):

    def __init__(self, name: str, initial_money: int):
        super().__init__(name, initial_money)
        self.__cards = my_deck.get_initial_cards()
        self.__points = Deck.sum_points(self.__cards)
        self.__aces = 0
        for card in self.__cards:
            self.__count_aces(card)
        self.__check_ace_points()

    def get_cards(self) -> list:
        return self.__cards

    def reset_cards(self):
        self.__cards.clear()
        self.__aces = 0
        self.__cards = my_deck.get_initial_cards()
        for card in self.__cards:
            self.__count_aces(card)
        self.__points = Deck.sum_points(self.__cards)

    def __count_aces(self, card: Card):
        if card.get_name() == "ACE":
            self.__aces += 1

    def __check_ace_points(self):
        while self.__points > 21 and self.__aces:
            self.__points -= 10
            self.__aces -= 1

    def __check_if_lose(self):
        if self.__points > 21:
            self.__points = 0

    def __update_points(self, card: Card):
        self.__points += card.get_value()
        self.__check_ace_points()

    def deal_card(self):
        card = my_deck.deal_card()
        self.__count_aces(card)
        self.__cards.append(card)
        self.__update_points(card)
        self.__check_if_lose()

    def loser_points(self):
        self.__points = 0

    def get_points(self) -> int:
        return self.__points


def get_my_deck() -> Deck:
    return my_deck
