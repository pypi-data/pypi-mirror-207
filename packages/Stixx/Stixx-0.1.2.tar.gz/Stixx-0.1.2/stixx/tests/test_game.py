from players import Player
from game import Game
import os
import sys
import unittest
from unittest.mock import patch
import io


sys.path.insert(0, os.path.abspath('..'))

LINE = "-" * 80


class TestGame(unittest.TestCase):
    def tearUp(self):
        player1 = Player("Bob")
        player2 = Player("Sue")
        self.game = Game(player1, player2)
        # self.game.play()

    def test_is_over_player1(self):
        self.tearUp()
        player1 = self.game.player1
        player2 = self.game.player2
        player2.left = 0
        player2.right = 0
        self.assertTrue(self.game.is_over())

    def test_is_over_player2(self):
        self.tearUp()
        player1 = self.game.player1
        player2 = self.game.player2
        player1.left = 0
        player1.right = 0
        self.assertTrue(self.game.is_over())

    def test__init__(self):
        self.tearUp()
        self.assertEqual(self.game.player1.name, "Bob")
        self.assertEqual(self.game.player2.name, "Sue")
        self.assertEqual(self.game.winner, None)

    def test_get_winner(self):
        self.tearUp()
        player1 = self.game.player1
        player2 = self.game.player2
        player2.left = 0
        player2.right = 0
        self.game.get_winner()
        self.assertEqual(self.game.winner, "Bob")

        self.tearDown()
        self.tearUp()
        player1 = self.game.player1
        player2 = self.game.player2
        player1.left = 0
        player1.right = 0
        self.game.get_winner()
        self.assertEqual(self.game.winner, "Sue")

    def test_valid_input(self):
        self.tearUp()
        self.assertTrue(self.game.valid_input("L"))
        self.assertTrue(self.game.valid_input("R"))
        self.assertFalse(self.game.valid_input("A"))
        self.assertFalse(self.game.valid_input("B"))

    def test_coin_toss(self):
        self.tearUp()
        self.game.coin_toss()
        self.assertTrue(self.game.current_player.name == "Bob" or self.game.current_player.name == "Sue")

    def test_switch_players(self):
        self.tearUp()
        current_player = self.game.current_player
        other_player = self.game.opponent

        self.game.switch_players()
        self.assertEqual(self.game.current_player, other_player)
        self.assertEqual(self.game.opponent, current_player)

    def test_prompt_dialog_start(self):
        self.tearUp()

        # TEST START DIALOG
        test_dialog = LINE + f"\n{self.game.current_player.name} goes first!"

        output = io.StringIO()
        sys.stdout = output
        self.game.prompt_dialog("start")
        dialog = output.getvalue().strip()
        sys.stdout = sys.__stdout__
        self.assertEqual(dialog, test_dialog)

    def test_prompt_dialog_turn(self):
        self.tearUp()
        turn_line_1 = f"\n{self.game.current_player.name} it's your turn!"
        turn_line_2 = f"\nYour current hand is: {self.game.current_player.current_hand()}"
        turn_line_3 = f"\n{self.game.opponent.name}'s hand is: {self.game.opponent.current_hand()}\n"

        test_dialog = LINE + turn_line_1 + turn_line_2 + turn_line_3
        output = io.StringIO()
        sys.stdout = output
        self.game.prompt_dialog("turn")
        dialog = output.getvalue().strip() + "\n"
        sys.stdout = sys.__stdout__
        self.assertEqual(dialog, test_dialog)

    def test_prompt_dialog_over(self):
        self.tearUp()
        self.game.get_winner()
        print(self.game.winner)
        over_line_1 = "\nGame over!" + f"\n{self.game.winner} wins!\n"
        over_line_2 = "\nFinal Hands: "
        over_line_3 = f"\n{self.game.player1.name}: {self.game.player1.current_hand()}"
        over_line_4 = f"\n{self.game.player2.name}: {self.game.player2.current_hand()}\n"

        test_dialog = (
            LINE.replace("-", "*") + over_line_1 + over_line_2 + over_line_3 + over_line_4 + LINE.replace("-", "*")
        )

        output = io.StringIO()
        sys.stdout = output
        self.game.prompt_dialog("over")
        dialog = output.getvalue().strip()
        sys.stdout = sys.__stdout__
        self.assertEqual(dialog, test_dialog)

    def test_prompt_dialog_invalid(self):
        self.tearUp()

        line_1 = "\nInvalid input!\nPlease type \"R\" or \"L\""
        line_2 = f"\nYour current hand is: {self.game.current_player.current_hand()}"
        line_3 = f"\n{self.game.opponent.name}'s hand is: {self.game.opponent.current_hand()}\n"

        test_dialog = LINE + line_1 + line_2 + line_3

        output = io.StringIO()
        sys.stdout = output
        self.game.prompt_dialog("invalid")
        dialog = output.getvalue().strip() + "\n"
        sys.stdout = sys.__stdout__
        self.assertEqual(dialog, test_dialog)

    def test_prompt_dialog_empty(self):
        self.tearUp()

        line_1 = "\nHand is empty!\nPlease try again."
        line_2 = f"\nYour current hand is: {self.game.current_player.current_hand()}"
        line_3 = f"\n{self.game.opponent.name}'s hand is: {self.game.opponent.current_hand()}\n"

        test_dialog = LINE + line_1 + line_2 + line_3

        output = io.StringIO()
        sys.stdout = output
        self.game.prompt_dialog("empty")
        dialog = output.getvalue().strip() + "\n"
        sys.stdout = sys.__stdout__
        self.assertEqual(dialog, test_dialog)

    ###############################################################################
    @patch("builtins.input", return_value="L")
    def test_select_hand_opponent(self, mock_input):
        self.tearUp()

        test_dialog = "\n"
        output = io.StringIO()
        sys.stdout = output
        self.game.select_hand_opponent()
        dialog = output.getvalue().strip() + "\n"
        sys.stdout = sys.__stdout__
        self.assertEqual(dialog, test_dialog)

    @patch("builtins.input", return_value="L")
    def test_select_hand(self, mock_input):
        self.tearUp()

        test_dialog = "\n"
        output = io.StringIO()
        sys.stdout = output
        self.game.select_hand()
        dialog = output.getvalue().strip() + "\n"
        sys.stdout = sys.__stdout__
        self.assertEqual(dialog, test_dialog)

    ###############################################################################
    # SELECT HAND OPPONENT TESTS

    @patch("builtins.input", return_value="L")
    def test_select_hand_opponent_left(self, mock_input):
        self.tearUp()
        test_value = self.game.current_player.left

        output = io.StringIO()
        sys.stdout = output
        self.game.select_hand_opponent()
        sys.stdout = sys.__stdout__

        assert self.game.current_player.left == test_value

    @patch("builtins.input", return_value="R")
    def test_select_hand_opponent_right(self, mock_input):
        self.tearUp()

        output = io.StringIO()
        sys.stdout = output
        self.game.select_hand_opponent()
        sys.stdout = sys.__stdout__

        test_value = self.game.current_player.right
        assert self.game.current_player.right == test_value

    ###############################################################################
    # SELECT HAND
    @patch("builtins.input", return_value="L")
    def test_select_hand_left(self, mock_input):
        self.tearUp()
        test_value = self.game.current_player.left

        output = io.StringIO()
        sys.stdout = output
        self.game.select_hand()
        sys.stdout = sys.__stdout__

        assert self.game.current_player.left == test_value

    @patch("builtins.input", return_value="R")
    def test_select_hand_right(self, mock_input):
        self.tearUp()

        output = io.StringIO()
        sys.stdout = output
        self.game.select_hand()
        sys.stdout = sys.__stdout__

        if self.game.which_hand != "L":
            test_value = self.game.current_player.right

        assert self.game.value == test_value

    ###############################################################################
    @patch("builtins.input", return_value="x", side_effect=["L", "R"])
    def test_select_hand_invalid(self, mock_input):
        self.tearUp()
        test_dialog = "\n"

        output = io.StringIO()
        sys.stdout = output
        self.game.select_hand()
        dialog = output.getvalue().strip() + "\n"
        sys.stdout = sys.__stdout__

        self.assertEqual(dialog, test_dialog)

    @patch("builtins.input", return_value="x", side_effect=["L", "R"])
    def test_select_hand_opponent_invalid(self, mock_input):
        self.tearUp()
        test_dialog = "\n"

        output = io.StringIO()
        sys.stdout = output
        self.game.select_hand_opponent()
        dialog = output.getvalue().strip() + "\n"
        sys.stdout = sys.__stdout__

        self.assertEqual(dialog, test_dialog)
