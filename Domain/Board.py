
class Board:

    def __init__(self):

        self._board = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]]

    @property
    def board(self):
        return self._board

    def get_token(self, row: int, column: int):

        """
        Returns the token sign from the board
        :param row: row index corresponding to the token
        :param column: column index corresponding to the token
        :return: token
        """

        return self._board[row][column]

    def update_board(self, row: int, column: int, token: str):

        """
        Updates the board with a token on a certain column
        :return:
        """

        self._board[row][column] = token
