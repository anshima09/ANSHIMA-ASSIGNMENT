def exception_logger(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            with open("decorator_log.txt", "a") as f:
                f.write(f"Error in {func.__name__}: {e}\n")
            print("An error occurred. Check the log.")
    return wrapper

@exception_logger
def risky_division(x, y):
    return x / y

risky_division(10, 0)
