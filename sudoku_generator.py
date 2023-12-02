# Import random - to be used in unused_in_box function
import random

class SudokuGenerator:
    # Initialize
    def __init__(self, row_length=9, removed_cells=0):
        self.row_length = row_length
        self.removed_cells = removed_cells

    # 2. Get Board
    def get_board(self):
        return self.board

    # 3. Print Board
    def print_board(self):
        for row in self.board:
            print(row)

    # 4. Valid in row
    def valid_in_row(self, row, num):
        for i in range(self.row_length):
            if self.board[row][i] == num:
                return False
        return True

    # 5. Valid in col
    def valid_in_col(self, col, num):
        for i in range(self.row_length):
            if self.board[i][col] == num:
                return False
        return True

    # 6. Valid in box
    def valid_in_box(self, row_start, col_start, num):
        for i in range(3):
            for j in range(3):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    # 7. Is Valid
    def is_valid(self, row, col, num):
        # Checks if number is in valid range
        if num < 1 or num > 9:
            return False
        # Checks columns
        for i in range(9):
            if self.board[i][col] == num:
                return False
        # Checks rows
        for i in range(9):
            if self.board[row][i] == num:
                return False
        row_start = row - row % 3
        col_start = col - col % 3
        return self.valid_in_box(row_start, col_start, num)

    # Additional function to create unused nums to be implemented into Fill Box function.
    def unused_in_box(self, row_start, col_start):
        used_nums = set()
        for i in range(3):
            for j in range(3):
                used_nums.add(self.board[row_start + i][col_start + j])
        all_nums = set(range(1,10))
        unused_nums = list(all_nums - used_nums)
        random.shuffle(unused_nums)
        return unused_nums

    # 8. Fill box
    def fill_box(self, row_start, col_start):
        unused_nums = self.unused_in_box(row_start, col_start)
        for i in range(3):
            for j in range(3):
                self.board[row_start + i][col_start + j] = unused_nums.pop()

    # 9. Fill Diagonal
    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i,i)

    # 10. Fill remaining - provided
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    # 11. Fill Values - provided
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    # 12. Remove cells
    def remove_cells(self):
        cells = self.removed_cells
        while cells > 0:
            row, col = random.randint(0, self.row_length - 1), random.randint(0,self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells -= 1

    # Sudoku Generator - to be implemented outside of class
    # def generate_sudoku(size, removed):
        # sudoku = SudokuGenerator(row_length = size, removed_cells=removed)
        # sudoku.remove_cells()
        # return sudoku.get_board()