"""Example usage of the Calculator module."""

from studio_pipeline.calculator import Calculator, Operation


def main():
    """Demonstrate calculator usage with all operations."""
    print("=" * 60)
    print("Calculator Demo - Using Dataclass, Enum, and Abstract Class")
    print("=" * 60)
    print()

    # Create calculator instance
    calc = Calculator()

    # Test addition
    print("1. Addition:")
    result = calc.add(10, 5)
    print(f"   {result}")
    print(f"   Success: {result.success}")
    print()

    # Test subtraction
    print("2. Subtraction:")
    result = calc.subtract(20, 8)
    print(f"   {result}")
    print(f"   Success: {result.success}")
    print()

    # Test multiplication
    print("3. Multiplication:")
    result = calc.multiply(7, 6)
    print(f"   {result}")
    print(f"   Success: {result.success}")
    print()

    # Test division
    print("4. Division:")
    result = calc.divide(100, 4)
    print(f"   {result}")
    print(f"   Success: {result.success}")
    print()

    # Test division by zero (error case)
    print("5. Division by Zero (Error Case):")
    result = calc.divide(10, 0)
    print(f"   {result}")
    print(f"   Success: {result.success}")
    print()

    # Test using enum directly
    print("6. Using Operation Enum:")
    result = calc.calculate(15, 3, Operation.MULTIPLY)
    print(f"   {result}")
    print(f"   Result value: {result.result}")
    print()

    # Show all available operations
    print("7. Available Operations:")
    for op in Operation:
        print(f"   - {op.name}: {op.value}")
    print()

    print("=" * 60)
    print("Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
