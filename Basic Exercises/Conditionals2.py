def add(num1, num2, modifier):
    if modifier:
        if num1 == 0:
            return num2
        elif num2 == 0:
            return num1
        else:
            return num1 + num2
    else:
        if num1 == 0:
            return num2
        elif num2 == 0:
            return num1
        else:
            return num1 * num2


print(add(3, 0, True))
print(add(3, 3, False))
