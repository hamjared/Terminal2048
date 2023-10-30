import pytest
import unittest
from gamelogic.GameBoard import GameBoard, BLANK_SPACE
from gamelogic.GameBoard import slide_array_right_to_left
import numpy as np


class TestGameBoardStaticMethods(unittest.TestCase):
    def test_slide_array_from_right_to_left_1(self):
        input_array = np.array([2, 0, 4, 8])
        expected_output = np.array([2, 4, 8, 0])
        expected_score = 0

        actual_output, score = slide_array_right_to_left(input_array)

        self.assertEqual(expected_output.tolist(), actual_output.tolist())
        self.assertEqual(expected_score, score)

    def test_slide_array_from_right_to_left_2(self):
        input_array = np.array([2, 2, 4, 8])
        expected_output = np.array([4, 4, 8, 0])
        expected_score = 4

        actual_output, score = slide_array_right_to_left(input_array)

        self.assertEqual(expected_output.tolist(), actual_output.tolist())
        self.assertEqual(expected_score, score)

    def test_slide_array_from_right_to_left_3(self):
        input_array = np.array([2, 2, 4, 4])
        expected_output = np.array([4, 8, 0, 0])
        expected_score = 12

        actual_output, score = slide_array_right_to_left(input_array)

        self.assertEqual(expected_output.tolist(), actual_output.tolist())
        self.assertEqual(expected_score, score)

    def test_slide_array_from_right_to_left_4(self):
        input_array = np.array([0, 2, 0, 8])
        expected_output = np.array([2, 8, 0, 0])
        expected_score = 0

        actual_output, score = slide_array_right_to_left(input_array)

        self.assertEqual(expected_output.tolist(), actual_output.tolist())
        self.assertEqual(expected_score, score)

    def test_slide_array_from_right_to_left_5(self):
        input_array = np.array([0, 2, 0, 8])
        expected_output = np.array([2, 8, 0, 0])
        expected_score = 0

        actual_output, score = slide_array_right_to_left(input_array)

        self.assertEqual(expected_output.tolist(), actual_output.tolist())
        self.assertEqual(expected_score, score)

    def test_slide_array_from_right_to_left_6(self):
        input_array = np.array([0, 2, 0, 2])
        expected_output = np.array([4, 0, 0, 0])
        expected_score = 4

        actual_output, score = slide_array_right_to_left(input_array)

        self.assertEqual(expected_output.tolist(), actual_output.tolist())
        self.assertEqual(expected_score, score)


def _count_blank_spaces(game_board: GameBoard):
    blank_spaces = 0
    for r in range(0, game_board.get_height()):
        for c in range(0, game_board.get_width()):
            if game_board.get_value(r, c) == BLANK_SPACE:
                blank_spaces = blank_spaces + 1

    return blank_spaces


class TestGameBoard(unittest.TestCase):
    def test_initializeGameBoard(self):
        width = 4
        height = 4
        gameBoard = GameBoard(width=width, height=height)

        self.assertEqual(0, gameBoard.get_score())
        for r in range(0, height):
            for c in range(0, width):
                self.assertEqual(0, gameBoard.get_value(row=r, column=c), "Row {} Column {} is not 0".format(r, c))

    def test_slide_left_with_combining(self):
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

        gameBoard.slide_left()
        expected_after_state = [
            [4, 4, 0, 0],
            [4, 4, 0, 0],
            [4, 4, 8, 0],
            [2, 4, 8, 0]
        ]
        expected_score = 20

        for r in range(0, height):
            for c in range(0, width):
                self.assertEqual(
                    expected_after_state[r][c],
                    gameBoard.get_value(row=r, column=c),
                    "Row {} Column {} is not expected".format(r, c))

        self.assertEqual(expected_score, gameBoard.get_score())

    def test_slide_right_with_combining(self):
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

        gameBoard.slide_right()
        expected_after_state = [
            [0, 0, 4, 4],
            [0, 0, 4, 4],
            [0, 4, 4, 8],
            [0, 2, 4, 8]
        ]

        expected_score = 20

        for r in range(0, height):
            for c in range(0, width):
                self.assertEqual(
                    expected_after_state[r][c],
                    gameBoard.get_value(row=r, column=c),
                    "Row {} Column {} is not expected".format(r, c))

        self.assertEqual(expected_score, gameBoard.get_score())

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

        expected_score = 44

        for r in range(0, height):
            for c in range(0, width):
                self.assertEqual(
                    expected_after_state[r][c],
                    gameBoard.get_value(row=r, column=c),
                    "Row {} Column {} is not expected".format(r, c))

        self.assertEqual(expected_score, gameBoard.get_score())

    def test_slide_down_with_combining(self):
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

        gameBoard.slide_down()
        expected_after_state = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 2, 4, 4],
            [4, 4, 8, 16]
        ]

        expected_score = 44

        for r in range(0, height):
            for c in range(0, width):
                self.assertEqual(
                    expected_after_state[r][c],
                    gameBoard.get_value(row=r, column=c),
                    "Row {} Column {} is not expected".format(r, c))

        self.assertEqual(expected_score, gameBoard.get_score())

    def test_generate_new_tile(self):
        width = 4
        height = 4
        gameBoard = GameBoard(width=width, height=height)

        begin_state = [
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 4, 8],
            [2, 0, 0, 8]
        ]

        for r in range(0, height):
            for c in range(0, width):
                gameBoard.set_value(begin_state[r][c], row=r, column=c)

        original_blank_spaces = _count_blank_spaces(gameBoard)
        expected_blank_spaces = original_blank_spaces - 1



        gameBoard._generate_new_tile()

        self.assertEqual(expected_blank_spaces, _count_blank_spaces(gameBoard))


if __name__ == '__main__':
    unittest.main()
