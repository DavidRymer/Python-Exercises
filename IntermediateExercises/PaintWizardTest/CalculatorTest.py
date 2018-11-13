import unittest
import IntermediateExercises.PaintWizard.Calculator
from IntermediateExercises.PaintWizard.Wall import Wall


class CalculatorTest(unittest.TestCase):
    def test_total_area(self):
        walls = [Wall(5, 10), Wall(3, 10)]
        self.assertEqual(IntermediateExercises.PaintWizard.Calculator.total_area(walls), 80)

    def test_least_waste(self):
        walls = [Wall(5, 10), Wall(3, 10), Wall(4, 30)]
        self.assertEqual(IntermediateExercises.PaintWizard.Calculator.least_waste(walls), "Cheapo Max")

    def test_least_cost(self):
        walls = [Wall(5, 10), Wall(3, 10), Wall(5, 17)]
        self.assertEqual(IntermediateExercises.PaintWizard.Calculator.least_cost(walls), "Average Joe's")


