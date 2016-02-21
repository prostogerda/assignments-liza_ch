#! /usr/bin/env python


from __future__ import division, print_function
from itertools import izip


def p_distance(str1, str2):
    """
    Calculates distance between two aligned sequences with the same lengths
    as ratio of mismatched symbols to all pairs of symbols. Pairs with gaps are
    ignored.
    :type str1: str
    :param str1:
    :type str2: str
    :param str2:
    :return: ValueError, if strings have unequal length
    :return: int or float
    """
    GAP_SYMBOL = "-"
    if len(str1) != len(str2):
        raise ValueError("Strings have unequal length")
    mismatches = 0
    num_of_pairs = len(str1)
    for char1, char2 in izip(str1, str2):
        if char1 == GAP_SYMBOL or char2 == GAP_SYMBOL:
            num_of_pairs -= 1
            continue
        if char1 != char2:
            mismatches += 1
    return mismatches / num_of_pairs

p_distance("qqqqqwwwww", "qq-eqwwwww")


# Accept, that in alignment can't occur situation with (-, -) pair

def p_dist_nice(str1, str2):
    """
    Calculates distance between two aligned sequences with the same lengths as
    ratio of mismatched symbols to all pairs of symbols. Pairs with gaps are
    ignored.
    :type str1: str
    :param str1:
    :type str2: str
    :param str2:
    :return: ValueError, if strings have unequal length
    :return: int or float
    """
    GAP_SYMBOL = "-"
    if len(str1) != len(str2):
        raise ValueError("Strings have unequal length")
    return sum(char1 != char2 and char1 != GAP_SYMBOL and char2 != GAP_SYMBOL
               for char1, char2 in izip(str1, str2)
               ) / (len(str1) - str1.count("-") - str2.count("-"))


p_dist_nice("qqqqqwwwww", "qq-eqwwwww")


def matrix_multiplication(matr1, matr2):
    """
    Multiplies 2 matrixes with sizes (a*b) and (b*c). Result is matrix (a*c).

    :type matr1: list
    :param matr1: list of lists with integer or float numbers
    :type matr2: list
    :param matr2: list of lists with integer or float numbers
    :return: ValueError, if nrows in 1st matrix is not equal to ncols in 2nd
    matrix
    :return: ValueError, if there are not numerical values
    """
    nrow_matr1, ncol_matr1 = len(matr1), len(matr1[0])
    nrow_matr2, ncol_matr2 = len(matr2), len(matr2[0])
    if ncol_matr1 != nrow_matr2:
        raise ValueError("Number of rows in 1st matrix must be equal to "
                         "number of columns in 2nd matrix")
    matrix_mult_res = [[None for j in xrange(ncol_matr2)]
                       for i in xrange(nrow_matr1)]
    def get_col(matr, j):
        return [row[j] for row in matr]
    mult_result = 0
    for row in matr1:
        for i in xrange(nrow_matr1):
            for j in xrange(ncol_matr2):
                for k in xrange(ncol_matr1):
                    if not (isinstance(row[k], (int, float)) and
                                isinstance(get_col(matr2, j)[k], (int, float))):
                        raise ValueError("Matrix must consist of numbers")
                    mult_result += row[k] * get_col(matr2, j)[k]
                matrix_mult_res[i][j] = mult_result
                mult_result = 0
    return matrix_mult_res


m1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
m2 = [[2, 3, 4], [2, 3, 4], [2, 3, 4]]
matrix_multiplication(m1, m2)


def matrix_mult_2(matr1, matr2):
    """
    Same comments
    """
    nrow_matr1, ncol_matr1 = len(matr1), len(matr1[0])
    nrow_matr2, ncol_matr2 = len(matr2), len(matr2[0])
    if ncol_matr1 != nrow_matr2:
        raise ValueError("Number of rows in 1st matrix must be equal to "
                         "number of columns in 2nd matrix")
    matrix_mult_res = [[None for j in xrange(ncol_matr2)]
                       for i in xrange(nrow_matr1)]

    def get_col(matr, j):
        return [row[j] for row in matr]

    def get_value(row, col):
        # if not isinstance(row[k], (int, float)) and isinstance(col[k],
        #                                                        (int, float)):
        #     raise ValueError("Matrix must consist of numbers")
        # What happens with outer function. if raise appears here?
        return sum(row[k] * col[k] for k in xrange(ncol_matr1))

    for i in xrange(nrow_matr1):
        for j in xrange(ncol_matr2):
            matrix_mult_res[i][j] = get_value(matr1[i], get_col(matr2, j))
    return matrix_mult_res


m1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
m2 = [[2, 3, 4], [2, 3, 4], [2, 3, 4]]
m3 = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
m4 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
matrix_mult_2(m1, m2)
matrix_mult_2(m3, m4)