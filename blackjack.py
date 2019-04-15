'''
The 21 BlackJack, now in Python.
Author: David García Morillo
'''
from time import sleep

from blackjack_player import BlackJackPlayer
from hand import BlackJackHand


def blackjack():
    """A multiplayer 21 BlackJack simulator. Just call this function, and enjoy!"""

    check_first_game = True
    players = []
    dealer = BlackJackHand()

    #---------------------------------------------------------------------------------#
    def initialization():
        nonlocal check_first_game

        print(
            "\t\t\t\t#########################################\tGame Started\t   \
#########################################")
        if check_first_game:
            check_first_game = False
            print(
                "\t\t\t\tThis BlackJack Game has been created by David Garcia Morillo"
            )
            number_of_people = ask_number_of_people()
            ask_player_attributes(number_of_people)
        game()

    def ask_number_of_people() -> int:
        while True:
            try:
                number_of_people = int(
                    input(
                        "\t\t\t\tHow many people are going to play? (1-5)\n\t\t\t\t"
                    ))
            except ValueError:
                print("\t\t\t\tPlease, use only numbers.\n")
            else:
                if not 0 < number_of_people <= 5:
                    print(
                        "\t\t\t\tThe number of people must be between 1 and 5\n"
                    )
                    continue
                break
        return number_of_people

    def ask_player_attributes(num_of_people: int):
        for i in range(num_of_people):
            name = input(
                f"\t\t\t\tPlease, enter your name, Player {str(i + 1)}\n\t\t\t\t"
            )
            while True:
                try:
                    initial_money = int(
                        input(
                            "\t\t\t\tHow much money do you have? (Use only numbers)\n\t\t\t\t"
                        ))
                except ValueError:
                    print("\t\t\t\tPlease, use only numbers.\n")
                else:
                    if initial_money < 0:
                        print(
                            "\t\t\t\tThe initial money must be greater than 0\n"
                        )
                        continue
                    players.append(BlackJackPlayer(name, initial_money))
                    break

    def game():
        print("\t\t\t\tThe game has started.\n")
        print(
            f"\t\t\t\tThe first card of the dealer is {str(dealer.get_cards()[0])}"
        )
        for player in players:
            player_turn(player)
        dealer_turn()
        end_game()
        reset()

    def check_player_bet(player: BlackJackPlayer):
        while True:
            try:
                bet = int(
                    input("\t\t\t\tWhat bet do you wanna make?\n\t\t\t\t"))
            except ValueError:
                print("\t\t\t\tPlease, use only numbers.\n")
            else:
                if bet > player.get_actual_money():
                    print(
                        "\t\t\t\tYour bet cannot be greater than your actual money.\n"
                    )
                elif bet <= 0:
                    print("\t\t\t\tYour bet must be greater than 0.\n")
                else:
                    player.set_actual_bet(bet)
                    break

    def player_win_lose_condition(player: BlackJackPlayer) -> bool:
        result = None
        if player.get_points() == 21:
            print("\t\t\t\tBLACKJACK")
            result = True
        elif not player.get_points():
            print("\t\t\t\tBUST.\n\t\t\t\tI'm afraid you lose this game :(\n")
            result = False

        return result

    def show_player_cards(player: BlackJackPlayer):
        print("\t\t\t\tNow, your cards are:", end=" ")
        player_cards = player.get_cards()
        for card in player_cards:
            if player_cards[-1] != card:  # While the card is not the last,
                print(card, end=", ")  # separate them with comas,
            else:  # otherwise, print the final point
                print(card, end=".\n")  # and a jumpline.

    def check_if_yes(user_decision: str) -> bool:
        return user_decision.strip().lower() == "y"\
            or user_decision.strip().lower() == "yes"\
            or user_decision.strip().lower() == "true"\
            or user_decision.strip().lower() == "1"

    def ask_if_hit(player: BlackJackPlayer):
        for _ in range(21):
            sleep(2)
            if player_win_lose_condition(player) is None:
                decision = input("\t\t\t\tDo you wanna hit? (y/n)\n\t\t\t\t")
                if check_if_yes(decision):
                    player.deal_card()
                    show_player_cards(player)
                else:
                    print(f"\t\t\t\t{str(player)} stanted")
                    break
            else:
                break

    def player_turn(player: BlackJackPlayer):
        print(
            f"\t\t\t\t#########################################\t{str(player)}'s turn\t   \
#########################################")
        print(
            f"\t\t\t\t{str(player)}, your actual money is {str(player.get_actual_money())} €\n"
        )

        check_player_bet(player)
        print("\t\t\t\tYour turn has started.\n\t\t\t\tYour cards are: ")
        print(
            f"\t\t\t\t{str(player.get_cards()[0])} and {str(player.get_cards()[1])}"
        )
        print()
        sleep(1)
        ask_if_hit(player)

    def dealer_win_lose_condition() -> bool:
        if not dealer.get_points():
            print("\t\t\t\tThe dealer busted. The game ended :)\n")
            return True
        return False

    def show_dealer_cards():
        print("\t\t\t\tThe dealer cards are: ", end="")
        dealer_cards = dealer.get_cards()
        for card in dealer_cards:
            if dealer_cards[-1] != card:
                print(card, end=", ")
            else:
                print(card, end=".\n")

    def dealer_turn():
        print(
            "\t\t\t\t#########################################\tDealer's Turn\t   \
#########################################")
        sleep(2)
        for _ in range(21):
            sleep(2)
            show_dealer_cards()
            if not dealer_win_lose_condition():
                if dealer.get_points() < 17:
                    print("\t\t\t\tThe dealer is going to hit a card\n")
                    dealer.deal_card()
                else:
                    print()
                    break
            else:
                print()
                break

    def end_game():
        print(
            "\t\t\t\t#########################################\tResults\t      \
##############################################")
        for player in players:
            if player.get_points() == 21\
                    or player.get_points() > dealer.get_points():
                player.update_actual_money(player.get_actual_bet())
                print(
                    f"\t\t\t\t{str(player)} won {str(player.get_actual_bet() * 2)}€ :)\n"
                )
            elif not player.get_points()\
                or player.get_points() < dealer.get_points():        # Checks if the player's points are 0 
                player.update_actual_money(-player.get_actual_bet()) # or if they are less than the dealer's points  
                print(f"\t\t\t\t{str(player)} lost against the dealer :(\n")
            else:
                print(f"\t\t\t\t{str(player)}, it is a Tie! :|\n")
        sleep(1)

    def ask_if_reset(player: BlackJackPlayer):
        player_reset: bool = None
        final_balance = f"{str(player.get_actual_money() - player.get_initial_money())} €"
        if "-" not in final_balance:
            final_balance = "+" + final_balance
        if player.get_actual_money() > 0:
            decision = input(
                f"\t\t\t\t{str(player)}, do you want to play again? (y/n)\n\t\t\t\t"
            )
            if check_if_yes(decision):
                player.reset_cards()
                player_reset = True
            else:
                print(f"\t\t\t\tThanks for playing, {str(player)}\
 your final balance is {final_balance}\n")
                player_reset = False
        else:
            print(
                f"\t\t\t\t{str(player)}, you have lost all your money. Thanks for playing\n"
            )
            player_reset = False
        return player_reset

    def reset():
        print(
            "\t\t\t\t#########################################\tGame Finished\t   \
#########################################")
        delete_players = []
        for player in players:
            if not ask_if_reset(player):
                delete_players.append(player)

        for player_to_delete in delete_players:
            players.remove(player_to_delete)

        print("\n\n\n\n\n")

        if players:
            dealer.reset_cards()
            initialization()

    #---------------------------------------------------------------------------------#

    initialization()


blackjack()
