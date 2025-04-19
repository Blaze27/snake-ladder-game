import random

class Dice:
    """
    A class representing a dice with a specified number of sides.

    The number of sides must be between 1 and 6 (inclusive). This restriction ensures
    that the dice adheres to common gaming standards.

    :raises ValueError: If the number of sides is less than 1 or greater than 6.
    """
    def __init__(self, sides: int = 6):
        """
        Initialize the dice with a specified number of sides.
        :param sides: The number of sides on the dice (default is 6).
        :raises ValueError: If sides is less than 1 or greater than 6.
        """
        self.sides = self.__validate_sides(sides)
    
    def roll(self) -> int:
        """
        Roll the dice and return a random number between 1 and the number of sides.
        :return: A random number between 1 and the number of sides.
        """
        return random.randint(1, self.sides)
    
    def __validate_sides(self, sides: int) -> int:
        if sides < 1 or sides > 6:
            raise ValueError("Number of sides must be greater than 1 and less than 7.")
        return sides