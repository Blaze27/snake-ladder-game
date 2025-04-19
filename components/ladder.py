from components.cell import Cell

class Ladder:
    def __init__(self, start_cell: Cell, end_cell: Cell):
        """
        Initialize the ladder with its start and end cells.
        
        :param start_cell: The cell where the ladder starts.
        :param end_cell: The cell where the ladder ends.
        """
        self.start_cell = start_cell
        self.end_cell = end_cell