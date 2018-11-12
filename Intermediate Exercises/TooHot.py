def too_hot(temperature, is_summer):
    if is_summer and 60 < temperature < 100:
        return True
    elif not is_summer and 60 < temperature < 90:
        return True
    else:
        return False

