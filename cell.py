import tkinter as tk

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
        xcord_1 = self.col * self.size
        ycord_1 = self.row * self.size

        xcord_2 = xcord_1 + self.size
        ycord_2 = ycord_1 + self.size

        font_name = "Arial"
        font_size = 20

        #draw the cell border
        self.screen.create_rectangle(xcord_1, ycord_1, xcord_2, ycord_2, fill="white")

        #cases if the cell has a non zero value
        if self.value != 0:
            self.screen.create_text(xcord_1 + self.size//2, ycord_1 + self.size//2, text=str(self.value), font=(font_name, font_size))
        elif self.sketched_value != 0:
            font_size = 15
            self.screen.create_text(xcord_1 + self.size // 2, ycord_1 + self.size // 2, text=str(self.value), font=(font_name, font_size))

        #changes the border to red if selected
        if self.selected:
            self.screen.create_rectangle(xcord_1, ycord_1, xcord_2, ycord_2, outline="red")