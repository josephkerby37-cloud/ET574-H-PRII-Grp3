# Name: Humaun Ahmed
# QCC ID: YOUR_QCC_ID
#humaun's own function's unittest by humaun in case anyone unabailable 
 
import unittest
from my_math import factorial
from my_math import volume_of_sphere


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

if __name__ == "__main__":
    unittest.main()


# Name: Kerby [Last Name]
# QCC ID: KERBY_QCC_ID

# Name: Kenn [Last Name]
# QCC ID: KENN_QCC_ID