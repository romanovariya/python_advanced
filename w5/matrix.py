import copy


class MatrixSizeError(Exception):
    pass


class Matrix:
    # Part 1
    def __init__(self, matrix):
        rows_len = len(matrix[0])
        for row in matrix:
            if len(row) != rows_len:
                raise MatrixSizeError
        self.matrix = copy.deepcopy(matrix)
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        line = ''
        for row in self.matrix:
            row = [str(i) for i in row]
            line += "\t".join(row)
            line += '\n'
        return line[:-1:]

    # Part 2
    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise MatrixSizeError
            else:
                for i in range(self.rows):
                    for j in range(self.cols):
                        if self.matrix[i][j] != other.matrix[i][j]:
                            return False
                return True
        else:
            raise TypeError

    def size(self):
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        res_tuple = (rows, columns)
        return res_tuple

    # Part 3
    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise MatrixSizeError
            else:
                sum_matrix = []
                for i in range(self.rows):
                    sum_matrix.append([])
                    for j in range(self.cols):
                        sum_matrix[i].append(self.matrix[i][j] +
                                             other.matrix[i][j])
                return Matrix(sum_matrix)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise MatrixSizeError
            else:
                sub_matrix = []
                for i in range(self.rows):
                    sub_matrix.append([])
                    for j in range(self.cols):
                        sub_matrix[i].append(self.matrix[i][j] -
                                             other.matrix[i][j])
                return Matrix(sub_matrix)
        else:
            raise TypeError

    # Part 4
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise MatrixSizeError
            else:
                mul_matrix = [[sum(a * b for a, b in zip(x_row, y_col))
                               for y_col in zip(*other.matrix)]
                              for x_row in self.matrix]
                return Matrix(mul_matrix)
        else:
            raise TypeError

    # Part 5
    def transpose(self):
        transposed_matrix = []
        for i in range(self.cols):
            transposed_matrix.append([])
            for j in range(self.rows):
                transposed_matrix[i].append(self.matrix[j][i])
        return Matrix(transposed_matrix)
    # Part 6

    def tr(self):
        if self.rows == self.cols:
            res = 0
            i = 0
            j = 0
            while i < self.rows:
                while j < self.cols:
                    res += self.matrix[i][j]
                    j += 1
                    i += 1
            return res
        else:
            raise MatrixSizeError

    def det(self):
        if self.rows == self.cols:
            n = self.rows
            am = copy.copy(self.matrix)

            for fd in range(n):
                for i in range(fd+1, n):
                    if am[fd][fd] == 0:
                        am[fd][fd] == 1.0e-18
                    cr_scaler = am[i][fd] / am[fd][fd]
                    for j in range(n):
                        am[i][j] = am[i][j] - cr_scaler * am[fd][j]

            product = 1.0
            for i in range(n):
                product *= am[i][i]
            return round(product)
        else:
            raise MatrixSizeError
