def too_hot(temperature, isSummer):
    if isSummer and 60 < temperature < 100:
        return True
    elif not isSummer and 60 < temperature < 90:
        return True
    else:
        return False

