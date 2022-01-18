class Queen:
    def __init__(self, row, column):
        if (not 8 > row >= 0) or (not 8 > column >0):
            raise ValueError("Queen must have a row from 0 to 7 and a column from 0 to 7.")
        self.row = row
        self.column = column

    def can_attack(self, other_queen):
        if self.row == other_queen.row and self.column == other_queen.column:
            raise ValueError("The two queens can not be on the same position.")
        return (self.row == other_queen.row) or (self.column == other_queen.column) or self.is_on_diagonal(other_queen)

    def is_on_diagonal(self, other_queen):
        # start in first row 
        start_col1 = self.column - self.row # diagonal from left to right
        start_col2 = self.column + self.row # diagonal from right to left
        diag_pos1 = ((0 + i, start_col1 + i)  for i in range(8)) # all positions on diag. from upper left to lower right
        diag_pos2 = ((0+i, start_col2 - i) for i in range(8)) # upper right to lower left
        return (other_queen.row, other_queen.column) in diag_pos1 or (other_queen.row, other_queen.column) in diag_pos2
 