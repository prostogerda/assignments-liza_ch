#! /usr/bin/env python


from __future__ import division, print_function
import itertools
import random


def merge(a, b):
    """
    Merges two sorted lists to one sorted list.
    Compares first elements of lists, appends lowest to the new list and
    moves index counter of this list to the next position. Compares elements
    with current indices. Repeats.
    When one of indices comes to end of list, appends to the result
    all elements, which left in another list
    :type a: collections.Sequence or collections.Set, I don't sure
    :param a: sorted
    :type b: collections.Sequence or collections.Set
    :param b: sorted
    :return: sorted list, composed of two lists
    :rtype: list
    """
    i, j = 0, 0
    one_sorted_list = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            one_sorted_list.append(a[i])
            i += 1
        else:
            one_sorted_list.append(b[j])
            j += 1
    if i == len(a):
        one_sorted_list.extend(itertools.islice(b, j, len(b)))
    else:
        one_sorted_list.extend(itertools.islice(a, i, len(a)))
    return one_sorted_list


def mergesort_rec(lst):
    """
    Sorts list recursively
    Breaks list to two parts. If their lengths are 0 or 1, merges them.
    If not, comes to beginning and tries to sort parts separately.
    :type lst: list
    :param lst: unsorted list
    :return:
    """
    first_half = lst[:len(lst) // 2]
    second_half = lst[len(lst) // 2:]
    if len(first_half) <= 1 and len(second_half) <= 1:
        return merge(first_half, second_half)
    return merge(mergesort_rec(first_half), mergesort_rec(second_half))


def test_mergesort_rec():
    unsorted_list = [random.randint(1, 1000) for _ in xrange(50)]
    return mergesort_rec(unsorted_list) == sorted(unsorted_list)


def main():
    if not test_mergesort_rec():
        raise RuntimeError


if __name__ == '__main__':
    main()