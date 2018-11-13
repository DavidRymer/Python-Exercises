from IntermediateExercises.PaintWizard.Paint import Paint, CheapoMax, DuluxourousPaints, AverageJoes


def total_area(walls):
    total = 0
    for x in walls:
        total += x.surface_area()
    return total


def least_waste_or_cost(walls, func):
    area = total_area(walls)
    amount_of_waste = {
        "Cheapo Max": func(CheapoMax(), area),
        "Average Joe's": func(AverageJoes(), area),
        "Deluxourious Paint": func(DuluxourousPaints(), area)
    }

    return min(amount_of_waste, key=lambda k: amount_of_waste[k])


def least_waste(walls):
    return least_waste_or_cost(walls, Paint.waste)


def least_cost(walls):
    return least_waste_or_cost(walls, Paint.cost)
