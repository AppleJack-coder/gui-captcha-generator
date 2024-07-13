import unittest
from backend.colors import Color
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
        self.assertEqual(self.color_manager.zero, (0, 0, 0, 0), 'Zero variable is\'t right')


    def test_random_return_type(self):
        random_color = self.color_manager.random()
        self.assertEqual(type(random_color), tuple, 'Return isn\'t tuple')
    
    @parameterized.expand([
        ['range_0_255', [0,255], [0,255], [0,255], [0,255]],
        ['range_wrong', [-1,255], [0,256], [-1,256], [-256,255]]
    ])
    def test_random(self, name, r_range, g_range, b_range, a_range):
        self.assertEqual(
            self.color_manager.random(r_range, g_range, b_range, a_range),
            (68, 32, 130, 60),
            'Color elements are not right or not of type int'
            )

    def test_random_overlap(self):
        self.assertEqual(
            self.color_manager.random([0,255], [15,12], [0,255], [0,255]),
            (68, 12, 130, 60),
            'Can\'t handle range elements overlaping'
            )
    
    def test_random_limited(self):
        self.assertEqual(
            self.color_manager.random([0,0], [255,255], [32,32], [0,0]),
            (0, 255, 32, 0)
        )


if __name__ == "__main__":
    unittest.main()
