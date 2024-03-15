#!/usr/bin/python3
import calculator_1
import sys
def main():
    if len(sys.argv) != 4:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        return 1

    if argv[2]  == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif argv[2] == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    elif argv[2] == '/':
        if b == 0:
            print("Error: Division by zero!")
            return 1
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
        return 0
if __name__ == "__main__":
    sys.exit(main())

