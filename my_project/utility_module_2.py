# my_project/utility_module_2.py
import argparse

def calculate_product(*args):
    result = 1
    for num in args:
        result *= num
    return result

def main():
    parser = argparse.ArgumentParser(description="Calculate the product of numbers.")
    parser.add_argument('numbers', type=float, nargs='+', help='Numbers to multiply.')
    args = parser.parse_args()
    result = calculate_product(*args.numbers)
    print(result)

if __name__ == "__main__":
    main()
