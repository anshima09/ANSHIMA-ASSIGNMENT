def format_currency(number):
    return "{:,}".format(number)


num=int(input("Enter a number to format as currency: "))
print("Formatted currency: ",format_currency(num))