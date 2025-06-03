import argparse

parser = argparse.ArgumentParser(description="Simple CLI Calculator")
parser.add_argument("num1", type=float)
parser.add_argument("operator", choices=["+", "-", "*", "/"])
parser.add_argument("num2", type=float)

args = parser.parse_args()

if args.operator == "+":
    print(args.num1 + args.num2)
elif args.operator == "-":
    print(args.num1 - args.num2)
elif args.operator == "*":
    print(args.num1 * args.num2)
elif args.operator == "/":
    if args.num2 != 0:
        print(args.num1 / args.num2)
    else:
        print("Error: Division by zero")