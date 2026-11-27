# Name: Humaun Ahmed
# QCC ID: YOUR_QCC_ID
#humaun's own function's unittest by humaun in case anyone unabailable 
 
import unittest
from my_math import factorial, volume_of_sphere, sqrt, area_of_circle


class TestFactorial(unittest.TestCase):

    def test_factorial_positive_number(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-3)

class TestVolumeOfSphere(unittest.TestCase):

    def test_volume_normal_radius(self):
        self.assertAlmostEqual(volume_of_sphere(3), 113.09733552923254)

    def test_volume_zero_radius(self):
        self.assertEqual(volume_of_sphere(0), 0)

    def test_volume_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_of_sphere(-2)

class TestSqrt(unittest.TestCase):

    def test_sqrt_positive(self):
        self.assertEqual(sqrt(25), 5)

    def test_sqrt_zero(self):
        self.assertEqual(sqrt(0), 0)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-4)

    def test_sqrt_invalid_type(self):
        with self.assertRaises(TypeError):
            sqrt("hello")


class TestAreaOfCircle(unittest.TestCase):

    def test_area_normal_radius(self):
        self.assertAlmostEqual(area_of_circle(3), 28.2743338823)

    def test_area_zero_radius(self):
        self.assertEqual(area_of_circle(0), 0)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area_of_circle(-3)

    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            area_of_circle("hello")

if __name__ == "__main__":
    unittest.main()


# Name: Kenn [Last Name]
# QCC ID: KENN_QCC_ID

# Name: Kerby [Last Name]
# QCC ID: KERBY_QCC_ID

