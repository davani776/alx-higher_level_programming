#!/usr/bin/python3
import calculator_1, sys
from sys import argv
def main():
    if (len(argv) == 1 and len(argv) == 2):
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        return (1)
    if argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        return (1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, add()))
        elif argv[2] == "-":
            print("{} + {} = {}".format(a, b, sub()))
        elif argv[2] == "*":
            print("{} + {} = {}".format(a, b, mul()))
        elif argv[2] == "/":
            print("{} + {} = {}".format(a, b, div()))
        return (0)    
if __name__ == "__main__":
    sys.exit(main())
