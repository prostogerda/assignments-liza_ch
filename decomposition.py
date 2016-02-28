#! /usr/bin/env python


from __future__ import division, print_function


"""
Gets natural number from 1 to 10^9 from std_in.
Finds maximum different natural numbers, sum of which equal to input number.
Prints result to std_out.
Raises errors when gets not number or incorrect number.
"""


def decompose(num):
    """
    Finds maximum different natural numbers, sum of which equal to num.
    :type num: int
    :param num:
    :return: list of sorted numbers
    """
    numbers = []
    special_values = [1, 2, 4]
    while num not in special_values:
        if num % 2:
            numbers.append((num // 2) + 1)
        else:
            numbers.append(num // 2)
        num //= 2
    if num == 4:
        numbers.append(1)
        numbers.append(3)
    if num == 2 or num == 1:
        numbers.append(num)
    return sorted(numbers)


def main():
    input_number = raw_input("Enter the natural number from 1 to 10^9: ")
    if not input_number.isdigit():
        raise ValueError("{} is not the number".format(input_number))
    if not (1 <= int(input_number) <= 10**9):
        raise ValueError("Incorrect number")
    print(*decompose(int(input_number)))


if __name__ == '__main__':
    main()
