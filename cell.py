# Cell Class
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.value = value
        self.initially_empty = value == 0
        self.editable = value == 0

        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False
        self.size = 50

    def set_cell_value(self, value):
        if self.editable:
            self.value = value
            self.editable = False

    def is_clicked(self, pos):
        xcord = self.col * self.size
        ycord = self.row * self.size
        return pygame.Rect(xcord, ycord, self.size, self.size).collidepoint(pos)

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        xcord = self.col * self.size
        ycord = self.row * self.size
        cell_size = 50
        cell_border_color = BLACK
        selected_cell_border_color = (255, 0, 0)  # red outline
        font_color = BLACK
        sketched_font_color = (128, 128, 128)  # light gray for sketched value
        font_size = 20

        cell = pygame.Rect(xcord, ycord, cell_size, cell_size)

        if self.selected:
            cell_border_color = selected_cell_border_color

        pygame.draw.rect(self.screen, cell_border_color, cell, 3)

        num_font = pygame.font.Font(None, font_size)

        # Draw sketched value in light gray if it exists and is different from the confirmed value
        if self.sketched_value != 0 and self.sketched_value != self.value:
            text_style = num_font.render(str(self.sketched_value), True, sketched_font_color)
            text_rect = text_style.get_rect(center=cell.center)
            self.screen.blit(text_style, text_rect)
        # Draw confirmed value in black
        elif self.value != 0:
            text_style = num_font.render(str(self.value), True, font_color)
            text_rect = text_style.get_rect(center=cell.center)
            self.screen.blit(text_style, text_rect)
