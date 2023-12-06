
import pygame
import random
import sys
import copy
# Initialize Pygame
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

......Classes

def show_win_screen(screen):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 72)
    win_text = font.render("GAME WON!", True, BLACK)
    text_rect = win_text.get_rect(center=(450 // 2, 450 // 4))
    screen.blit(win_text, text_rect)

    button_font = pygame.font.Font(None, 36)
    exit_button = pygame.draw.rect(screen, BLACK, (150, 320, 150, 50))
    exit_text = button_font.render("Exit Game", True, WHITE)
    screen.blit(exit_text, (165, 330))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def show_lose_screen(screen):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 72)
    lose_text = font.render("GAME LOST", True, BLACK)
    text_rect = lose_text.get_rect(center=(450 // 2, 450 // 4))
    screen.blit(lose_text, text_rect)

    button_font = pygame.font.Font(None, 36)
    restart_button = pygame.draw.rect(screen, BLACK, (150, 320, 150, 50))
    restart_text = button_font.render("Restart", True, WHITE)
    screen.blit(restart_text, (175, 330))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    main()  # Restart the game

# Function to display the start screen
def start_screen(screen):
    screen.fill(WHITE)

    # Display the title "Sudoku" on the start screen
    font = pygame.font.Font(None, 36)
    title_text = font.render("Sudoku", True, BLACK)
    text_rect = title_text.get_rect(center=(450 // 2, 450 // 4))
    screen.blit(title_text, text_rect)

    # Create buttons for easy, medium, and hard levels
    button_font = pygame.font.Font(None, 24)
    easy_button = pygame.draw.rect(screen, BLACK, (150, 200, 150, 50))
    medium_button = pygame.draw.rect(screen, BLACK, (150, 260, 150, 50))
    hard_button = pygame.draw.rect(screen, BLACK, (150, 320, 150, 50))

    easy_text = button_font.render("Easy", True, WHITE)
    medium_text = button_font.render("Medium", True, WHITE)
    hard_text = button_font.render("Hard", True, WHITE)

    screen.blit(easy_text, (175, 215))
    screen.blit(medium_text, (165, 275))
    screen.blit(hard_text, (175, 335))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    return 30
                elif medium_button.collidepoint(event.pos):
                    return 40
                elif hard_button.collidepoint(event.pos):
                    return 50
def draw_buttons(screen):
    button_font = pygame.font.Font(None, 24)

    exit_button = pygame.draw.rect(screen, BLACK, (50, 450, 100, 40))
    exit_text = button_font.render("Exit", True, WHITE)
    screen.blit(exit_text, (50 + 25, 455))

    restart_button = pygame.draw.rect(screen, BLACK, (175, 450, 100, 40))
    restart_text = button_font.render("Restart", True, WHITE)
    screen.blit(restart_text, (175 + 15, 455))

    reset_button = pygame.draw.rect(screen, BLACK, (300, 450, 100, 40))
    reset_text = button_font.render("Reset", True, WHITE)
    screen.blit(reset_text, (300 + 25, 455))

    return exit_button, restart_button, reset_button

# Main Game Logic
def main():
    pygame.mixer.music.load(r'audio\8bit-music-for-game-68698.mp3')
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    button_click_sound = pygame.mixer.Sound(r'audio\mouse-click-153941.mp3')
    screen = pygame.display.set_mode((450, 500))

    difficulty = start_screen(screen)  # Wait for user to select a difficulty
    button_click_sound.play()
    screen.fill(WHITE)
    board = Board(450 ,450, screen, difficulty)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.select_cell(event.pos)

            elif event.type == pygame.KEYDOWN:
                board.handle_key_input(event.key)
            if board.is_board_full():
                if board.is_board_correct():
                    show_win_screen(screen)
                    button_click_sound.play()
                    break
                else:
                    show_lose_screen(screen)
                    button_click_sound.play()
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    button_click_sound.play()
                    pygame.quit()
                    sys.exit()
                elif restart_button.collidepoint(event.pos):
                    button_click_sound.play()
                    main()  # Restart the game
                elif reset_button.collidepoint(event.pos):
                    button_click_sound.play()
                    # Reset the game board
                    board.reset_board()


        screen.fill(WHITE)
        board.draw()

        exit_button, restart_button, reset_button = draw_buttons(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()