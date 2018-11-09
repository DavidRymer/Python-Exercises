def add(num1, num2, modifier):
    if modifier:
        if num1 == 0:
            return num2
        elif num2 == 0:
            return num1
        else:
            return num1 + num2
    else:
        return num1 * num2



