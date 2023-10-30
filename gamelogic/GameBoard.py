from enum import Enum
from random import randint, random
from gamelogic.GameOverException import GameOverException

import numpy as np

BLANK_SPACE = 0
"""
Constant that defines the numerical value for a blank space. 
"""


def slide_array_right_to_left(np_array):
    """
    Helper function to slide values in an array from right to left.
    Ex. If 2,2,4,4 is passed in, 4,8,0,0 will be returned.

    """

    # First move all entries to the left without considering
    # combing with its neighbor. Entries can move to the left
    # as long as the entry to its left is a BLANK_SPACE.
    # This can be achieved by simply removing all BLANK_SPACE from
    # the array then filling it wih zeros up to its original length

    original_length = len(np_array)
    np_array = np_array[(np_array != BLANK_SPACE)]

    # Now loop from left to right and combine the current element
    # with its neighbor on the right if they are equal. Note that
    # elements are only allowed to combine one time.
    i = 0
    score = 0
    while i < (len(np_array) - 1):
        cur = np_array[i]
        # safe to get the next element since we are looping
        # from 0 to length-1
        right_neighbor = np_array[i + 1]

        if cur == right_neighbor:
            np_array[i] = cur + cur
            score = score + cur + cur
            # now delete the neighbor
            np_array = np.delete(np_array, i + 1)
        i = i + 1

    # Now fill the array back to its original length, using zeros to
    # pad if necessary
    np_array.resize([original_length])

    return np_array, score


class SlideDirection(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


class GameBoard:
    """
    Encapsulates the behavior of a game board. The game board is expected
    to look like this for a 4x4 board
    -------------------------------
             Col 0  Col 1   Col 2   Col 3
    row 0: |      |       |       |       |
    row 1: |      |       |       |       |
    row 2: |      |       |       |       |
    row 3: |      |       |       |       |
    -------------------------------
    """

    GENERATE_4_PROBABILITY = 0.1
    """
    Controls how often a 4 will be generated. 
    The rules of 2048 dictate that this is 10% 
    of the time. 
    """

    def __init__(self, width=4, height=4):
        """
        Create a new instance of a Game Board
        :param width: The width of the game board. If not passed in default of 4 is used
        :param height: The height of the game board. If not passed in default of 4 is used
        """
        self.width = width
        self.height = height

        self._game_board = np.array([])
        self._initialize_new_game_board()

        self._score = 0

    def _initialize_new_game_board(self):
        """
        Initialize an empty game board
        :return: void
        """
        self._game_board = np.zeros(shape=(self.height, self.width), dtype=int)
        self._score = 0

    def get_value(self, row: int, column: int) -> int:
        """
        Get the value at the specified position in the game board. The row and column indexes are 0 based with 0,0
        being the top left
        :param row: The row index to get
        :param column: The colum index to get
        :return: The value at the specified position
        """
        return self._game_board[row][column]

    def set_value(self, value: int, row: int, column: int):
        """
        Set the value at the specified position in the game board. The row and column indexes are 0 based with 0,0
        being the top left
        :param value: the value to set
        :param row: The row index to get
        :param column: The colum index to get

        """
        self._game_board[row][column] = value

    def reset_game_board(self):
        """
        Reset the game board to its empty state.
        :return: void
        """
        self._initialize_new_game_board()

    def slide_left(self):
        """
        Perform the action of sliding the game board to the left.
        :return: void
        """

        for r in range(0, self._game_board.shape[0]):
            new_row, score = slide_array_right_to_left(self._game_board[r])
            self._game_board[r] = new_row
            self._score = self._score + score

    def slide_right(self):
        """
        Perform the action of sliding the game board to the right.
        :return: void
        """

        # first flip the game board (reverse all rows)
        self._game_board = np.fliplr(self._game_board)

        # now slide left
        self.slide_left()

        # now flip the board again to get it back to the correct orientation
        self._game_board = np.fliplr(self._game_board)

    def slide_up(self):
        """
        Perform the action of sliding the game board up.
        :return: void

        """
        # first transpose the game board. This will make it so that sliding
        # left is the same as sliding up.
        self._game_board = np.transpose(self._game_board)

        # Now slide to the left
        self.slide_left()

        # Now transpose again to return the board to the correct orientation.
        self._game_board = np.transpose(self._game_board)

    def slide_down(self):
        """
        Perform the action of sliding the game board down.
        :return: void
        """

        # first reverse the game board up and down
        self._game_board = np.flipud(self._game_board)

        # now call slide up
        self.slide_up()

        # now reverse it back to its correct orientation.
        self._game_board = np.flipud(self._game_board)

    def do_turn(self, slide_direction):
        """

        @param slide_direction:
        @return: false if game is over, true otherwise.
        """
        if slide_direction == SlideDirection.LEFT:
            self.slide_left()
        elif slide_direction == SlideDirection.RIGHT:
            self.slide_right()
        elif slide_direction == SlideDirection.UP:
            self.slide_up()
        elif slide_direction == SlideDirection.DOWN:
            self.slide_down()

        self._generate_new_tile()

        return self._detect_end_of_game()

    def _generate_new_tile(self):
        """
        Generates a random new tile for the game board.
        """
        if random() < GameBoard.GENERATE_4_PROBABILITY:
            new_num = 4
        else:
            new_num = 2

        # generate a random place for the tile to go
        # do this by iterating over the board and creating a list
        # of tuples representing blank spaces, then select a random tuple

        # blank spaces will be a tuple of lists. The first element in the
        # tuple will be the x positions and the second will be y position
        # Ex ([2,2], [2,3]) means there is a zero in row index 2 col index 2 and
        # row index 2 col index 3.
        blank_spaces = np.where(self._game_board == BLANK_SPACE)

        index_to_use = randint(0, len(blank_spaces[0]) - 1)

        r = blank_spaces[0][index_to_use]
        c = blank_spaces[1][index_to_use]

        self._game_board[r][c] = new_num

    def _detect_end_of_game(self):
        """
        TODO implement to automatically detect end of game.
        """
        game_over = False

        if game_over:
            raise GameOverException("No more moves are available. "
                                    "Game Over! Score " + str(self._score))

    def undo_turn(self):
        """
        TODO implement an undo turn option
        Not implemented currently. But would be a good thing to add.
        """
        raise NotImplemented("Undo Turn is Not Implemented Yet")

    def get_score(self):
        return self._score

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def save_sate(self, filename):
        """
        Save the game board state to the file passed in.

        :param filename: The file to save the game board state to.
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
        Creates a string representation of the current Game Board State
        """
        pass
