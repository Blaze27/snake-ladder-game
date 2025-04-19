from src.constants import Constants

class Cell:
    """
    A class representing a cell in a grid.
    """

    def __init__(self, position: int):
        """
        Initialize the cell with its number.

        :param x: The cell number.
        """
        self.position = position
        self.cell_state = Constants.UN_OCCUPIED
        self.occupied_by = set()

    def occupy(self, player):
        """
        Mark the cell as occupied.
        """
        self.occupied_by.add(player)
        self.cell_state = Constants.OCCUPIED
        print(f"Cell ({self.x}) is now occupied.")

    def vacate(self, player):
        """
        Mark the cell as unoccupied.
        """
        if player in self.occupied_by:
            self.occupied_by.remove(player)
        else:
            raise ValueError("Player not found in occupied list.")
        if len(self.occupied_by) == 0:
            self.cell_state = Constants.UN_OCCUPIED
        print(f"Cell ({self.x}, {self.y}) is now unoccupied.")