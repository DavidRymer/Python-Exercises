import math


def pi_function(n):
    a = range(2, n + 1)
    b, c = [], a
    while c[0] < math.sqrt(n):
        first_element= c[0]
        b += [first_element]
        c = [x for x in c if x % first_element != 0]
    return len(b+c)


print(pi_function(20000000))