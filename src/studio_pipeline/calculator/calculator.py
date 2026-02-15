"""Main Calculator class."""

from typing import Dict

from .base import (
    AdditionHandler,
    DivisionHandler,
    MultiplicationHandler,
    OperationHandler,
    SubtractionHandler,
)
from .operations import Operation
from .result import CalculationResult


class Calculator:
    """
    Main calculator class that performs mathematical operations.

    This calculator uses the Strategy pattern with abstract operation handlers
    to perform different types of calculations.

    Example:
        >>> from studio_pipeline.calculator import Calculator, Operation
        >>> calc = Calculator()
        >>> result = calc.calculate(10, 5, Operation.ADD)
        >>> print(result)
        10 add 5 = 15.0
    """

    def __init__(self):
        """Initialize the calculator with operation handlers."""
        self._handlers: Dict[Operation, OperationHandler] = {
            Operation.ADD: AdditionHandler(),
            Operation.SUBTRACT: SubtractionHandler(),
            Operation.MULTIPLY: MultiplicationHandler(),
            Operation.DIVIDE: DivisionHandler(),
        }

    def calculate(self, a: float, b: float, operation: Operation) -> CalculationResult:
        """
        Perform a calculation.

        Args:
            a: First operand
            b: Second operand
            operation: The operation to perform

        Returns:
            A CalculationResult containing the result or error

        Example:
            >>> calc = Calculator()
            >>> result = calc.calculate(10, 2, Operation.DIVIDE)
            >>> print(result.result)
            5.0
        """
        handler = self._handlers.get(operation)

        if handler is None:
            return CalculationResult(
                operation=operation,
                operand1=a,
                operand2=b,
                error=f"Unknown operation: {operation}",
            )

        try:
            result = handler.calculate(a, b)
            return CalculationResult(
                operation=operation,
                operand1=a,
                operand2=b,
                result=result,
            )
        except Exception as e:
            return CalculationResult(
                operation=operation,
                operand1=a,
                operand2=b,
                error=str(e),
            )

    def add(self, a: float, b: float) -> CalculationResult:
        """Convenience method for addition."""
        return self.calculate(a, b, Operation.ADD)

    def subtract(self, a: float, b: float) -> CalculationResult:
        """Convenience method for subtraction."""
        return self.calculate(a, b, Operation.SUBTRACT)

    def multiply(self, a: float, b: float) -> CalculationResult:
        """Convenience method for multiplication."""
        return self.calculate(a, b, Operation.MULTIPLY)

    def divide(self, a: float, b: float) -> CalculationResult:
        """Convenience method for division."""
        return self.calculate(a, b, Operation.DIVIDE)
