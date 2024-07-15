import unittest
from backend.colors import Color, check_range
import typing
import random
from parameterized import parameterized


class TestColorsManager(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.color_manager = Color()

    def setUp(self):
        random.seed(1)


    def test_zero(self):
        """
        Test availability of a zero constant in Color class
        """
        self.assertEqual(self.color_manager.zero, (0, 0, 0, 0), 'Zero variable is\'t right')


    def test_random_return_type(self):
        """
        Test type of return of random color function
        """
        random_color = self.color_manager.random()
        self.assertEqual(type(random_color), tuple, 'Return isn\'t tuple')
    
    @parameterized.expand([
        ['range_0_255', [0,255], [0,255], [0,255], [0,255]],
        ['range_wrong', [-1,255], [0,256], [-1,256], [-256,255]]
    ])
    def test_random(self, name, r_range, g_range, b_range, a_range):
        """
        Test return of random color function with different wrong ranges
        """
        self.assertEqual(
            self.color_manager.random(r_range, g_range, b_range, a_range),
            (68, 32, 130, 60),
            'Color elements are not right or not of type int'
            )

    def test_random_overlap(self):
        """
        Test return of random color function with overlaping range
        """
        self.assertEqual(
            self.color_manager.random([0,255], [15,12], [0,255], [0,255]),
            (68, 12, 130, 60),
            'Can\'t handle range elements overlaping'
            )
    
    def test_random_limited(self):
        """
        Test return of random color function with limited range
        """
        self.assertEqual(
            self.color_manager.random([0,0], [255,255], [32,32], [0,0]),
            (0, 255, 32, 0)
        )
    

    @parameterized.expand([
        ['0_to_255', [0, 255]],
        ['min_1_to_255', [-1, 255]],
        ['0_to_258', [0, 258]],
        ['min_255_to_256', [-255, 256]]
    ])
    def test_check_range(self, name, range_):
        """
        Test check_range function for out of bounds ranges
        """
        self.assertEqual(check_range(range_), [0, 255], 'Out of bounds check isn\'t right')

    def test_check_range_equal(self):
        """
        Test check_range function for equal bounds in range
        """
        self.assertEqual(check_range([12, 12]), [12, 12], 'Equal bounds check isn\'t right')

    def test_check_range_plain(self):
        """
        Test check_range function for normal range
        """
        self.assertEqual(check_range([3, 250]), [3, 250], 'Plain check isn\'t right')

    def test_check_range_overlap(self):
        """
        Test check_range function for overlaping range boundaries
        """
        self.assertEqual(check_range([14, 12]), [12, 12], 'Overlap check isn\'t right')


if __name__ == "__main__":
    unittest.main()
