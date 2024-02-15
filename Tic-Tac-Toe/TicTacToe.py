import pygame
import debug


class BoardModel:
    board = [' ' for _ in range(10)]

    def is_board_full(self):
        for i in self.board:
            if i == ' ':
                return False
        return True

    def initialize_board(self):
        for i in range(10):
            self.board[i] = ' '

    def space_is_free(self, clicked_row, clicked_col):
        flat_dim_index = flat_index(clicked_row, clicked_col)
        if self.board[flat_dim_index] == ' ':
            return True
        else:
            return False

    def is_winner(self, player):
        if (self.board[1] == player and self.board[2] == player and self.board[3] == player) or \
                (self.board[4] == player and self.board[5] == player and self.board[6] == player) or \
                (self.board[7] == player and self.board[8] == player and self.board[9] == player) or \
                (self.board[1] == player and self.board[4] == player and self.board[7] == player) or \
                (self.board[2] == player and self.board[5] == player and self.board[8] == player) or \
                (self.board[3] == player and self.board[6] == player and self.board[9] == player) or \
                (self.board[1] == player and self.board[5] == player and self.board[9] == player) or \
                (self.board[3] == player and self.board[5] == player and self.board[7] == player):
            return True
        else:
            return False

    def set_position(self, row, column, player):
        flat_dim_index = flat_index(row, column)
        self.board[flat_dim_index] = player

    def get_symbol_on_position(self, row, column):
        flat_dim_index = flat_index(row, column)
        return self.board[flat_dim_index]


class DrawerView:
    # Screen dimensions
    width = 300
    height = 300
    line_width = 5
    board_rows = 3
    board_cols = 3
    square_size = 100
    circle_radius = 30
    circle_width = 15
    cross_width = 25
    space = 55

    # Colors
    line_color = (23, 145, 135)
    bg_color = (28, 170, 156)
    circle_color = (239, 231, 200)
    cross_color = (66, 66, 66)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tic Tac Toe')
    screen.fill(bg_color)

    # board = [' ' for _ in range(10)]

    def draw_lines(self):
        # Horizontal lines
        pygame.draw.line(self.screen, self.line_color, (0, self.square_size), (self.width, self.square_size),
                         self.line_width)
        pygame.draw.line(self.screen, self.line_color, (0, 2 * self.square_size), (self.width, 2 * self.square_size),
                         self.line_width)

        # Vertical lines
        pygame.draw.line(self.screen, self.line_color, (self.square_size, 0), (self.square_size, self.height),
                         self.line_width)
        pygame.draw.line(self.screen, self.line_color, (2 * self.square_size, 0), (2 * self.square_size, self.height),
                         self.line_width)

    def draw_figures(self, board: BoardModel):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                if board.get_symbol_on_position(row, col) == 'O':  # [row * 3 + col + 1]
                    pygame.draw.circle(self.screen, self.circle_color, (
                        int(col * self.square_size + self.square_size // 2),
                        int(row * self.square_size + self.square_size // 2)),
                                       self.circle_radius,
                                       self.circle_width)
                elif board.get_symbol_on_position(row, col) == 'X':
                    pygame.draw.line(self.screen, self.cross_color,
                                     (col * self.square_size + self.space,
                                      row * self.square_size + self.square_size - self.space),
                                     (col * self.square_size + self.square_size - self.space,
                                      row * self.square_size + self.space), self.cross_width)
                    pygame.draw.line(self.screen, self.cross_color,
                                     (col * self.square_size + self.space, row * self.square_size + self.space),
                                     (col * self.square_size + self.square_size - self.space,
                                      row * self.square_size + self.square_size - self.space),
                                     self.cross_width)

    def get_mouse_row_col(self, mouse_x, mouse_y):
        x, y = int(mouse_y // self.square_size), int(mouse_x // self.square_size)
        return x, y


def flat_index(row, col):
    return row * 3 + col + 1


class Controller:
    def __init__(self):
        pygame.init()
        self.drawer = DrawerView()
        self.board = BoardModel()

    def game(self):
        self.drawer.draw_lines()
        pygame.display.update()
        running = True
        player_symbol = 'X'
        board = BoardModel()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # a1 = board.is_board_full()
                # debug.debug(a1, 10)
                if event.type == pygame.MOUSEBUTTONDOWN and not board.is_board_full():
                    mouse_x = event.pos[0]  # x
                    mouse_y = event.pos[1]  # y

                    clicked_row, clicked_col = self.drawer.get_mouse_row_col(mouse_x, mouse_y)
                    # print(clicked_row, clicked_col)

                    if board.space_is_free(clicked_row, clicked_col) \
                            and player_symbol == 'X' \
                            and not board.is_board_full():
                        board.set_position(clicked_row, clicked_col, 'X')
                        player_symbol = 'O'
                        self.drawer.draw_figures(self.board)

                    if board.space_is_free(clicked_row, clicked_col) \
                            and player_symbol == 'O' and not board.is_board_full():
                        board.set_position(clicked_row, clicked_col, 'O')
                        player_symbol = 'X'
                        self.drawer.draw_figures(self.board)
                pygame.display.update()

            if board.is_winner('X'):
                print("X wins!")
                running = False
            elif board.is_winner('O'):
                print("O wins!")
                running = False
            elif board.is_board_full():
                print("Tie game!")


if __name__ == "__main__":
    controller = Controller()
    controller.game()
