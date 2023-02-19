import unittest

from Domain.Board import Board


class TestBoard(unittest.TestCase):

    def test_constructor_board(self):

        board = Board()

        test_board = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]]

        self.assertEqual(board.board, test_board)

    def test_update_board(self):

        board = Board()

        board.update_board(1, 5, "X")

        self.assertEqual(board.get_token(1, 5), "X")
