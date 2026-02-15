"""Abstract base class for calculator operations."""

from abc import ABC, abstractmethod


class OperationHandler(ABC):
    """
    Abstract base class for handling calculator operations.

    This class defines the interface that all operation handlers must implement.
    """

    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        """
        Perform the calculation.

        Args:
            a: First operand
            b: Second operand

        Returns:
            The result of the calculation

        Raises:
            ValueError: If the operation cannot be performed
        """
        pass

    @abstractmethod
    def get_operation_name(self) -> str:
        """
        Get the name of the operation.

        Returns:
            The name of the operation
        """
        pass


class AdditionHandler(OperationHandler):
    """Handler for addition operations."""

    def calculate(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def get_operation_name(self) -> str:
        """Get operation name."""
        return "add"


class SubtractionHandler(OperationHandler):
    """Handler for subtraction operations."""

    def calculate(self, a: float, b: float) -> float:
        """Subtract two numbers."""
        return a - b

    def get_operation_name(self) -> str:
        """Get operation name."""
        return "subtract"


class MultiplicationHandler(OperationHandler):
    """Handler for multiplication operations."""

    def calculate(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def get_operation_name(self) -> str:
        """Get operation name."""
        return "multiply"


class DivisionHandler(OperationHandler):
    """Handler for division operations."""

    def calculate(self, a: float, b: float) -> float:
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def get_operation_name(self) -> str:
        """Get operation name."""
        return "divide"
