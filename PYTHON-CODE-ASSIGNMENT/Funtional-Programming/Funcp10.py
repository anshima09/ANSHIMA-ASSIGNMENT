def compose(*funcs):
    def composed(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return composed

add2 = lambda x: x + 2
times3 = lambda x: x * 3

composed_func = compose(add2, times3)  # (x * 3) + 2
print("Composed Result after performing the function:", composed_func(4))  # (4 * 3) + 2 = 14
