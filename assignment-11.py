#! /usr/bin/env python3


def change(total, coins):
    """
    Finds minimal set of given coins, from which given sum may be collected.
    :type total: int
    :param total:
    :type coins: collections.Sequence(int)
    :param coins: Sorted, increasing list. Must begin with nominal "1"
    :return: list of coins
    :rtype: tuple(int)
    """
    solution_matrix = [[0] * (total+1) for _ in range(len(coins))]
    # extra col for zero sum
    for j in range(0, total+1):
        solution_matrix[0][j] = j
    # adds 0, 1, 2 ... in 1st row, because we can collect given sum of
    # coins with nominal "1" in only one way
    coins_res = []
    for i in range(1, len(coins)):
        curr_coin = coins[i]
        # I understand, that previous step isn't necessary, but, as for me, it
        # "explains" the sense of coins[i]
        for j in range(0, total + 1):
            if j < curr_coin:
                solution_matrix[i][j] = solution_matrix[i-1][j]
            else:
                solution_matrix[i][j] = min(solution_matrix[i-1][j],
                                            solution_matrix[i][j-1] + 1,
                                            solution_matrix[i][j-curr_coin]+1)
            # calculates values by finding minimum value in 3 cells
    while i and j:
        # Finds cell, from which we came to current cell (by "minimal" rule)
        # In dependence of result comes to appropriate cell and adds to result
        # appropriate coin
        if solution_matrix[i][j] == solution_matrix[i-1][j]:
            i -= 1
            curr_coin = coins[i]
        elif solution_matrix[i][j] == solution_matrix[i][j-1] + 1:
            coins_res.append(1)  # "1" means the coin with nominal "1"
            j -= 1
        else:
            coins_res.append(curr_coin)
            j -= curr_coin
    return coins_res


def test_coins():
    coins = [1, 4, 6, 10]
    total = 18
    change(total, coins)
    coins = [1, 2, 5, 10]
    total = 19
    change(total, coins)


class Matrix():
    """
    Object with properties of mathematical matrix
    Can be transposed (change columns and rows)
    Can be compared with another matrices (equal or not).
    Can be added to number or another matrix with the same size.
    Can be multiplicated on another matrix or number
    """
    def __init__(self, values): # matr_type=None:
        if isinstance(values, int): # matrix of one element
            self._values = [[values]]
        elif (isinstance(values, (tuple, list))
              and isinstance(values[0], (tuple, list))):
            # "rewrite" matrix, when gets smth like tuple(list, list...) or
            # list[tuple, tuple...] or tuple(tuple, tuple...) to make it
            # changeable
            self._values = [[None] * len(values[0]) for _ in range(len(values))]
            for i in range(0, len(values)):
                for j in range(0, len(values[0])):
                    self._values[i][j] = values[i][j]
        elif isinstance(values, (tuple, list)) and isinstance(values[0], int):
            # when we have only one list or tuple, we can make from it
            # row_vector (default) or column_vector
            self._values = [[None] * len(values)]
            for j in range(0, len(values)):
                self._values[0][j] = values[j]
            # if matr_type == column_vector:
            #     self.transpose()
        else:
            raise ValueError
        self._ncol = len(self._values[0])
        self._nrow = len(self._values)

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        self._values = values

    @property
    def ncol(self):
        return self._ncol

    @property
    def nrow(self):
        return self._nrow

    def __str__(self):
        # I don't sure that I understood correctly, what you asked to do.
        for i in range(0, self.nrow):
            print(self.values[i])

    def __eq__(self, other):
        """
        :type other: Matrix
        :param other:
        :return:
        """
        if (self.ncol != other.ncol) or (self.nrow != other.nrow):
            return False
        for i in range(0, self.nrow):
            for j in range(0, self.ncol):
                if self.values[i][j] != other.values[i][j]:
                    return False
        return True

    def __ne__(self, other):
        return not self.values == other.values

    def transpose(self):
        new_matr = Matrix([[None] * self.nrow for _ in range(self.ncol)])
        for i in range(0, self.nrow):
            for j in range(0, self.ncol):
                new_matr.values[j][i] = self.values[i][j]
        self._values = new_matr.values

    def __add__(self, other):
        """
        Adds to matrix number or another matrix
        :param other:
        :return:
        """
        matrix_sum = Matrix([[None] * self.ncol for _ in range(self.nrow)])
        if isinstance(other, int):
            # Adds number to all cells
            for i in range(0, self.nrow):
                for j in range(0, self.ncol):
                    matrix_sum.values[i][j] = self.values[i][j] + other
        elif isinstance(other, Matrix):
            if self.ncol != other.ncol or self.nrow != other.nrow:
                raise ValueError("Matrices have unequal sizes")
            # Sums appropriate cells in 2 matrices
            for i in range(0, self.nrow):
                for j in range(0, self.ncol):
                    matrix_sum.values[i][j] = self._values[i][j] + other.values[i][j]
        else:
            raise ValueError("Incorrect type of added element")
        return matrix_sum

    def __sub__(self, other):
        return self + (-1 * other)

    def __radd__(self, other):
        return self + other

    @staticmethod
    def _multiply(matr1, matr2):
        """
        :type matr1: Matrix
        :param matr1:
        :type matr2: Matrix
        :param matr2:
        :return:
        """
        if matr1.ncol != matr2.nrow:
            raise ValueError("Number of rows in 1st matrix must be equal to "
                             "number of columns in 2nd matrix")
        matrix_mult_res = [[None for j in range(matr2.ncol)]
                           for i in range(matr1.nrow)]

        def get_col(matrix, j):
            return [row[j] for row in matrix.values]

        def get_value(row, col):
            return sum(row[k] * col[k] for k in range(matr1.ncol))

        for i in range(matr1.nrow):
            for j in range(matr2.ncol):
                matrix_mult_res[i][j] = get_value(matr1.values[i],
                                                  get_col(matr2, j))
        return matrix_mult_res

    def __mul__(self, other):
        if isinstance(other, int):
            # multiplicates all cells to number
            matrix_mul = Matrix([[None] * self.ncol
                                 for _ in range(self.nrow)])
            for i in range(0, self.nrow):
                for j in range(0, self.ncol):
                    matrix_mul.values[i][j] = self.values[i][j] * other
        elif isinstance(other, Matrix):
            # multiplicates 2 matrices
            matrix_mul = Matrix(self._multiply(self, other)) # looks strange...
        else:
            raise ValueError("Incorrect type of multiplier")
        return matrix_mul

    def __rmul__(self, other):
        if not isinstance(other, Matrix):
            return self * other
        return self._multiply(other, self)


def test_matrix():
    matr = Matrix([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
    matr.transpose()
    str(matr)
    w = Matrix([[1, 2, 4], [1, 3, 3], [1, 2, 3], [1, 2, 3]])
    e = Matrix([[2, 3, 4, 5], [2, 7, 4, 5], [1, 3, 4, 5]])
    str(w * e)


def main():
    test_coins()
    test_matrix()


if __name__ == '__main__':
    main()
