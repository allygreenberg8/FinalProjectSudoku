class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.fill_values()
        self.remove_cells()

        self.random_module = __import__('random')

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(self.row_length)]

    def valid_in_box(self, row_start, col_start, num):
        for i in range(3):
            for j in range(3):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    def fill_box(self, row_start, col_start):
        nums = list(range(1, 10))
        self.random_module.shuffle(nums)
        for i in range(3):
            for j in range(3):
                num = nums.pop()
                while not self.valid_in_row(row_start + i, num) or not self.valid_in_col(col_start + j, num):
                    nums.insert(0, num)
                    num = nums.pop()
                self.board[row_start + i][col_start + j] = num

    def is_valid(self, row, col, num):
        # Check if the number is not in the given row
        if num in self.board[row]:
            return False

        # Check if the number is not in the given column
        if num in [self.board[r][col] for r in range(self.row_length)]:
            return False

        # Check if the number is not in the 3x3 box
        row_start = row - row % 3
        col_start = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[row_start + i][col_start + j] == num:
                    return False

        return True

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    def fill_remaining(self, i, j):
        if j >= self.row_length and i < self.row_length - 1:
            i += 1
            j = 0
        if i >= self.row_length and j >= self.row_length:
            return True
        if i < 3:
            if j < 3:
                j = 3
        elif i < 6:
            if j == int(i / 3) * 3:
                j += 3
        else:
            if j == 6:
                i += 1
                j = 0
                if i >= self.row_length:
                    return True
        for num in range(1, 10):
            if self.valid_in_row(i, num) and self.valid_in_col(j, num) and self.valid_in_box(i - i % 3, j - j % 3, num):
                self.board[i][j] = num
                if self.fill_remaining(i, j + 1):
                    return True
                self.board[i][j] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, 0)

    def remove_cells(self):
        count = self.removed_cells
        while count > 0:
            i = self.random_module.randint(0, 8)
            j = self.random_module.randint(0, 8)
            if self.board[i][j] != 0:
                count -= 1
                self.board[i][j] = 0

    def get_board(self):
        return self.board


def generate_sudoku(self, size, removed):
    generator = SudokuGenerator(row_length=size, removed_cells=removed)
    sudoku_board = generator.get_board()
    return sodoku_board