class Wall:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def surface_area(self):
        return self.height * self.width

