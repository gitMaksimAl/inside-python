# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в
# аргументы matrix, и возвращает транспонированную матрицу.
import sys
matrix = [[1, 2, 3],
         [4, 5, 6], 
         [7, 8, 9]]


def transpose(matrix):
    length = len(matrix[0])
    for i in range(len(matrix) - 1):
        if len(matrix[i]) != length:
            return matrix
    matrix_t = []
    for i in range(length):
        column = []
        for j in range(len(matrix)):
            column.append(matrix[j][i])
        matrix_t.append(column)
    return matrix_t


print(matrix)
print(transposed_matrix:=transpose(matrix))

matrix = [[4, 7, 2, 1],
        [3, 9, 8, 6]]
print(matrix)
print(transposed_matrix:=transpose(matrix))

matrix = [[1]]
print(matrix)
print(transposed_matrix:=transpose(matrix))

