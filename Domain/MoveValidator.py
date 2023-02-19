from Domain.Board import Board
from Domain.Move import Move


class MoveValidator:

    def validate(self, move: Move, board: Board):
        """
        Validates a move
        :param move: move to be validated
        :param board: board on which the move belongs
        :return:
        """

        errors = ""

        if move.column > 6 or move.column < 0:

            errors += "Row index out of bound!\n"

        if errors:
            raise ValueError(errors)
