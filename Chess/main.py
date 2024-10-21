import pygame
import chess
import random

# Initialize pygame and chess board
pygame.init()
board = chess.Board()

# Constants for window dimensions and colors
WIDTH, HEIGHT = 600, 750
BOARD_SIZE = 512
MARGIN = (WIDTH - BOARD_SIZE) // 2
TITLE_HEIGHT = 50
SQ_SIZE = BOARD_SIZE // 8
LIGHT = (235, 236, 208)
DARK = (115, 149, 82)
LIGHT_HIGHLIGHT = (245, 246, 130)
DARK_HIGHLIGHT = (185, 202, 67)
BOT_HIGHLIGHT_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (48, 46, 43)

# Load chess piece images
pieces = {f'{color}_{piece}': pygame.image.load(f'Chess/pieces/{color}_{piece}.png') for color in ['w', 'b'] for piece in ['p', 'r', 'n', 'b', 'q', 'k']}

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Bot")

# Fonts for the title and endgame message
title_font = pygame.font.Font(None, 48)
endgame_font = pygame.font.Font(None, 64)

# Variables for game state
mode = None
selected_square = None
bot_last_move = None
game_over_message = None
running = True
game_mode = None
bot_difficulty = None
show_difficulty_selection = False
confirmation_active = False
confirm_restart_rect = None
cancel_restart_rect = None


def draw_board(selected_square=None, bot_move_square=None):
    for row in range(8):
        for col in range(8):
            color = LIGHT if (row + col) % 2 == 0 else DARK
            if selected_square == chess.square(col, 7 - row):
                color = LIGHT_HIGHLIGHT if (
                    row + col) % 2 == 0 else DARK_HIGHLIGHT
            if bot_move_square == chess.square(col, 7 - row):
                color = BOT_HIGHLIGHT_COLOR
            square_rect = pygame.Rect(
                MARGIN + col * SQ_SIZE, TITLE_HEIGHT + row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            pygame.draw.rect(screen, color, square_rect)


def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_image = pieces[f'{"w" if piece.color else "b"}_{
                piece.symbol().lower()}']
            x = MARGIN + \
                chess.square_file(square) * SQ_SIZE + \
                (SQ_SIZE - piece_image.get_width()) // 2
            y = TITLE_HEIGHT + (7 - chess.square_rank(square)) * \
                SQ_SIZE + (SQ_SIZE - piece_image.get_height()) // 2
            screen.blit(piece_image, pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))


