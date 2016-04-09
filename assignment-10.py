#! /usr/bin/env python


from __future__ import division, print_function
import itertools


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
    best_subseq_rev = []
    best_subseq = []
    for i in xrange(1, len(seq)):
        for j in xrange(0, i):
            if seq[i] <= seq[j]:
                best_subtasks[i] = max(best_subtasks[j]+1, best_subtasks[i])
    current_best_len = max(best_subtasks)
    for num, subtask in itertools.izip(reversed(seq), reversed(best_subtasks)):
        # we go from end to begin in our seq and in best_subtasks
        if subtask == current_best_len:
            # when we find subtask, which length is equal to current best len,
            # we check, is this the part of our subsequence
            if not best_subseq_rev or num >= best_subseq_rev[-1]:
                # we append next number if result list is empty
                # or num >= last element in our subsequence.
                # >= - because we go from end to begin. So best_subseq_rev must
                # be nondecreasing
                best_subseq_rev.append(num)
                current_best_len -= 1
                # now we need to find next subtask with  less length
        if not current_best_len:
            break
            # end of iteration if current_best_len == 0, which means, that we
            # found all our subsequence
    # rewrite result in correct order
    return best_subseq.extend(reversed(best_subseq_rev)) or best_subseq


def align(seq1, seq2):
    """
    Aligns two sequences.
    Costs of mismatches and gaps in both sequences are equal (= 1).
    :type seq1: collections.Sequence
    :param seq1:
    :type seq2: collections.Sequence
    :param seq2:
    :return: Two sequences with gaps
    :rtype: tuple(str, str)
    """
    solution_matrix = [[0] * (len(seq1) + 1) for _ in xrange(len(seq2) + 1)]
    #  note: solution_matrix has one extra row and column for empty subsequences
    for j in xrange(0, len(seq1)+1):
        solution_matrix[0][j] = j
    # adds 0, 1, 2 ... in 1st row
    # Necessary for correct calculation of values in next row
    for i in xrange(0, len(seq2)+1):
        solution_matrix[i][0] = i
    # adds 0, 1, 2 ... in 1st column
    # Necessary for correct calculation of values in next column
    GAP_SYMBOL = "-"
    sol_seq1_rev = []
    sol_seq2_rev = []
    sol_seq1 = ""
    sol_seq2 = ""
    for i in xrange(1, len(seq2)+1):
        for j in xrange(1, len(seq1)+1):
            solution_matrix[i][j] = min(solution_matrix[i-1][j-1] +
                                        (seq2[i-1] != seq1[j-1]),
                                        solution_matrix[i-1][j] + 1,
                                        solution_matrix[i][j-1] + 1)
            # calculates values by finding minimum value in 3 previous cells
    while i or j:
        # Finds cell, from which we came to current cell (by "minimal" rule)
        # In dependence of result comes to appropriate cell and adds to result
        # letter or gap symbol
        if solution_matrix[i][j] == solution_matrix[i][j-1] + 1:
            sol_seq1_rev.append(seq1[j-1])
            sol_seq2_rev.append(GAP_SYMBOL)
            j -= 1
        elif solution_matrix[i][j] == solution_matrix[i-1][j] + 1:
            sol_seq2_rev.append(seq2[i-1])
            sol_seq1_rev.append(GAP_SYMBOL)
            i -= 1
        else:
            sol_seq1_rev.append(seq1[j-1])
            sol_seq2_rev.append(seq2[i-1])
            i -= 1
            j -= 1
    sol_seq1 = "".join(reversed(sol_seq1_rev))
    sol_seq2 = "".join(reversed(sol_seq2_rev))
    # reverse result
    return sol_seq1, sol_seq2


def test_align():
    seq1 = "anastasia"
    seq2 = "ananasik"
    align(seq1, seq2)
    seq3 = "agatacacaga"
    seq4 = "tacataagata"
    align(seq3, seq4)


def test_nonincreasing_sqr():
    seq = [7, 11, 5, 10, 4, 11, 6, 7, 9, 3, 4, 6, 7]
    longest_nonincreasing_subseq_sqr(seq)


def main():
    test_nonincreasing_sqr()
    test_align()


if __name__ == '__main__':
    main()
