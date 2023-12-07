import pygame
import sys
pygame.init()

class Cell:
    #initialization constructor
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.sketched_value = 0
        self.selected = False #tracking if the cell is selected or not
        self.size = 50

    #setter for the cell value
    def set_cell_value(self, value):
        self.value = value

    #setter for the sketched value of the cell
    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        #coordinates and constant variables
        xcord = self.col * self.size
        ycord = self.row * self.size

        cell_size = 50
        cell_border_color = (0, 0, 0) #black outline
        selected_cell_border_color = (255, 0, 0) #red outline
        font_color = (0, 0, 0)
        font_size = 20

        #cell rectangle
        cell = pygame.Rect(xcord, ycord, cell_size, cell_size)

        if self.selected:
            cell_border_color = selected_cell_border_color

        #draw cell
        pygame.draw.cell(self.screen, cell_border_color, cell, 3)

        #if the cell has a non-zero value, format the number in the cell box
        if self.value != 0:
            num_font = pygame.font.Font(None, font_size)
            text_style = pygame.font.render(str(self.value), font_color)
            text_rect = text_style.get_rect(center=cell.center)
            self.screen.blit(text_style, text_rect)

