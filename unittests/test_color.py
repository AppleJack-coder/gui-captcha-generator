import unittest
from backend.colors import Color
import typing
import random


class TestColorsManager(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.color_manager = Color()

    def setUp(self):
        random.seed(1)

    def test_zero(self):
        self.assertEqual(self.color_manager.zero, (0, 0, 0, 0), 'Zero variable is\'t right')

    def test_random(self):
        random_color = self.color_manager.random()
        
        self.assertEqual(type(random_color), tuple, 'Return isn\'t tuple')
        self.assertEqual(random_color, (68, 32, 130, 60), 'Color elements are not right or int')
        self.assertEqual(
            self.color_manager.random(r_range=[0,0], g_range=[255,255], b_range=[32,32], a_range=[0,0]),
            (0, 255, 32, 0),
            'Can\'t handle ranges with 1 element (example: [0,0])'
            ) 


if __name__ == "__main__":
    unittest.main()
