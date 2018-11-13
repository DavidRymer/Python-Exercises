import unittest
from IntermediateExercises.PaintWizard.Paint import Paint, CheapoMax, DuluxourousPaints, AverageJoes


class PaintTest(unittest.TestCase):
    def test_waste(self):
        self.assertEqual(CheapoMax().waste(200), 0)
        self.assertEqual(CheapoMax().waste(220), 18.0)
        self.assertEqual(AverageJoes().waste(165), 0)
        self.assertEqual(AverageJoes().waste(247.5), 7.5)
        self.assertEqual(DuluxourousPaints().waste(200), 0)
        self.assertEqual(DuluxourousPaints().waste(300), 5)

    def test_cost(self):
        self.assertEqual(CheapoMax().cost(200), 19.99)
        self.assertEqual(CheapoMax().cost(220), 39.98)
        self.assertEqual(AverageJoes().cost(165), 17.99)
        self.assertEqual(AverageJoes().cost(247.5), 35.98)
        self.assertEqual(DuluxourousPaints().cost(200), 25.0)
        self.assertEqual(DuluxourousPaints().cost(300), 50.0)

    def test_number_of_cans(self):
        self.assertEqual(CheapoMax().number_of_cans(200), 1)
        self.assertEqual(CheapoMax().number_of_cans(220), 2)
        self.assertEqual(AverageJoes().number_of_cans(165), 1)
        self.assertEqual(AverageJoes().number_of_cans(247.5), 2)
        self.assertEqual(DuluxourousPaints().number_of_cans(200), 1)
        self.assertEqual(DuluxourousPaints().number_of_cans(300), 2)



