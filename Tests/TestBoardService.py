import unittest

from Domain.Board import Board
from Domain.Move import Move
from Domain.MoveValidator import MoveValidator
from Service.BoardService import BoardService


class TestBoardService(unittest.TestCase):

    def test_make_move(self):

        board = Board()

        move_validator = MoveValidator()

        board_service = BoardService(board, move_validator)

        move = Move(1, 2, "X")

        board_service.make_move(move)

        self.assertEqual(board_service.get_board()[1][2], "X")

    def test_find_row(self):

        board = Board()

        move_validator = MoveValidator()

        board_service = BoardService(board, move_validator)

        move = Move(5, 2, "X")

        board_service.make_move(move)

        move = Move(4, 2, "X")

        board_service.make_move(move)

        test_row = board_service.find_row(2)

        self.assertEqual(test_row, 3)

    def test_generate_player_move(self):

        board = Board()

        move_validator = MoveValidator()

        board_service = BoardService(board, move_validator)

        move = Move(5, 2, "X")

        board_service.make_move(move)

        move = Move(4, 2, "X")

        board_service.make_move(move)

        move = board_service.generate_player_move(2)

        self.assertEqual(move.row, 3)
        self.assertEqual(move.column, 2)
        self.assertEqual(move.token, "0")

    def test_player_move(self):

        board = Board()

        move_validator = MoveValidator()

        board_service = BoardService(board, move_validator)

        move = Move(5, 2, "X")

        board_service.make_move(move)

        move = Move(4, 2, "X")

        board_service.make_move(move)

        board_service.player_move(2)

        self.assertEqual(board.get_token(3, 2), "0")

    def test_valid_moves(self):

        board = Board()

        move_validator = MoveValidator()

        board_service = BoardService(board, move_validator)

        move = Move(5, 2, "X")

        board_service.make_move(move)

        move = Move(4, 2, "X")

        board_service.make_move(move)

        board_service.player_move(2)

        valid_moves = board_service.valid_moves()

        test_valid_moves = [(5, 0), (5, 1), (2, 2), (5, 3), (5, 4), (5, 5), (5, 6)]

        self.assertEqual(valid_moves, test_valid_moves)

