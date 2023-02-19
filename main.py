from Domain.Board import Board
from Domain.MoveValidator import MoveValidator
from Service.BoardService import BoardService
from UserInterface.GUI import Connect4GUI


def main():

    board = Board()
    move_validator = MoveValidator()

    board_service = BoardService(board, move_validator)

    connect4 = Connect4GUI(board_service)

    connect4.run_game()

main()