def draw_title():
    title_surface = title_font.render("Chess Bot", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(WIDTH // 2, TITLE_HEIGHT // 2))
    screen.blit(title_surface, title_rect)


def draw_endgame_message(message):
    message_surface = endgame_font.render(message, True, (255, 255, 255))
    message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(message_surface, message_rect)


def get_square_under_mouse():
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    x, y = [int((v - MARGIN) // SQ_SIZE) for v in mouse_pos]
    if 0 <= x < 8 and TITLE_HEIGHT <= y * SQ_SIZE + TITLE_HEIGHT < TITLE_HEIGHT + BOARD_SIZE:
        return chess.square(x, 7 - int((mouse_pos[1] - TITLE_HEIGHT) // SQ_SIZE))
    return None


def is_pawn_promotion(move):
    return board.piece_at(move.from_square).piece_type == chess.PAWN and (chess.square_rank(move.to_square) == 0 or chess.square_rank(move.to_square) == 7)


def pawn_promotion():
    return chess.QUEEN


def check_game_over():
    if board.is_checkmate():
        if game_mode == "pvp":
            return "Checkmate! Black Wins!" if board.turn else "Checkmate! White Wins!"
        else:
            return "Checkmate! Bot Wins!" if board.turn else "Checkmate! You Win!"
    elif board.is_stalemate():
        return "Stalemate! It's a Draw!"
    elif board.is_insufficient_material():
        return "Draw due to Insufficient Material!"
    elif board.is_seventyfive_moves():
        return "Draw by 75-move Rule!"
    elif board.is_fivefold_repetition():
        return "Draw by Repetition!"
    elif board.is_variant_draw():
        return "Draw by Variant!"
    return None


def draw_mode_selection():
    screen.fill(BACKGROUND_COLOR)
    title_surface = title_font.render(
        "Choose Game Mode", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_surface, title_rect)
    pvp_surface = endgame_font.render(
        "Player vs Player", True, (255, 255, 255))
    pvp_rect = pvp_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(pvp_surface, pvp_rect)
    pvb_surface = endgame_font.render("Player vs Bot", True, (255, 255, 255))
    pvb_rect = pvb_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(pvb_surface, pvb_rect)
    return pvp_rect, pvb_rect


def draw_difficulty_selection():
    screen.fill(BACKGROUND_COLOR)
    title_surface = title_font.render(
        "Select Bot Difficulty", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_surface, title_rect)
    easy_surface = endgame_font.render("Easy", True, (255, 255, 255))
    easy_rect = easy_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(easy_surface, easy_rect)
    medium_surface = endgame_font.render("Medium", True, (255, 255, 255))
    medium_rect = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(medium_surface, medium_rect)
    # Logic for hard mode is not implemented yet... [You can work on it if you want]
    # hard_surface = endgame_font.render("Hard", True, (255, 255, 255))
    # hard_rect = hard_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    # screen.blit(hard_surface, hard_rect)
    # return easy_rect, medium_rect, hard_rect
    return easy_rect, medium_rect


def draw_restart_button():
    restart_surface = endgame_font.render("Restart", True, (255, 255, 255))
    restart_rect = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(restart_surface, restart_rect)
    return restart_rect


def reset_game():
    global board, game_mode, bot_difficulty, show_difficulty_selection, game_over_message, selected_square, confirmation_active
    board.reset()
    game_mode = None
    bot_difficulty = None
    show_difficulty_selection = False
    game_over_message = None
    selected_square = None
    confirmation_active = False


def draw_confirmation_box():
    box_width, box_height = 400, 150
    confirmation_box_rect = pygame.Rect(
        WIDTH // 2 - box_width // 2, HEIGHT // 2 - box_height // 2, box_width, box_height)
    pygame.draw.rect(screen, (50, 50, 50), confirmation_box_rect)
    pygame.draw.rect(screen, (255, 255, 255), confirmation_box_rect, 3)
    confirm_text = endgame_font.render("Restart game?", True, (255, 255, 255))
    screen.blit(confirm_text, (confirmation_box_rect.x +
                60, confirmation_box_rect.y + 20))
    yes_surface = endgame_font.render("Yes", True, (255, 255, 255))
    no_surface = endgame_font.render("No", True, (255, 255, 255))
    confirm_restart_rect = yes_surface.get_rect(
        center=(confirmation_box_rect.x + 100, confirmation_box_rect.y + 100))
    cancel_restart_rect = no_surface.get_rect(
        center=(confirmation_box_rect.x + 300, confirmation_box_rect.y + 100))
    screen.blit(yes_surface, confirm_restart_rect)
    screen.blit(no_surface, cancel_restart_rect)
    return confirm_restart_rect, cancel_restart_rect


''' 
Main bot logic

The bot has two difficulty levels: 'easy' and 'medium' [for now].
- In 'easy' mode, the bot makes a random legal move.
- In 'medium' mode, the bot prioritizes capturing moves. 
  - If there are capturing moves available, it selects the capture with the highest piece value.
  - If no capturing moves are available, it makes a random legal move.

'''
def bot_move(mode):
    moves = list(board.legal_moves)
    
    if mode == 'easy':
        return random.choice(moves) if moves else None
    elif mode == 'medium':
        captures = [move for move in moves if board.is_capture(move)]
        if captures:
            piece_values = {chess.PAWN: 1, chess.KNIGHT: 3,
                            chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}
            captures_by_value = {}
            for capture in captures:
                value = piece_values[board.piece_at(
                    capture.to_square).piece_type]
                captures_by_value.setdefault(value, []).append(capture)
            best_captures = captures_by_value[max(captures_by_value.keys())]
            return random.choice(best_captures)
        return random.choice(moves)
    return None


while running:
    screen.fill(BACKGROUND_COLOR)

    if game_mode is None:
        pvp_rect, pvb_rect = draw_mode_selection()
    elif show_difficulty_selection:
        # easy_rect, medium_rect, hard_rect = draw_difficulty_selection()
        easy_rect, medium_rect = draw_difficulty_selection()
    else:
        draw_title()
        draw_board(selected_square, bot_last_move)
        draw_pieces()
        if game_over_message:
            draw_endgame_message(game_over_message)
        restart_rect = draw_restart_button()
        if confirmation_active:
            confirm_restart_rect, cancel_restart_rect = draw_confirmation_box()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if game_mode is None:
                if pvp_rect.collidepoint(mouse_pos):
                    game_mode = 'pvp'
                elif pvb_rect.collidepoint(mouse_pos):
                    game_mode = 'pvb'
                    show_difficulty_selection = True
            elif show_difficulty_selection:
                if easy_rect.collidepoint(mouse_pos):
                    bot_difficulty = 'easy'
                    show_difficulty_selection = False
                elif medium_rect.collidepoint(mouse_pos):
                    bot_difficulty = 'medium'
                    show_difficulty_selection = False
                # elif hard_rect.collidepoint(mouse_pos):
                #     bot_difficulty = 'hard'
                #     show_difficulty_selection = False
            else:
                if restart_rect.collidepoint(mouse_pos) and not confirmation_active:
                    confirmation_active = True
                if confirmation_active:
                    if confirm_restart_rect and confirm_restart_rect.collidepoint(mouse_pos):
                        reset_game()
                    elif cancel_restart_rect and cancel_restart_rect.collidepoint(mouse_pos):
                        confirmation_active = False
                square = get_square_under_mouse()
                if square is not None:
                    if selected_square is None:
                        if board.piece_at(square):
                            selected_square = square
                    else:
                        move = chess.Move(selected_square, square)
                        if is_pawn_promotion(move):
                            move = chess.Move(
                                selected_square, square, promotion=pawn_promotion())
                        if move in board.legal_moves:
                            board.push(move)
                            pygame.display.flip()
                            selected_square = None
                            game_over_message = check_game_over()
                            if not game_over_message and game_mode == 'pvb':
                                bot_last_move = bot_move(bot_difficulty)
                                if bot_last_move:
                                    board.push(bot_last_move)
                                game_over_message = check_game_over()
                        else:
                            selected_square = None

    pygame.display.flip()


pygame.quit()
