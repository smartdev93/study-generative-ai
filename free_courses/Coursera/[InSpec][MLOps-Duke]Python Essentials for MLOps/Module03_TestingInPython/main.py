import argparse
import sys

from calculator import Calculator

def parse_args():
    parser = argparse.ArgumentParser(
        description = "A simple CLI for Calculator (add, subtract, multiply, divide)"
    )
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="Which arithmtic operation to perform"
    )
    parser.add_argument(
        "a", type=float, help="First operand (a number)"
    )
    parser.add_argument(
        "b", type=float, help="Second operand number (b number)"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    calc = Calculator()

    if args.operation == "add":
        result = calc.add(args.a, args.b)
    elif args.operation == "subtract":
        result = calc.subtract(args.a, args.b)
    elif args.operation == "multiply":
        result = calc.multiply(args.a, args.b)
    elif args.operation == "divide":
        result = calc.divide(args.a, args.b)
    else:
        print(f"Unknown operation: {args.operation}", file=sys.stderr)
        sys.exit(1)

    print(result)

if __name__ == "__main__":
    main()