# my_project/utility_module_1.py
import argparse

def calculate_sum(*args):
    return sum(args)

def main():
    parser = argparse.ArgumentParser(description="Calculate the sum of numbers.")
    parser.add_argument('numbers', type=float, nargs='+', help='Numbers to sum.')
    args = parser.parse_args()
    result = calculate_sum(*args.numbers)
    print(result)

if __name__ == "__main__":
    main()
