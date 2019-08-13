"""
The 21 BlackJack now in python!
"""
from time import sleep
from typing import List

from blackjack_player import BlackJackPlayer
from blackjack_hand import BlackJackHand

###########################################################################################


players: List[BlackJackPlayer] = []
dealer_hand: BlackJackHand = BlackJackHand()


###########################################################################################


def blackjack() -> None:
    """A multiplayer 21 BlackJack simulator. Just call this function, and enjoy!"""

    start_game()
    while True:
        print(
            (
                "\t\t\t\t#########################################"
                "\tGame Started\t   #########################################"
            )
        )

        print(f"\t\t\t\tThe first card of the dealer is {dealer_hand.cards[0]}")

        for player in players:
            player_turn(player)

        dealer_turn()
        end_game()
        if not next_game():
            break


###########################################################################################


def start_game() -> None:
    """Starts the game"""
    print("\t\t\t\tThis BlackJack Game has been created by David Garcia Morillo")
    number_of_people: int = ask_number_of_people()
    ask_and_set_player_attributes(number_of_people)


def ask_number_of_people() -> int:
    """Ask how many people it is going to start playing the game"""
    while True:
        try:
            number_of_people: int = int(
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
    """Ask the players their names and initial money and
    pass them to the 'BlackJackPlayer' class"""
    for i in range(num_of_people):
        name: str = input(f"\t\t\t\tPlease, enter your name, Player {i + 1}\n\t\t\t\t")
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

                if initial_money < 50:
                    print(
                        "\t\t\t\tThe initial money must be greater or equal than 50\n"
                    )
                else:
                    players.append(BlackJackPlayer(name, initial_money))
                    break


def ask_player_bet(player: BlackJackPlayer) -> None:
    """Ask the player received as paramater what bet does he/she wanna make"""
    while True:
        try:
            bet = int(input("\t\t\t\tWhat bet do you wanna make?\n\t\t\t\t"))

        except ValueError:
            print("\t\t\t\tPlease, use only numbers.\n")

        else:
            if bet > player.actual_money:
                print("\t\t\t\tYour bet cannot be greater than your actual money.\n")

            elif bet <= 0:
                print("\t\t\t\tYour bet must be greater than 0.\n")

            else:
                player.actual_bet = bet
                break


def player_win_or_lose(player: BlackJackPlayer) -> bool:
    """Checks if the player received as paramater won or lost"""
    result: bool = False
    player_points: int = player.hand.points

    if player_points == 21:
        print("\t\t\t\tBLACKJACK")
        result = True

    elif player_points == 0:
        print("\t\t\t\tBUST.\n\t\t\t\tI'm afraid you lose this game :(\n")
        result = True

    return result


def check_if_yes(user_decision: str) -> bool:
    """Checks if the player decision is affirmative"""
    return user_decision.strip().lower() in {"y", "yes", "1", "true"}


def ask_if_hit() -> bool:
    """Ask the player if he/she wants to hit"""
    sleep(2)
    decision = input("\t\t\t\tDo you wanna hit? (y/n)\n\t\t\t\t")
    return check_if_yes(decision)


def player_turn(player: BlackJackPlayer) -> None:
    """Reproduce the player which receive as parameter turn"""
    print(
        (
            f"\t\t\t\t#########################################\t{player}'s turn"
            "\t   #########################################"
        )
    )
    print(f"\t\t\t\t{player}, your actual money is {player.actual_money} €\n")

    ask_player_bet(player)

    print("\t\t\t\tYour cards are: ")
    print(f"\t\t\t\t{player.hand.cards[0]} and {player.hand.cards[1]}")
    print()
    sleep(1)
    while not player_win_or_lose(player):
        hit: bool = ask_if_hit()
        if hit:
            player.hand.deal_card()
            print(f"\t\t\t\tNow, your cards are: {player.hand}")
            sleep(1)

        else:
            print(f"\t\t\t\t{player} stood\n")
            break


def dealer_lost() -> bool:
    """Check if the dealer lost"""
    if dealer_hand.points == 0:
        print("\t\t\t\tThe dealer busted. The game ended :)\n")
        return True
    return False


def dealer_turn() -> None:
    """Reproduce the dealer turn"""
    print(
        (
            "\t\t\t\t#########################################\tDealer's Turn"
            "\t   #########################################"
        )
    )
    sleep(2)
    print(
        f"\t\t\t\tThe dealer's cards are {dealer_hand.cards[0]} and {dealer_hand.cards[1]}\n"
    )

    while not dealer_lost() and dealer_hand.points < 17:
        sleep(2)
        print("\t\t\t\tThe dealer is going to hit a card\n")
        dealer_hand.deal_card()
        sleep(1)
        print(f"\t\t\t\tNow, the dealer's cards are: {dealer_hand}")


def end_game() -> None:
    """Checks which player wins or loses, and manage their money according to that"""
    print(
        (
            "\t\t\t\t#########################################\tResults"
            "\t      ##############################################"
        )
    )
    dealer_points: int = dealer_hand.points

    for player in players:
        player_points: int = player.hand.points

        if player_points == 21 or player_points > dealer_points:
            player.actual_money += player.actual_bet
            print(f"\t\t\t\t{player} won {player.actual_bet * 2}€ :)\n")
        # Checks if the player points are 0 or if they are less than the dealer's ones
        elif not player_points or player_points < dealer_points:
            player.actual_money -= player.actual_bet
            print(f"\t\t\t\t{player} lost against the dealer :(\n")

        else:
            print(f"\t\t\t\t{player}, it is a tie! :|\n")
    sleep(1)


def ask_if_next_game(player: BlackJackPlayer) -> bool:
    """Ask a player if he/she wants to play another game"""
    player_next_game: bool = False
    final_balance: str = f"{player.actual_money - player.initial_money} €"
    # Check if 'final_balance' is negative, if not, adds a '+' sign
    if "-" not in final_balance:
        final_balance = "+" + final_balance

    if player.actual_money > 0:
        decision: str = input(
            f"\t\t\t\t{player}, do you want to play again? (y/n)\n\t\t\t\t"
        )

        if check_if_yes(decision):
            player.hand.initialize_attributes()
            player_next_game = True

        else:
            print(
                (
                    f"\t\t\t\tThanks for playing, {player}"
                    f" your final balance is {final_balance}\n"
                )
            )

    else:
        print(f"\t\t\t\t{player}, you have lost all your money. Thanks for playing\n")

    return player_next_game


def next_game() -> bool:
    """Check if there are players for a next game"""
    global players

    print(
        (
            "\t\t\t\t#########################################\tGame Finished"
            "\t   #########################################"
        )
    )

    players = [player for player in players if ask_if_next_game(player)]

    print("\n\n\n\n\n")

    if players:
        dealer_hand.initialize_attributes()
        return True

    return False


if __name__ == "__main__":
    blackjack()
