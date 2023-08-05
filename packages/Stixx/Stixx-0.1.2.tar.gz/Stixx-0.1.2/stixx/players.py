""" Player Class for Stixx Game.

This module contains the Player class for the Stixx game.
It is used by the Game class to keep track of the players'
names, scores, and actions.

Example:
    player = Player("Foo")
    player.update("L", 2)
    player.current_hand()
    player.is_empty("L")
    player.is_both_empty()
"""


class Player:
    """Player class for Stixx game.

    This class is used to keep track of the players' names,
    scores, and actions.

    Attributes:
        name: The name of the player.
        left: The number of sticks in the player's left hand.
        right: The number of sticks in the player's right hand.
    """

    def __init__(self, name: str) -> None:
        """Initialize the player's name and score.

        Args:
            name: The name of the player.
        """

        self.name = name
        self.left = 1
        self.right = 1

    def is_both_empty(self) -> bool:
        """Check if player's hands are empty."""
        return self.left == 0 and self.right == 0

    def current_hand(self) -> str:
        """Return the current hand."""
        return f"{self.left} {self.right}"

    def update(self, hand: str, value: int) -> None:
        """Update the player's hand."""
        if hand == "L":
            if (self.left + value) % 5 != 0:
                self.left = (self.left + value) % 5
            else:
                self.left = 0
        else:
            if (self.right + value) % 5 != 0:
                self.right = (self.right + value) % 5
            else:
                self.right = 0

    def is_empty(self, hand: str) -> bool:
        """Check if the hand is empty."""
        if hand == "L":
            return self.left == 0
        else:
            return self.right == 0
