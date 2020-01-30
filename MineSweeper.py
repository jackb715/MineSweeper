from random import seed
from random import randint


class Cell:
    visible = False
    value = 0

    def __init__(self):
        self.visible = False
        self.value = 0


class Field:
    num_col = 0
    num_row = 0
    matrix = [[]]
    num_bombs = 0

    def __init__(self, col, row, bombs):
        self.num_col = col
        self.num_row = row
        self.num_bombs = bombs
        self.matrix = [[Cell() for j in range(self.num_col)] for i in range(self.num_row)]
        self.bomb_coordinates = []

    # Populates board with bomb and initializes cell values
    def populate(self, col_init, row_init):
        click_init = [row_init, col_init]
        i = 0
        while i < self.num_bombs:
            row = randint(1, self.num_col)
            col = randint(1, self.num_row)
            coordinate = [row, col]
            if self.bomb_coordinates.__contains__(coordinate) or coordinate == click_init:
                i = i-1         # Choose a different coordinate
            else:
                self.bomb_coordinates.add(coordinate)
                self.matrix[row][col].value = -1        # Make the coordinate a bomb
                i = i+1
        for j in self.bomb_coordinates:
            adjacents = self.bomb_coordinates[j].adjacents
            for i in adjacents:
                adjacents[i].value = adjacents[i].value + 1

    def click(self, row, col):
        # either a bomb
        if self.bomb_coordinates.__contains__([row, col]):
            # Reveal entire board
            for j in range(self.num_bombs):
                for i in range(self.num_row):
                    self.matrix[row][col].visible = True
        # or a number
        elif self.matrix[row][col].value > 0:
            self.matrix[row][col].visible = True
        # Cell is blank
        else:
            self.matrix[row][col].visible = True
            adjacents = self.get_adjacent_cells(row, col)
            for i in adjacents:
                if self.bomb_coordinates.__contains__(adjacents[i]):
                    return
                else:
                    coordinate = adjacents[i]
                    self.click(coordinate[0], coordinate[1])

    # Determines if a cell coordinate is valid
    def is_cell_valid(self, row, col):
        if row > self.num_row or col > self.num_col:
            return False

        elif row < 0 or col < 0:
            return False

        else:
            return True

    # returns a list of valid cell coordinates adjacent to a particular cell
    def get_adjacent_cells(self, row, col):
        adjacents = []
        j = 0
        i = 0
        while j < 3:
            while i < 3:
                if self.is_cell_valid(row - 1 + j, i - 1 + i) and (row != row - 1 + j and col != col - 1 + i):
                    adjacents.add([row - 1 + j, i - 1 + i])
                i = i + 1
            j = j + 1
        return adjacents

    def print_field(self):
        line=""
        separator = ""
        for i in range(self.num_col):
            separator+="---"
        for i in range(self.num_row):
            print(separator)
            for j in range(self.num_col):
                if self.matrix[i][j].visible:
                    line+= "|" + str(self.matrix[i][j].value) + "|"
                else:
                    line+= "| |"
            print(line)
            line = ""

# Main method .......
test_field = Field(3,3,3)

test_field.click(0,0)
test_field.click(0,1)
test_field.print_field()

