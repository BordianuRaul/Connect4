import math
import random

from Domain.Board import Board
from Domain.Move import Move
from Domain.MoveValidator import MoveValidator


class BoardService:

    def __init__(self, board: Board, move_validator: MoveValidator()):

        self._game_board = board
        self._move_validator = move_validator

    @property
    def game_board(self):
        return self._game_board

    def make_move(self, move: Move):

        """
        Updates the board with a move done either by the player or computer
        :param move: a connect 4 move
        :return: None
        """

        row = move.row
        column = move.column
        token = move.token

        self._game_board.update_board(row, column, token)

    def get_board(self) -> list:
        """
        Returns the matrix of the game_board
        """

        return self._game_board.board

    def player_move(self, column: int):

        """
        Computes a move made by the player
        :param column: column on which the player made the move
        :return:
        """

        player_move = self.generate_player_move(column)

        self._move_validator.validate(player_move, self._game_board)

        self.make_move(player_move)

    def generate_player_move(self, column: int) -> Move:
        """
        Generates a move data structure corresponding to a player move
        :return:
        """

        row = self.find_row(column)

        move = Move(row, column, "0")

        return move

    def find_row(self, column: int):
        """
        Finds the first empty row, for a given column
        :param column: column index
        :return: index of the row
        """

        for row in range(5, -1, -1):

            if self._game_board.get_token(row, column) == " ":
                return row

    def computer_move(self):
        """
        Handles the creation of a computer move
        :return:
        """

        computer_move = self.generate_computer_move()
        self.make_move(computer_move)

    def ai_move(self):
        """
        Handles the creation of a move made by de AI
        :return:
        """

        ai_move = self.generate_ai_move()
        self.make_move(ai_move)

    def generate_ai_move(self) -> Move:
        """
        Generates a move made by the AI
        :return:
        """

        aux_board = self._game_board.board

        column = self.minimax(aux_board, 7, -math.inf, math.inf, True)[0]

        row = self.find_row(column)

        ai_move = Move(row, column, "X")

        return ai_move

    def generate_computer_move(self) -> Move:
        """
        Generates a move made by the computer
        :return: generated move
        """

        moves = self.valid_moves()

        indexes = random.randint(0, len(moves) - 1)

        row = moves[indexes][0]
        column = moves[indexes][1]

        computer_move = Move(row, column, "X")

        return computer_move

    def valid_moves(self) -> list:

        """
        Finds all the valid moves that can be made on the board
        :return:
        """

        valid_moves = []

        for column in range(0, 7):
            for row in range(5, -1, -1):
                if self._game_board.get_token(row, column) == " ":
                    valid_moves.append((row, column))
                    break

        return valid_moves

    def check_win(self, token: str):

        """
        Checks if the winning condition was satisfied either on line, column or diagonals
        :return: True/False
        """

        if self.check_win_lines(token):
            return True
        if self.check_win_on_columns(token):
            return True
        if self.check_win_on_diagonals_left_to_right(token):
            return True
        if self.check_win_on_diagonals_from_right_to_left(token):
            return True

        return False

    def check_win_lines(self, token: str):

        """
        Checks if the winning condition was satisfied on a line
        :return: 
        """
        
        for line in range(5, -1, -1):
            for column in range(0, 4):
                if self._game_board.get_token(line, column) == token and self._game_board.get_token(line, column) \
                        == self._game_board.get_token(line, column + 1) \
                        == self._game_board.get_token(line, column + 2) == self._game_board.get_token(line, column + 3):

                    return True

        return False
    
    def check_win_on_columns(self, token: str):
        
        """
        Checks if the winning condition was satisfied on a column
        :return: 
        """
        
        for column in range(0, 7):
            for line in range(5, 2, -1):
                if self._game_board.get_token(line, column) == token and\
                        self._game_board.get_token(line, column) == self._game_board.get_token(line - 1, column) \
                        == self._game_board.get_token(line - 2, column) == self._game_board.get_token(line - 3, column):

                    return True

        return False
    
    def check_win_on_diagonals_left_to_right(self, token: str):
        
        """
        Checks if the winning condition was satisfied on a diagonal from left to right
        :return: 
        """
        
        for line in range(5, 2, -1):
            for column in range(4):
                if self._game_board.get_token(line, column) == token and\
                        self._game_board.get_token(line, column) == self._game_board.get_token(line - 1, column + 1) \
                        == self._game_board.get_token(line - 2, column + 2) ==\
                        self._game_board.get_token(line - 3, column + 3):

                    return True
        return False
    
    def check_win_on_diagonals_from_right_to_left(self, token: str):
        
        """
        Checks if the winning condition was satisfied on a diagonal from right to left
        token: token of the player or of the computer
        :return: 
        """
        
        for line in range(5, 2, -1):
            for column in range(3, 7):
                if self._game_board.get_token(line, column) == token and\
                        self._game_board.get_token(line, column) == self._game_board.get_token(line - 1, column - 1) \
                        == self._game_board.get_token(line - 2, column - 2) ==\
                        self._game_board.get_token(line - 3, column - 3):

                    return True
        return False

    def check_draw(self):
        """
        Checks if the match resulted in a draw
        :return:
        """

        valid_moves = self.valid_moves()

        if len(valid_moves) == 0:
            return True
        return False

    def minimax(self, aux_board: list, depth: int, alpha, beta, maximizing_player: bool):

        """
        Implementation of the minimax algorithm to determine the column of the best move to be made by the AI,
        optimized with alpha, beta pruning
        :param aux_board: a copy of the board that the game is running
        :param depth: depth of the tree that will be generated
        :param alpha: alpha value
        :param beta: beta value
        :param maximizing_player: True for the maximizing player and False for the minimizing player
        :return: index of the column resulted from the search
        """

        valid_moves = self.valid_moves_for_board(aux_board)

        is_terminal = self.is_terminal_node()

        if depth == 0 or is_terminal:

            if is_terminal:

                if self.check_win("X"):
                    return None, 20000

                elif self.check_win("0"):
                    return None, -10000

                else:
                    return None, 0
            else:
                return None, self.score(aux_board, "X")

        if maximizing_player:

            value = -math.inf
            column = valid_moves[0][1]
            for move in valid_moves:

                row = move[0]
                col = move[1]

                duplicate_board = self.get_copy_of_board(aux_board)
                duplicate_board[row][col] = "X"
                new_score = self.minimax(duplicate_board, depth - 1, alpha, beta, False)[1]

                if new_score > value:
                    value = new_score
                    column = col

                alpha = max(alpha, value)
                if alpha >= beta:
                    break

            return column, value
        else:

            value = math.inf
            column = valid_moves[0][1]
            for move in valid_moves:

                row = move[0]
                col = move[1]

                duplicate_board = self.get_copy_of_board(aux_board)
                duplicate_board[row][col] = "0"
                new_score = self.minimax(duplicate_board, depth - 1, alpha, beta, True)[1]

                if new_score < value:
                    value = new_score
                    column = col

                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    @staticmethod
    def valid_moves_for_board(board: list):

        """
        Finds all moves that can be made on the current board status
        :param board: board of the current game
        :return: list with indexes of all possible moves
        """

        valid_moves = []

        for column in range(0, 7):
            for row in range(5, -1, -1):
                if board[row][column] == " ":
                    valid_moves.append((row, column))
                    break

        return valid_moves

    @staticmethod
    def get_copy_of_board(board: list):

        """
        Creates a copy of a board
        :param board: current board of the game
        :return:
        """

        board_duplicate = []

        for row in board:
            board_duplicate.append(row.copy())

        return board_duplicate

    def is_terminal_node(self):
        """
        Checks if the node from the minimax algorithm tree is terminal
        :return:
        """
        return self.check_win("X") or self.check_win("0") or self.check_draw()

    def score(self, board: list, token: str):

        """
        Generates the score of a move
        :param board: possible board configuration
        :param token: token of the minimizing/maximizing player
        :return:score of a move
        """

        score = 0

        # Score center column

        center_array = [i[3] for i in board]
        center_count = center_array.count(token)
        score += center_count * 3

        # Score Horizontal

        for row in board:
            for column in range(4):
                window = row[column:column + 4]
                score += self.evaluate_windows(window, token)

        # Score Vertical

        column_array = []
        for column in range(7):
            column_array.append([i[column] for i in board])

        for column in column_array:
            for row in range(3):
                window = column[row: row + 4]
                score += self.evaluate_windows(window, token)

        # Score diagonals left to right
        diagonals_array = []
        for r in range(5, 2, -1):
            for c in range(0, 4):
                diagonals_array.append([board[r][c], board[r - 1][c + 1], board[r - 2][c + 2], board[r - 3][c + 3]])

        for window in diagonals_array:
            score += self.evaluate_windows(window, token)

        diagonals_array = []
        for r in range(5, 2, -1):
            for c in range(3, 7):
                diagonals_array.append([board[r][c], board[r - 1][c - 1], board[r - 2][c - 2], board[r - 3][c - 3]])

        for window in diagonals_array:
            score += self.evaluate_windows(window, token)

        return score

    @staticmethod
    def evaluate_windows(window: list, token: str):

        """
        Return the score for a certain windows of the board
        :param window:represents a list of 4 elements representing
                      4 successive elements from a line/column or a diagonal from the board
        :param token: current board state of the game
        :return: score of the window
        """

        score = 0
        opp_token = "0"
        if token == "0":
            opp_token = "X"

        if window.count(token) == 4:
            score += 10000
        elif window.count(token) == 3 and window.count(" ") == 1:
            score += 5
        elif window.count(token) == 2 and window.count(" ") == 2:
            score += 2
        if window.count(opp_token) == 3 and window.count(" ") == 1:
            score -= 4
        if window.count(opp_token) == 4:
            score -= 10000

        return score
