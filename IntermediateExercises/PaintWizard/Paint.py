import math
from abc import ABC


class Paint(ABC):
    def __init__(self, volume, price, area_per_litre):
        self.volume = volume
        self.price = price
        self.area_per_litre = area_per_litre

    def number_of_cans(self, total_area):
        number_of_cans = total_area/(self.volume * self.area_per_litre)

        if total_area % (self.volume * self.area_per_litre) > 0:
            return math.floor(number_of_cans) + 1
        else:
            return number_of_cans

    def waste(self, total_area):

        return self.number_of_cans(total_area) * self.volume - (total_area/self.area_per_litre)

    def cost(self, total_area):

        return self.number_of_cans(total_area) * self.price


class CheapoMax(Paint):
    def __init__(self):
        Paint.__init__(self, 20, 19.99, 10)


class AverageJoes(Paint):
    def __init__(self):
        Paint.__init__(self, 15, 17.99, 11)


class DuluxourousPaints(Paint):
    def __init__(self):
        Paint.__init__(self, 10, 25.0, 20)


a = Paint(33, 33, 33)
print(a.volume)
