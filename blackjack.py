"""
TODO
"""
from time import sleep
from typing import List, Optional

from blackjack_player import BlackJackPlayer
from deck import Card
from hand import BlackJackHand


def blackjack() -> None:
    """A multiplayer 21 BlackJack simulator. Just call this function, and enjoy!"""

    check_first_game: bool = True
    players: List[BlackJackPlayer] = []
    dealer: BlackJackHand = BlackJackHand()

    ###########################################################################################

    def initialization() -> None:
        nonlocal check_first_game

        print(
            (
                "\t\t\t\t#########################################"
                "\tGame Started\t   #########################################"
            )
        )
        if check_first_game:
            check_first_game = False
            print(
                "\t\t\t\tThis BlackJack Game has been created by David Garcia Morillo"
            )
            number_of_people: int = ask_number_of_people()
            ask_and_set_player_attributes(number_of_people)
        game()

    def ask_number_of_people() -> int:
        while True:
            try:
                number_of_people = int(
                    input("\t\t\t\tHow many people are going to play? (1-5)\n\t\t\t\t")
                )
            except ValueError:
                print("\t\t\t\tPlease, use only numbers.\n")
            else:
                if not 0 < number_of_people <= 5:
                    print("\t\t\t\tThe number of people must be between 1 and 5\n")
                else:
                    break
        return number_of_people

    def ask_and_set_player_attributes(num_of_people: int) -> None:
        for i in range(num_of_people):
            name: str = input(
                f"\t\t\t\tPlease, enter your name, Player {i + 1!r}\n\t\t\t\t"
            )
            while True:
                try:
                    initial_money = int(
                        input(
                            "\t\t\t\tHow much money do you have? (Use only numbers)\n\t\t\t\t"
                        )
                    )
                except ValueError:
                    print("\t\t\t\tPlease, use only numbers.\n")
                else:
                    if initial_money < 0:
                        print("\t\t\t\tThe initial money must be greater than 0\n")
                    else:
                        players.append(BlackJackPlayer(name, initial_money))
                        break

    ###########################################################################################

    def game() -> None:
        print("\t\t\t\tThe game has started.\n")
        print(f"\t\t\t\tThe first card of the dealer is {dealer.cards[0]!r}")
        for player in players:
            player_turn(player)
        dealer_turn()
        end_game()
        reset()

    ###########################################################################################

    def check_player_bet(player: BlackJackPlayer) -> None:
        while True:
            try:
                bet = int(input("\t\t\t\tWhat bet do you wanna make?\n\t\t\t\t"))
            except ValueError:
                print("\t\t\t\tPlease, use only numbers.\n")
            else:
                if bet > player.actual_money:
                    print(
                        "\t\t\t\tYour bet cannot be greater than your actual money.\n"
                    )
                elif bet <= 0:
                    print("\t\t\t\tYour bet must be greater than 0.\n")
                else:
                    player.actual_bet = bet
                    break

    def player_win_lose_condition(player: BlackJackPlayer) -> Optional[bool]:
        result: bool = None
        if player.points == 21:
            print("\t\t\t\tBLACKJACK")
            result = True
        elif not player.points:
            print("\t\t\t\tBUST.\n\t\t\t\tI'm afraid you lose this game :(\n")
            result = False

        return result

    def show_cards(cards: List[Card]) -> None:
        for card in cards:
            if card != cards[-1]:
                print(card, end=", ")
            else:
                print(card, end=".\n")

    def check_if_yes(user_decision: str) -> bool:
        return (
            user_decision.strip().lower() == "y"
            or user_decision.strip().lower() == "yes"
            or user_decision.strip().lower() == "true"
            or user_decision.strip().lower() == "1"
        )

    def ask_if_hit(player: BlackJackPlayer) -> None:
        for _ in range(21):
            sleep(2)
            if player_win_lose_condition(player) is None:
                decision = input("\t\t\t\tDo you wanna hit? (y/n)\n\t\t\t\t")
                if check_if_yes(decision):
                    player.deal_card()
                    print("\t\t\t\tNow, your cards are:", end=" ")
                    show_cards(player.cards)
                else:
                    print(f"\t\t\t\t{player!r} stanted")
                    break
            else:
                break

    def player_turn(player: BlackJackPlayer) -> None:
        print(
            (
                f"\t\t\t\t#########################################\t{player!r}'s turn"
                "\t   #########################################"
            )
        )
        print(f"\t\t\t\t{player!r}, your actual money is {player.actual_money!r} €\n")

        check_player_bet(player)
        print("\t\t\t\tYour turn has started.\n\t\t\t\tYour cards are: ")
        print(f"\t\t\t\t{player.cards[0]!r} and {player.cards[1]!r}")
        print()
        sleep(1)
        ask_if_hit(player)

    ###########################################################################################

    def dealer_win_lose_condition() -> bool:
        if not dealer.points:
            print("\t\t\t\tThe dealer busted. The game ended :)\n")
            return True
        return False

    def dealer_turn() -> None:
        print(
            (
                "\t\t\t\t#########################################\tDealer's Turn"
                "\t   #########################################"
            )
        )
        sleep(2)
        for _ in range(21):
            sleep(2)
            print("\t\t\t\tThe dealer cards are: ", end="")
            show_cards(dealer.cards)
            if not dealer_win_lose_condition():
                if dealer.points < 17:
                    print("\t\t\t\tThe dealer is going to hit a card\n")
                    dealer.deal_card()
                else:
                    print()
                    break
            else:
                print()
                break

    ###########################################################################################

    def end_game() -> None:
        print(
            (
                "\t\t\t\t#########################################\tResults"
                "\t      ##############################################"
            )
        )
        for player in players:
            if player.points == 21 or player.points > dealer.points:
                player.actual_money += player.actual_bet
                print(f"\t\t\t\t{player!r} won {player.actual_bet * 2!r}€ :)\n")
            # Checks if the player points are 0 or if they are less than the dealer's ones
            elif not player.points or player.points < dealer.points:
                player.actual_money -= player.actual_bet
                print(f"\t\t\t\t{player!r} lost against the dealer :(\n")
            else:
                print(f"\t\t\t\t{player!r}, it is a Tie! :|\n")
        sleep(1)

    def ask_if_reset(player: BlackJackPlayer) -> None:
        player_resets: bool = None
        final_balance: str = f"{player.actual_money - player.initial_money!r} €"
        if "-" not in final_balance:
            final_balance = "+" + final_balance
        if player.actual_money > 0:
            decision: str = input(
                f"\t\t\t\t{player!r}, do you want to play again? (y/n)\n\t\t\t\t"
            )
            if check_if_yes(decision):
                player.initialize_attributes()
                player_resets = True
            else:
                print(
                    (
                        f"\t\t\t\tThanks for playing, {player!r}"
                        f" your final balance is {final_balance}\n"
                    )
                )
                player_resets = False
        else:
            print(
                f"\t\t\t\t{player!r}, you have lost all your money. Thanks for playing\n"
            )
            player_resets = False
        return player_resets

    def reset() -> None:
        print(
            (
                "\t\t\t\t#########################################\tGame Finished"
                "\t   #########################################"
            )
        )
        delete_players: List[BlackJackPlayer] = []
        for player in players:
            if not ask_if_reset(player):
                delete_players.append(player)

        for player_to_delete in delete_players:
            players.remove(player_to_delete)

        print("\n\n\n\n\n")

        if players:
            dealer.initialize_attributes()
            initialization()

    ###########################################################################################

    initialization()


blackjack()
