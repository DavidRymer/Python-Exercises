def unique_sum(n1, n2, n3):

    numbers = [n1, n2, n3]

    for x in numbers:
        if numbers.count(x) > 1:
            while numbers.count(x) > 0:
                numbers.remove(x)

    return sum(numbers)


print(unique_sum(1, 2, 3))
print(unique_sum(3, 3, 3))
print(unique_sum(1, 1, 2))
