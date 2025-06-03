def nested_try():
    try:
        x = int("100")
        try:
            y = 10 / 0
        except ZeroDivisionError:
            print("Inner block: Division by zero error")
    except ValueError:
        print("Outer block: Value error")

nested_try()
