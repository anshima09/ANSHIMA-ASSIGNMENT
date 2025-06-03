def memoized_fibonacci():
    memo = {}

    def fib(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]

    return fib

fib = memoized_fibonacci()
print(fib(30))