import unittest
from IntermediateExercises.PaintWizard.Wall import Wall


class WallTest(unittest.TestCase):
    def test_surface_area(self):
        wall = Wall(5, 10)
        self.assertEqual(wall.surface_area(), 50)
