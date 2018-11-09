def add(num1, num2, modifier):
    if modifier:
        return num1 + num2
    else:
        return num1 * num2


print(add(3, 3, True))
print(add(3, 3, False))
