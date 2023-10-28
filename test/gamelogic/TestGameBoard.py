import pytest
import unittest
from gamelogic.GameBoard import GameBoard


class TestGameBoard(unittest.TestCase):
    def test_initializeGameBoard(self):
        width = 4
        height = 4
        gameBoard = GameBoard(width=width, height=height)

        for r in range(0, height):
            for c in range(0, width):
                self.assertEqual(0, gameBoard.get_value(row=r, column=c), "Row {} Column {} is not 0".format(r, c))

    def test_slide_up_simple(self):
        width = 4
        height = 4
        gameBoard = GameBoard(width=width, height=height)

        for r in range(0, height):
            for c in range(0, width):
                self.assertEqual(0, gameBoard.get_value(row=r, column=c), "Row {} Column {} is not 0".format(r, c))

    def test_slide_up_with_combining(self):
        width = 4
        height = 4
        gameBoard = GameBoard(width=width, height=height)

        begin_state = [
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 4, 8],
            [2, 0, 4, 8]
        ]

        for r in range(0, height):
            for c in range(0, width):
                gameBoard.set_value(begin_state[r][c], row=r, column=c)

        gameBoard.slide_up()
        expected_after_state = [
            [4, 4, 4, 4],
            [4, 2, 8, 16],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        for r in range(0, height):
            for c in range(0, width):
                self.assertEqual(
                    expected_after_state[r][c],
                    gameBoard.get_value(row=r, column=c),
                    "Row {} Column {} is not expected".format(r, c))


if __name__ == '__main__':
    unittest.main()
