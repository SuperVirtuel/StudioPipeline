"""Calculator module with dataclass, enum, and abstract class."""

from .calculator import Calculator
from .operations import Operation
from .result import CalculationResult

__all__ = ["Calculator", "Operation", "CalculationResult"]
