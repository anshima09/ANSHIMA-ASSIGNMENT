def is_strong_password(pwd):
    if len(pwd) < 8:
        return False
    has_upper = any(char.isupper() for char in pwd)
    has_lower = any(char.islower() for char in pwd)
    has_digit = any(char.isdigit() for char in pwd)
    has_special = any(char in "!@#$%^&*()-_+=" for char in pwd)
    return has_upper and has_lower and has_digit and has_special


str=input("Enter a password to check if its's strong: ")
print(is_strong_password(str)) 