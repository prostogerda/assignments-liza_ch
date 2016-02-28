#! /usr/bin/env python


from __future__ import division, print_function


"""
Gets natural number from 1 to 10^9 from std_in.
Finds maximum different natural numbers, sum of which equal to input number.
Prints result to std_out.
Raises errors when gets not number or incorrect number.
"""


def decompose(n):
    """
    Finds maximum different natural numbers, sum of which equal to n.
    :type n: int
    :param n:
    :return: list of numbers
    """
    numbers = []
    if n == 1 or n == 2:
        numbers.append(n)
        return numbers
    numbers = [1]
    ost = n -1
    while ost:
        if ost > 2 * (numbers[-1] + 1):
            numbers.append(numbers[-1] + 1)
            ost -= numbers[-1]
        else:
            numbers.append(ost)
            ost -= numbers[-1]
            return numbers


def main():
    input_number = raw_input("Enter the natural number from 1 to 10^9: ")
    if not input_number.isdigit():
        raise ValueError("{} is not the number".format(input_number))
    if not (1 <= int(input_number) <= 10**9):
        raise ValueError("Incorrect number")
    print(*decompose(int(input_number)))


if __name__ == '__main__':
    main()
