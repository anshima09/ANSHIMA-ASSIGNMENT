import importlib

module_name = input("Enter module name to import (e.g., math): ")
function_name = input("Enter function name (e.g., sqrt): ")

try:
    mod = importlib.import_module(module_name)
    func = getattr(mod, function_name)
    arg = float(input("Enter a number: "))
    print("Result:", func(arg))
except (ImportError, AttributeError):
    print("Module or function not found.")