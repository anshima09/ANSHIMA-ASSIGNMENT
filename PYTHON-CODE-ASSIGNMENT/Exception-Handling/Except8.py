def convert_input(data):
    try:
        return int(data)
    except ValueError as e:
        raise RuntimeError("Conversion failed") from e

try:
    convert_input("abc")
except RuntimeError as e:
    print("Caught exception:", e)
