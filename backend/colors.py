# Functions for working with colors
import typing
import random


class Color:
    def __init__(self) -> typing.NoReturn:
        self.zero = (0, 0, 0, 0)
    

    def random(self, r_range=[0, 255], g_range=[0, 255], b_range=[0, 255], a_range=[0, 255]) -> typing.Tuple[int]:
        """
        Generates random uniform color in RGBA format

        Returns
        -------
        color: typing.Tuple[int]
            Random color
        """

        color = tuple()
        color_elems = [r_range, g_range, b_range, a_range]
        for i in range(4):
            randint = random.randint(color_elems[i][0], color_elems[i][1])
            color += (randint,)
        
        return color

    
