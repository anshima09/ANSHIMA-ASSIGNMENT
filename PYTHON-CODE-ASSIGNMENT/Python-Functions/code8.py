def variable_sum(*args):
    return sum(args)

tuple_values=(1,2,3,4,5)
print("The sum of the tuple values is: ", variable_sum(*tuple_values))