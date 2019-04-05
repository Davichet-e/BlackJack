from Deck import Deck, Card

myDeck = Deck()


class Player():
    def __init__(self, name, initialMoney):
        self.__name = name
        self.__initialMoney = initialMoney
        self.__actualMoney = initialMoney
        self.__cards = myDeck.get_initial_cards()
        self.__points = Deck.sum_points(self.__cards)
        self.__actualBet = 0

    def __str__(self):
        return self.__name

    def get_initial_money(self):
        return self.__initialMoney

    def get_actual_money(self):
        return self.__actualMoney

    def update_actual_money(self, money):
        self.__actualMoney += money

    def get_cards(self):
        return self.__cards

    def reset_cards(self):
        self.__cards.clear()
        self.__cards = myDeck.get_initial_cards()
        self.__points = Deck.sum_points(self.__cards)

    def check_ace(self):
        for card in self.__cards:
            if card.get_name() == "ACE":
                if self.__points > 21:
                    self.__points -= 10

    def update_points(self):
        self.__points = Deck.sum_points(self.__cards)
        self.check_ace()

    def deal_card(self):
        self.__cards.append(myDeck.deal_card())
        self.update_points()

    def loser_points(self):
        self.__points = 0

    def get_points(self):
        return self.__points

    def get_actual_bet(self):
        return self.__actualBet

    def set_actual_bet(self, newBet):
        self.__actualBet = newBet


def get_my_Deck():
    return myDeck
