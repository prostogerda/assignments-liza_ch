#! /usr/bin/env python


from __future__ import division, print_function


"""
Gets natural number from 1 to 10^9 from std_in.
Finds maximum different natural numbers, sum of which equal to input number.
Prints result to std_out.
Raises errors when gets not number or incorrect number.
"""


numbers = []


def decompose(num):
    """
    Finds maximum different natural numbers, sum of which equal to num.
    :type num: int
    :param num:
    :return: list of numbers
    """
    if num == 4:
        numbers.append(1)
        numbers.append(3)
        return numbers
    if num == 2 or num == 1:
        numbers.append(num)
        return numbers
    if num % 2:
        numbers.append((num // 2) + 1)
    else:
        numbers.append(num // 2)
    decompose(num // 2)
    return sorted(numbers)


def main():
    input_number = raw_input("Enter the natural number from 1 to 10^9: ")
    if not input_number.isdigit():
        # 2 next lines may be written as raise ValueError(),
        # but it looks not so beautiful in std_out
        print("{} is not the number".format(input_number))
        exit()
    if not (1 <= int(input_number) <= 10**9):
        print("Incorrect number")
        exit()
    print(*decompose(int(input_number)))


if __name__ == '__main__':
    main()
