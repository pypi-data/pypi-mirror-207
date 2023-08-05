"""Stixx game module.

This module contains the Game class and the main function.
To play the game, run this module.


Typical usage example:
    player_1 = Player(input("Player 1 name: ").strip())
    player_2 = Player(input("Player 2 name: ").strip())
    stixx_game = Game(player_1, player_2)
    stixx_game.play()

"""

import players
from players import Player
import random


# TODO: Create is_valid method for Player class to check if the move is valid
# TODO: Add an extra move for the players


class Game:
    """Game class for the Stixx game.

    This class contains the game logic and the game play.

    Attributes:
        player1: The first player.
        player2: The second player.
        current_player: The current player.
        opponent: The opponent of the current player.
        winner: The winner of the game.
    """

    def __init__(self, player1: players.Player, player2: players.Player) -> None:
        """Initialize a new game.

        Args:
            player1: The first player.
            player2: The second player.
        """

        self.player1 = player1
        self.player2 = player2
        self.current_player = self.coin_toss()
        self.opponent = self.player1 if self.current_player == self.player2 else self.player2
        self.winner = None

        self.value = 0
        self.which_hand = None
        self.opponent_hand = None

    def coin_toss(self) -> players.Player:
        """Randomly select who goes first."""
        return random.choice([self.player1, self.player2])

    def is_over(self) -> bool:
        """Check if the game is over."""
        return self.player1.is_both_empty() or self.player2.is_both_empty()

    def get_winner(self) -> None:
        """Get the winner of the game."""
        if self.player1.is_both_empty():
            self.winner = self.player2.name
        elif self.player2.is_both_empty():
            self.winner = self.player1.name

    def valid_input(self, hand: str) -> bool:
        """Check if the hand is valid."""
        if hand != "L" and hand != "R":
            return False
        return True

    def switch_players(self) -> None:
        """Switch players."""
        self.current_player, self.opponent = self.opponent, self.current_player

    def prompt_dialog(self, which_dialog: str) -> None:
        """Print the dialog of the game.

        Args:
            which_dialog: The dialog to print.
        """

        LINE = "-" * 80
        if which_dialog == "start":
            print(LINE + f"\n{self.current_player.name} goes first!")

        elif which_dialog == "turn":
            line_1 = f"\n{self.current_player.name} it's your turn!"
            line_2 = f"\nYour current hand is: {self.current_player.current_hand()}"
            line_3 = f"\n{self.opponent.name}'s hand is: {self.opponent.current_hand()}\n"
            dialog = LINE + line_1 + line_2 + line_3
            print(dialog)

        elif which_dialog == "over":
            self.get_winner()

            line_1 = "\nGame over!" + f"\n{self.winner} wins!\n"
            line_2 = "\nFinal Hands: "
            line_3 = f"\n{self.player1.name}: {self.player1.current_hand()}"
            line_4 = f"\n{self.player2.name}: {self.player2.current_hand()}\n"

            dialog = LINE.replace("-", "*") + line_1 + line_2 + line_3 + line_4 + LINE.replace("-", "*")
            print(dialog)

        elif which_dialog == "invalid":
            line_1 = "\nInvalid input!\nPlease type \"R\" or \"L\""
            line_2 = f"\nYour current hand is: {self.current_player.current_hand()}"
            line_3 = f"\n{self.opponent.name}'s hand is: {self.opponent.current_hand()}\n"

            dialog = LINE + line_1 + line_2 + line_3
            print(dialog)

        elif which_dialog == "empty":
            line_1 = "\nHand is empty!\nPlease try again."
            line_2 = f"\nYour current hand is: {self.current_player.current_hand()}"
            line_3 = f"\n{self.opponent.name}'s hand is: {self.opponent.current_hand()}\n"

            dialog = LINE + line_1 + line_2 + line_3
            print(dialog)

    def select_hand(self) -> None:
        """Get the move of the current player."""
        while True:
            self.which_hand = input("Which hand? (L/R): ").strip().upper()
            if not self.valid_input(self.which_hand):
                self.prompt_dialog("invalid")
            elif self.current_player.is_empty(self.which_hand):
                self.prompt_dialog("empty")
            else:
                if self.which_hand == "L":
                    self.value = self.current_player.left
                else:
                    self.value = self.current_player.right
                break

    def select_hand_opponent(self) -> None:
        """Select the opponent's hand."""
        while True:
            self.opponent_hand = input("Which opponent's hand? (L/R): ").strip().upper()
            if not self.valid_input(self.opponent_hand):
                self.prompt_dialog("invalid")
            elif self.opponent.is_empty(self.opponent_hand):
                self.prompt_dialog("empty")
            else:
                self.opponent.update(self.opponent_hand, self.value)
                break

    def play(self) -> None:
        """Play the game"""

        # Print the start dialog
        self.prompt_dialog("start")

        # Play the game
        while True:
            # Print the dialog of the game
            self.prompt_dialog("turn")

            # Current player select hand
            self.select_hand()

            # Current player select opponent's hand
            self.select_hand_opponent()

            # Check if the game is over
            if self.is_over():
                self.prompt_dialog("over")
                break

            # Switch players
            self.switch_players()


if __name__ == "__main__":
    player_1 = Player(input("Player 1 name: ").strip())
    player_2 = Player(input("Player 2 name: ").strip())
    stixx_game = Game(player_1, player_2)
    stixx_game.play()
