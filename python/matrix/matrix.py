class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        for row in matrix_string.splitlines():
            self.matrix.append([int(element) for element in row.split()])

    def row(self, index):
        # Index of matrix starts with 1, not with 0.
        return self.matrix[index-1]

    def column(self, index):
        # Index of matrix starts with 1, not with 0.
        return [row[index-1] for row in self.matrix]
