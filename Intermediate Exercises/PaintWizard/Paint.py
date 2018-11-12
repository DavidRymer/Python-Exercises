import math


class Paint(object):
    def __init__(self, volume, price, area_per_litre):
        self.volume = volume
        self.price = price
        self.area_per_litre = area_per_litre

    def waste(self, total_area):

        if total_area % self.area_per_litre == 0:
            return 0
        else:
            return self.volume

    def cost(self, total_area):

        number_of_cans = total_area/(self.volume * self.area_per_litre)

        if total_area % (self.volume * self.area_per_litre) > 0:
            return math.floor(number_of_cans)*self.price + self.price
        else:
            return number_of_cans * self.price


class CheapoMax(Paint):
    def __init__(self):
        Paint.__init__(self, 20, 19.99, 10)


class AverageJoes(Paint):
    def __init__(self):
        Paint.__init__(self, 15, 17.99, 11)


class DuluxourousPaints(Paint):
    def __init__(self):
        Paint.__init__(self, 10, 25.0, 20)


