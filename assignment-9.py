#! /usr/bin/env python


from __future__ import division, print_function


def longest_nonincreasing_subseq_sqr(seq):
    """
    Finds one of longest nonincreasing subsequences in sequence.
    complexity ~ len(seq)**2
    :type seq: collections.Sequence[int]
    :param seq:
    :return:
    :rtype: list
    """
    best_subtasks = [1] * len(seq)
    best_subseq_rev = [None]
    best_subseq = []
    for i in xrange(1, len(seq)):
        for j in xrange(0, i):
            if seq[i] <= seq[j]:
                best_subtasks[i] = max(best_subtasks[j]+1, best_subtasks[i])
    current_best_len = max(best_subtasks)
    for num in reversed(seq):
        if best_subtasks[-1] == current_best_len and num >= best_subseq_rev[-1]:
            best_subseq_rev.append(num)
            current_best_len -= 1
        best_subtasks.pop()
    best_subseq.extend(item for item in reversed(best_subseq_rev))
    return best_subseq.pop() or best_subseq


def longest_nonincreasing_subseq_log(seq):
    pass


def longest_common_subseq(seq1, seq2):
    """
    Finds one of longest common subsequences in two sequences
    :type seq1: collections.Sequence
    :param seq1:
    :type seq2: collections.Sequence
    :param seq2:
    :return:
    :rtype: list
    """
    solution_matrix = [[0] * (len(seq1) + 1) for _ in xrange(len(seq2) + 1)]
    subseq_reversed = []
    subseq = []
    #  note: solution_matrix has one extra row and column for empty subsequences
    for i in xrange(1, len(seq2)+1):
        for j in xrange(1, len(seq1)+1):
            solution_matrix[i][j] = (solution_matrix[i-1][j-1] + 1
                                     if seq2[i-1] == seq1[j-1]
                                     else max(solution_matrix[i-1][j],
                                              solution_matrix[i][j-1]))
    while i and j:
        if solution_matrix[i][j] == solution_matrix[i][j-1]:
            j -= 1
        elif solution_matrix[i][j] == solution_matrix[i-1][j]:
            i -= 1
        else:
            subseq_reversed.append(seq2[i-1])
            i -= 1
            j -= 1
    return subseq.extend(item for item in reversed(subseq_reversed)) or subseq


def test_subseq():
    seq1 = "qwertyff"
    seq2 = "aswfvtmj5yffff"
    longest_common_subseq(seq1, seq2)


def test_nonincreasing_sqr():
    seq = [7, 7, 7, 6, 5, 10, 4, 9, 8, 8, 7, 2, -1]
    longest_nonincreasing_subseq_sqr(seq)


def test_nonincreasing_log():
    seq = [12, 10, 8, 22, 0, -7]
    longest_nonincreasing_subseq_log(seq)
    pass


def main():
    test_subseq()
    test_nonincreasing_sqr()
    test_nonincreasing_log()


if __name__ == '__main__':
    main()


# while i and j:
#     i, j = next(i_, j_) for i_, j_ in ((i-1, j), (i, j-1), (i-1, j-1)) if  else
#
