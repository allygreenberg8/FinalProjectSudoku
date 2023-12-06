class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.square_size = width / 9
        self.screen = screen
        self.difficulty = difficulty
        self.cells = []
        self.initial_values = []
        self.selected_cell = None
        size = 9
        removed = self.difficulty
        board = generate_sudoku(size, removed)
        self.make_board(board)

    def make_board(self, sodoku_board)
        self.initial_values = [[sudoku_board[row][col] for col in range(9)] for row in range(9)]
        for row in range(9):
            for col in range(9):
                cell = Cell(sudoku_board[row][col], row, col, self.screen)
                self.cells.append(cell)
                if sudoku_board[row][col] == 0:
                    cell.editable = True
                else:
                    cell.editable = False

    def reset_board(self):
        for i, cell in enumerate(self.cells):
            row = i // 9
            col = i % 9
            initial_value = self.initial_values[row][col]
            cell.value = initial_value
            cell.sketched_value = 0
            cell.selected = False
            if initial_value == 0:
                cell.editable = True
            else:
                cell.editable = False

    def draw(self):
        # Draw each cell
        for cell in self.cells:
            cell.draw()

        # Draw grid lines
        for x in range(0, self.width, int(self.square_size)):
            pygame.draw.line(self.screen, BLACK, (x, 0), (x, self.height))
        for y in range(0, self.height, int(self.square_size)):
            pygame.draw.line(self.screen, BLACK, (0, y), (self.width, y))

    def select_cell(self, pos):
        for cell in self.cells:
            if cell.is_clicked(pos) and cell.initially_empty and cell.editable:
                if self.selected_cell:
                    self.selected_cell.selected = False

                cell.selected = True
                self.selected_cell = cell
                return
        if self.selected_cell:
            self.selected_cell.selected = False
            self.selected_cell = None

    def handle_key_input(self, key):
        if self.selected_cell and self.selected_cell.initially_empty:

            if key >= pygame.K_1 and key <= pygame.K_9:
                self.selected_cell.set_sketched_value(int(chr(key)))  # Set temporary value

            elif key == pygame.K_RETURN and self.selected_cell.sketched_value != 0:
                self.confirm_value()  # Confirm value when 'Enter' is pressed

    def confirm_value(self):
        if self.selected_cell:
            self.selected_cell.set_cell_value(self.selected_cell.sketched_value)
            self.selected_cell.selected = False
            self.selected_cell = None

    def is_board_full(self):
        return all(cell.value != 0 for cell in self.cells)

    def is_board_correct(self):
        # Check each row, column, and 3x3 square
        for i in range(9):
            row = [self.cells[i * 9 + j].value for j in range(9)]
            col = [self.cells[j * 9 + i].value for j in range(9)]
            square = [self.cells[3 * (i // 3) * 9 + 3 * (i % 3) + j // 3 * 9 + j % 3].value for j in range(9)]

            if len(set(row)) != 9 or len(set(col)) != 9 or len(set(square)) != 9:
                return False
        return True