def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_gen():
    for i in range(2, 100):
        if is_prime(i):
            yield i

print("Prime numbers upt to 100:")
print(list(prime_gen()))
