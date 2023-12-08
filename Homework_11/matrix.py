class Matrix:

    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._columns = cols
        self._data = None

    def __str__(self):
        strings = []
        for row in self.data:
            strings.append(' '.join([str(i) for i in row]))
        return '\n'.join(strings)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: list):
        self._data = data

    def __repr__(self):
        return f"Matrix({self._rows}, {self._columns})"

    def __eq__(self, other: "Matrix") -> bool:
        if self._rows != other._rows or self._columns != other._columns:
            return False
        return all(map(lambda x, y: x == y,
                       (x for x in self.data),
                       (y for y in other.data)))

    def __add__(self, other: "Matrix") -> "Matrix":
        if self._rows != other._rows or self._columns != other._columns:
            return None
        result = Matrix(self._rows, self._columns)
        result.data = [[self.data[j][i] + other.data[j][i]
                        for i in range(self._columns)]
                       for j in range(self._rows)]
        return result

    def __mul__(self, other: "Matrix") -> "Matrix":
        result = Matrix(self._rows, other._columns)
        result.data = [[sum([self._data[i][k] * other._data[k][j]
                            for k in range(self._columns)])
                       for j in range(other._columns)]
                       for i in range(self._rows)]
        return result


if __name__ == "__main__":
    matrix3 = Matrix(3, 2)
    matrix3.data = [[1, 2], [3, 4], [5, 6]]
    print(matrix3 == matrix3)

    matrix4 = Matrix(2, 2)
    matrix4.data = [[7, 8], [9, 10]]

    result = matrix3 * matrix4
    print(matrix3, matrix4, result, sep='\n')
    print()
    print(matrix3 + matrix4)
    print()
    print(matrix3 + matrix3)
