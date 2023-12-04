# my_project/utilities.py
from importlib import import_module
import subprocess
import argparse

def dynamic_module_call(module_name, *args):
    try:
        module = import_module(f"my_project.{module_name}")
        return module.calculate(*args)
    except ImportError:
        raise ImportError(f"Module '{module_name}' not found.")

def get_argparse_help(module_name):
    try:
        # Run the script with a dummy argument to capture the argparse help message
        result = subprocess.check_output(['python', '-m', f"my_project.{module_name}", '--help'])
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Utility script runner.")
    parser.add_argument('module_name', type=str, help='Name of the utility module.')
    parser.add_argument('arguments', type=int, nargs='*', help='Additional arguments.')
    args = parser.parse_args()

    # Example usage of dynamic_module_call
    try:
        if '--help' in args.module_name:
            # Display help message only if --help is explicitly provided
            help_message = get_argparse_help(args.module_name)
            print(help_message)
        else:
            result = dynamic_module_call(args.module_name, *args.arguments)
            print(f"Result from dynamic_module_call: {result}")
    except ImportError as e:
        print(f"ImportError: {str(e)}")

if __name__ == "__main__":
    main()
