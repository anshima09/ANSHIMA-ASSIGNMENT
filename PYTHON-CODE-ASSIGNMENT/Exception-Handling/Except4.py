class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120")
    else:
        print("Valid age:", age)


age=int(input("Enter your age:"))
try:
    validate_age(age)
except InvalidAgeError as e:
    print("Caught exception:", e)
