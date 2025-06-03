def get_integer():
    try:
        num = int(input("Enter an integer: "))
        print("You entered:", num)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

get_integer()
