import pygame, sys
pygame.init()
from FINALcell import Cell
pygame.display.init
from FINALsudoku_generator import SudokuGenerator

class Board():

    # constructor
    def __init__(self, width, height, screen, difficulty, correctValues, trueValues):
        self.width = 450
        self.height = 450
        self.square_size = width/9
        self.screen = screen
        self.difficulty = difficulty
        self.correctValues = correctValues
        self.trueValues = trueValues # edit to check board
        self.cells = []
        self.selected_cell = Cell(0, 0, 0, self.screen)

        self.row1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.row2 = [9, 10, 11, 12, 13, 14, 15, 16, 17]
        self.row3 = [18, 19, 20, 21, 22, 23, 24, 25, 26]
        self.row4 = [27, 28, 29, 30, 31, 32, 33, 34, 35]
        self.row5 = [36, 37, 38, 39, 40, 41, 42, 43, 44]
        self.row6 = [45, 46, 47, 48, 49, 50, 51, 52, 53]
        self.row7 = [54, 55, 56, 57, 58, 59, 60, 61, 62]
        self.row8 = [63, 64, 65, 66, 67, 68, 69, 70, 71]
        self.row9 = [72, 73, 74, 75, 76, 77, 78, 79, 80]

        self.cells_to_check = []


    # draw function - DONE
    def draw(self):

        # make background white
        self.screen.fill("white")

        # set lineWidth var
        lineWidth = 0

        # draw horizontal lines
        for i in range(1, 9):
            # set the bold for the 3x3 lines
            if i == 3 or i == 6:
                lineWidth = 6
            else:
                lineWidth = 2

            # draw the line
            pygame.draw.line(self.screen, "black",
                             (0, i * self.square_size),
                             (self.width, i * self.square_size),
                             lineWidth)

        # draw vertical lines
        for i in range(1, 9):
            # set the bold for the 3x3 lines
            if i == 3 or i == 6:
                lineWidth = 6
            else:
                lineWidth = 2

            # draw the line
            pygame.draw.line(self.screen, "black",
                             (i * self.square_size, 0),
                             (i * self.square_size, self.height),
                             lineWidth)

        # create the 81 cells and put them in the cell list
        # name of cells is their index
        for row in range(0, 9):
            for col in range(0, 9):
                newCell = Cell(0, row, col, self.screen)
                newCell.set_cell_value(self.correctValues[row][col])
                self.cells.append(newCell)
                newCell.draw()



    # select function - marks cell as current selected cell - DONE
    def select(self, row, col):
        ind = 0

        if row == 1:
            ind = self.row1[col-1]
        elif row == 2:
            ind = self.row2[col-1]
        elif row == 3:
            ind = self.row3[col-1]
        elif row == 4:
            ind = self.row4[col-1]
        elif row == 5:
            ind = self.row5[col-1]
        elif row == 6:
            ind = self.row6[col-1]
        elif row == 7:
            ind = self.row7[col-1]
        elif row == 8:
            ind = self.row8[col-1]
        elif row == 9:
            ind = self.row9[col-1]

        self.selected_cell = self.cells[ind]
        self.cells[ind].selected = True
        self.cells[ind].draw()



    # click function - returns row and col of coordinate - DONE
    def click(self, x, y):
        if x > self.width or y > self.height:
            return None
        else:
            row = 0
            col = 0

            if y < self.square_size:
                row = 1
            elif y < 2*self.square_size:
                row = 2
            elif y < 3*self.square_size:
                row = 3
            elif y < 4*self.square_size:
                row = 4
            elif y < 5*self.square_size:
                row = 5
            elif y < 6*self.square_size:
                row = 6
            elif y < 7*self.square_size:
                row = 7
            elif y < 8*self.square_size:
                row = 8
            elif y < 9 * self.square_size:
                row = 9


            if x < self.square_size:
                col = 1
            elif x < 2*self.square_size:
                col = 2
            elif x < 3*self.square_size:
                col = 3
            elif x < 4*self.square_size:
                col = 4
            elif x < 5*self.square_size:
                col = 5
            elif x < 6*self.square_size:
                col = 6
            elif x < 7*self.square_size:
                col = 7
            elif x < 8*self.square_size:
                col = 8
            elif x < 9*self.square_size:
                col = 9

            return (row, col)

    # clear function - empty out selected cell - DONE
    def clear(self):
        self.selected_cell = ""



    # sketch function - set value of sketched cell and draw it - DONE
    def sketch(self, value):
        self.selected_cell.set_sketched_value(value)
        self.selected_cell.draw_sketched()
        self.cells_to_check.append(self.selected_cell)



    # sets value of cell equal to input value - DONE
    def place_number(self, value):
        self.selected_cell.set_cell_value(value)



    # sets all cells to original value; 0 if cleared - DONE
    def reset_to_original(self):
        for cell in self.cells:
            cell.set_sketched_value(cell.value)



    # is full function - returns boolean of whether board full or not - DONE
    def is_full(self):
        count = 0
        for cell in self.cells:
            if cell.get_sketched_value() != 0:
                count+=1
        ans = 0

        if self.difficulty == 30:
            ans = 30
        elif self.difficulty == 40:
            ans = 40
        elif self.difficulty == 50:
            ans = 50

        if count == ans:
            return True
        else:
            return False


        '''
       full = False
        try:
            for cell in self.cells:
                if 0 < cell.sketched_value <= 9:
                    full = True
                else:
                    raise NameError
            return full

        except:
            return False
            
            
            
        if self.find_empty() == None:
            return False
        else:
            return True
        
        '''




    # update board func - updates underlying 2d board with values in all cells
    def update_board(self):
        for cell in self.cells:
            cell.set_cell_value(cell.selected_value)



    # find empty func - returns row + col of an empty cell - DONE
    def find_empty(self):
        empty = ""
        for cell in self.cells:
            if cell.sketched_value == 0:
                empty = str(self.cells.index(cell))
                break
        row = 0
        col = 0

        if empty in self.row1:
            row = 1
            col = self.row1.index(empty)
        elif empty in self.row2:
            row = 2
            col = self.row2.index(empty)
        elif empty in self.row3:
            row = 3
            col = self.row3.index(empty)
        elif empty in self.row4:
            row = 4
            col = self.row4.index(empty)
        elif empty in self.row5:
            row = 5
            col = self.row5.index(empty)
        elif empty in self.row6:
            row = 6
            col = self.row6.index(empty)
        elif empty in self.row7:
            row = 7
            col = self.row7.index(empty)
        elif empty in self.row8:
            row = 8
            col = self.row8.index(empty)
        elif empty in self.row9:
            row = 9
            col = self.row9.index(empty)

        if row == 0:
            return None
        else:
            return (row, col)



    # checks if board is solved correctly - DONE
    def check_board(self):
        for cell in self.cells_to_check:
            correct = 0
            ans = 0
            count = 0
            correctCount = 0

            if self.difficulty == 30:
                correctCount = 30
            elif self.difficulty == 40:
                correctCount = 40
            elif self.difficulty == 50:
                correctCount = 50

            for cell in self.cells_to_check:
                row = cell.get_row()
                col = cell.get_col()
                location = str(row) + str(col)
                ans = self.trueValues[location]
                if ans == cell.get_sketched_value():
                    count += 1

            if count == correctCount:
                return True
            else:
                return False



        '''
        correct = 0
        ans = 0


        for cell in self.cells_to_check:
            if cell.sketched_value == cell.value:
                correct += 1

        if self.difficulty == 30:
            ans = 30
        elif self.difficulty == 40:
            ans = 40
        elif self.difficulty == 50:
            ans = 50

        if correct == ans:
            return True
        else:
            return False
        '''


'''
# keep program running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
'''
