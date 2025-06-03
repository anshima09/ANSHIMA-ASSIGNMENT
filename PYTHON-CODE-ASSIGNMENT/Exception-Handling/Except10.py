class TooYoungError(Exception): pass
class TooOldError(Exception): pass

def check_age(age):
    if age < 18:
        raise TooYoungError("Too young to proceed.")
    elif age > 60:
        raise TooOldError("Too old to proceed.")
    else:
        print("Age is appropriate.")


age=int(input("Enter your age: "))
try:
    check_age(age)
except TooYoungError as e:
    print(e)
except TooOldError as e:
    print(e)
