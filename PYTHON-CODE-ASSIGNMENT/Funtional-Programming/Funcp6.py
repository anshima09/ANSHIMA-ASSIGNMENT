def curried_sum(x):
    def add_y(y):
        def add_z(z):
            return x + y + z
        return add_z
    return add_y

result = curried_sum(1)(2)(3)

print("Curried Sum Result:", result)
