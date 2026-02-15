"""Dataclass for calculation results."""

from dataclasses import dataclass
from typing import Optional

from .operations import Operation


@dataclass
class CalculationResult:
    """
    Dataclass representing the result of a calculation.

    Attributes:
        operation: The operation performed
        operand1: First operand
        operand2: Second operand
        result: The calculation result
        error: Optional error message if calculation failed
    """

    operation: Operation
    operand1: float
    operand2: float
    result: Optional[float] = None
    error: Optional[str] = None

    @property
    def success(self) -> bool:
        """Check if the calculation was successful."""
        return self.error is None

    def __str__(self) -> str:
        """String representation of the calculation result."""
        if self.success:
            op_val = self.operation.value
            return f"{self.operand1} {op_val} {self.operand2} = {self.result}"
        else:
            return f"Error: {self.error}"
