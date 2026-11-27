import unittest
from my_math import factorial, volume_of_sphere, sqrt, area_of_circle

class TestMyMath(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_volume_of_sphere(self):
        self.assertAlmostEqual(volume_of_sphere(1), 4.1887902048)
        self.assertEqual(volume_of_sphere(0), 0)

    def test_sqrt(self):
        self.assertEqual(sqrt(25), 5)
        self.assertEqual(sqrt(0), 0)

    def test_area_of_circle(self):
        self.assertAlmostEqual(area_of_circle(2), 12.5663706144)
        self.assertEqual(area_of_circle(0), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
