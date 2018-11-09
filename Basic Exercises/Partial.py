from functools import partial


def multiply(x, y):
    return x*y


double = partial(multiply, 2)
triple = partial(multiply, 3)

print(double(4))
print(triple(7))
