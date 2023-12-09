import pygame
import sys
pygame.init()
from FINALsudoku_generator import SudokuGenerator

class Cell:
    # cell class variables
    size = 50

    #initialization constructor
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.sketched_value = 0
        self.selected = False #tracking if the cell is selected or not

        # drawing variables, coordinates and constant variables
        self.xcord = (self.col) * self.size
        self.ycord = (self.row) * self.size

        self.cell_border_color = "black "  # black outline

        self.cell = pygame.Rect(self.xcord, self.ycord, self.size, self.size)

    def get_col(self):
        return self.col

    def get_row(self):
        return self.row

    # setter for the cell value
    def set_cell_value(self, value):
        self.value = value

    def get_sketched_value(self):
        return self.sketched_value

    # setter for the sketched value of the cell
    def set_sketched_value(self, value):
        self.sketched_value = value

    # draw function
    def draw(self):

        if self.selected:
            self.cell_border_color = "red"

        # draw rectangle
        pygame.draw.rect(self.screen, self.cell_border_color, self.cell, width = 1)

        #if the cell has a non-zero value, format the number in the cell box
        if self.value != 0:
            num_font = pygame.font.Font(None, 20)
            num = num_font.render(str(self.value), True, "black")
            numRect = num.get_rect(center=self.cell.center)
            self.screen.blit(num, numRect)

    # draw a sketched cell
    def draw_sketched(self):
        pygame.draw.rect(self.screen, "black", self.cell, width=1)

        num_font = pygame.font.Font(None, 20)
        num = num_font.render(str(self.sketched_value), True, "black")
        numRect = num.get_rect(center=self.cell.center)
        self.screen.blit(num, numRect)


