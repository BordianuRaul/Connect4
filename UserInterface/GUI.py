import sys

import pygame

from Service.BoardService import BoardService


class Connect4GUI:

    def __init__(self, board_service: BoardService):
        self._board_service = board_service

        pygame.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.mixer.music.load('background.mp3')
        pygame.mixer.music.play(-1)

        self.piece = pygame.mixer.Sound("piece_drop.mp3")

        pygame.display.set_caption('Connect 4')
        size = (700, 600)
        self.screen = pygame.display.set_mode(size)

    def draw_board(self):
        """
        Draws board
        :return:
        """

        blue = (0, 0, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        yellow = (255, 255, 0)

        for column in range(7):
            for line in range(5, -1, -1):
                pygame.draw.rect(self.screen, blue, (column * 100, line * 100, 100, 100))

                if self._board_service.game_board.get_token(line, column) == "X":
                    pygame.draw.circle(self.screen, red, (int(column * 100 + 100 / 2),
                                                          int(line * 100 + 100 / 2)), 45)

                elif self._board_service.game_board.get_token(line, column) == "0":
                    pygame.draw.circle(self.screen, yellow, (int(column * 100 + 100 / 2),
                                                             int(line * 100 + 100 / 2)), 45)
                else:
                    pygame.draw.circle(self.screen, black, (int(column * 100 + 100 / 2),
                                                            int(line * 100 + 100 / 2)), 45)

        pygame.display.update()

    def run_game(self):

        """
        Runs game
        :return:
        """

        while True:
            try:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                    self.draw_board()

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        self.piece.play()
                        self.handle_player_move(event)
                        self.draw_board()

                        if self._board_service.check_win("0"):
                            print("Congrats, you win!")
                            pygame.time.wait(5000)
                            return 0

                        if self._board_service.check_draw():
                            print("It's a DRAW!")
                            pygame.time.wait(5000)
                            return 0

                        self.handle_computer_move()
                        self.piece.play()
                        self.draw_board()

                        if self._board_service.check_win("X"):
                            print("Game over! Computer wins!")
                            pygame.time.wait(5000)
                            return 0

                        if self._board_service.check_draw():
                            print("It's a DRAW!")
                            pygame.time.wait(5000)
                            return 0

            except Exception as ex:
                print("Oops: ", ex)

    def handle_player_move(self, event):
        """
        Handles the move made by the player
        :param event:
        :return:
        """

        column_pos_clicked = event.pos[0]

        column = column_pos_clicked // 100

        self._board_service.player_move(column)

    def handle_computer_move(self):
        """
        Handles the move made by the computer
        :return:
        """

        self._board_service.ai_move()
