class Matrix:
    def __init__(self, array):
        self.matrix = array

    def __add__(self, other):
        result = []

        for i in range(len(self.matrix)):
            result.append([0] * len(self.matrix[0]))

        for i in range(len(self.matrix)):
            for i2 in range(len(self.matrix[0])):
                result[i][i2] = self.matrix[i][i2] + other.matrix[i][i2]

        return Matrix(result)

    def __str__(self):
        result_str = ''
        for i in range(len(self.matrix)):
            result_str += ' '.join(map(str, self.matrix[i]))
            result_str += '\n'
        return result_str


matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matrix2 = [
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
]

m1 = Matrix(matrix1)
m2 = Matrix(matrix2)
final_result = m1 + m2

print(final_result)
