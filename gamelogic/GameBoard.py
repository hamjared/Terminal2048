import numpy as np


class GameBoard:
    """
    Encapsulates the beahvior of a game board. The game board is expected to look like this for a 4x4 board
    -------------------------------
             Col 0  Col 1   Col 2   Col 3
    row 0: |      |       |       |       |
    row 1: |      |       |       |       |
    row 2: |      |       |       |       |
    row 3: |      |       |       |       |
    -------------------------------
    """
    BLANK_SPACE = 0
    """
    Constant that defines the numerical value fo a blank space. 
    """

    def __init__(self, width=4, height=4):
        """
        Create a new instance of a Game Board
        :param width: The width of the game board. If not passed in default of 4 is used
        :param height: The height of the game board. If not passed in default of 4 is used
        """
        self.width = width
        self.height = height

        self._gameBoard = None
        self._initialize_new_game_board()

        pass

    def _initialize_new_game_board(self):
        """
        Initialize an empty game board
        :return: void
        """
        self._gameBoard = np.zeros(shape=(self.height, self.width), dtype=int)

    def get_value(self, row: int, column: int) -> int:
        """
        Get the value at the specified position in the game board. The row and column indexes are 0 based with 0,0
        being the top left
        :param row: The row index to get
        :param column: The colum index to get
        :return: The value at the specified position
        """
        return self._gameBoard[row][column]

    def set_value(self, value: int,  row: int, column: int):
        """
        Set the value at the specified position in the game board. The row and column indexes are 0 based with 0,0
        being the top left
        :param value: the value to set
        :param row: The row index to get
        :param column: The colum index to get

        """
        self._gameBoard[row][column] = value

    def reset_game_board(self):
        """
        Reset the game board to its empty state.
        :return: void
        """
        pass

    def slide_left(self):
        """
        Perform the action of sliding the game board to the left.
        :return: void
        """
        pass

    def slide_right(self):
        """
        Perform the action of sliding the game board to the right.
        :return: void
        """

        pass

    def slide_up(self):
        """
        Perform the action of sliding the game board to the up.
        :return: void

        """
        pass

    def slide_down(self):
        """
        Perform the action of sliding the game board to the down.
        :return: void
        """
        pass

    def save_sate(self, filename):
        """
        Save the gameboard state to the file passed in.

        :param filename: The file to save the gameboard state to.
        :return: void
        """
        pass

    def load_saved_game(self, filename):
        """
        Load the game board from a previously saved state.
        :param filename: The file to load the game state from.
        :return: void
        """
        pass

    def __str__(self):
        """
        Creats a string representation of the current Game Board State
        """
        pass
