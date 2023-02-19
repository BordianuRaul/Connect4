import unittest

from Domain.Board import Board
from Domain.Move import Move
from Domain.MoveValidator import MoveValidator


class TestMoveValidator(unittest.TestCase):

    def test_validate_move(self):


        board = Board()
        move_validator = MoveValidator()

        board.update_board(0, 3, "X")
        board.update_board(1, 3, "X")
        board.update_board(2, 3, "X")
        board.update_board(3, 3, "X")
        board.update_board(4, 3, "X")
        board.update_board(5, 3, "X")

        move = Move(6, 3, "0")

        try:

            move_validator.validate(move, board)
        except ValueError as ex:

            self.assertEqual(ex, "The column is already full!\n")
