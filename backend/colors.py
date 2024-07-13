# Functions for working with colors
import typing
import random


def check_range(target_range: typing.List[int]) -> typing.List[int]:
        """
        Checks if any of range elements are greater than 255
        or less than 0

        Parameters
        ----------
        target_range: typing.List[int]
            Range to check
        
        Returns
        -------
        correct_range: typing.List[int]
            Checked and corrected range
        """

        # Check if min value is greater than max value
        if (target_range[0] > target_range[1]):
            target_range[0] = target_range[1]

        correct_range = list()
        for elem in target_range:
            if elem < 0:
                correct_range.append(0)
            elif elem > 255:
                correct_range.append(255)
            else:
                correct_range.append(elem)

        return correct_range


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
            checked_range = check_range(color_elems[i])
            randint = random.randint(checked_range[0], checked_range[1])
            color += (randint,)
        
        return color

    
