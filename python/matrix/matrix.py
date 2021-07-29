class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.matrix = [[int(element) for element in row.split()]
                       for row in matrix_string.splitlines()]

    def row(self, index: int) -> list[int]:
        # Index of matrix starts with 1, not with 0.
        return self.matrix[index-1].copy()

    def column(self, index: int) -> list[int]:
        # Index of matrix starts with 1, not with 0.
        return [row[index-1] for row in self.matrix]
