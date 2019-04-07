from deck import Deck, Card

myDeck = Deck()

class Player():
    def __init__(self, name: str, initialMoney: int):
        self.__name = name
        self.__initialMoney = initialMoney
        self.__actualMoney = initialMoney
        self.__cards = myDeck.get_initial_cards()
        self.__points = Deck.sum_points(self.__cards)
        self.__actualBet = 0
        self.__aces = 0
        for card in self.__cards:
            self.__count_aces(card)

    def __str__(self) -> str:
        return self.__name

    def get_initial_money(self) -> int:
        return self.__initialMoney

    def get_actual_money(self) -> int:
        return self.__actualMoney

    def update_actual_money(self, money: int):
        self.__actualMoney += money

    def get_cards(self) -> list:
        return self.__cards

    def reset_cards(self):
        self.__cards.clear()
        self.__cards = myDeck.get_initial_cards()
        self.__points = Deck.sum_points(self.__cards)
    
    def __count_aces(self, card: Card):
        if card.get_name() == "ACE":
            self.__aces += 1

    def __check_ace_points(self):
        while self.__points > 21 and self.__aces:
            self.__points -= 10
            self.__aces -= 1

    def update_points(self):
        self.__points = Deck.sum_points(self.__cards)
        self.__check_ace_points()

    def deal_card(self):
        card = myDeck.deal_card()
        self.__count_aces(card)
        self.__cards.append(card)
        self.update_points()

    def loser_points(self):
        self.__points = 0

    def get_points(self) -> int:
        return self.__points

    def get_actual_bet(self) -> int:
        return self.__actualBet

    def set_actual_bet(self, newBet: int):
        self.__actualBet = newBet


def get_my_Deck() -> Deck:
    return myDeck
