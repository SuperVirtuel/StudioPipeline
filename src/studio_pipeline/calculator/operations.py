"""Enum for calculator operations."""

from enum import Enum


class Operation(Enum):
    """
    Enum representing different mathematical operations.

    Attributes:
        ADD: Addition operation
        SUBTRACT: Subtraction operation
        MULTIPLY: Multiplication operation
        DIVIDE: Division operation
    """

    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"

    def __str__(self):
        """String representation of the operation."""
        return self.value
