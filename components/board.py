from typing import List
from components.snake import Snake
from components.ladder import Ladder

class Board:
    def __init__(self, board_size = 100):
        """
        Initialize the board with a specified size.
        :param board_size: The number of cells on the board (default is 100).
        """
        self.board_size = board_size
        self.board = self.__create_board()
        self.snakes: List[Snake] = []
        self.ladders: List[Ladder] = []

    def __create_board(self):
        """
        Create a board with the specified number of cells.
        :return: A list of cells representing the board.
        """

        from components.cell import Cell

        return [Cell(i) for i in range(1, self.board_size + 1)]

    def add_snake(self, snake):
        """
        Add a snake to the board.
        :param: snake
        """

        self.snakes.append(snake)

    def add_ladder(self, ladder):
        """
        Add a ladder to the board.
        :param: ladder
        """

        self.ladders.append(ladder)
    
