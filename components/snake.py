from components.cell import Cell

class Snake:
    def __init__(self, start_cell: Cell, end_cell: Cell):
        """
        Initialize the snake with its start and end cells.
        
        :param start_cell: The cell where the snake starts.
        :param end_cell: The cell where the snake ends.
        """
        self.start_cell = start_cell
        self.end_cell = end_cell
    
    