#! /usr/bin/env python3


from functools import reduce


def reverse(num_str: str) -> int:
    """
    Function reverses the number (abcd -> dcba)
    :param num_str:
    :return:
    """
    return int(num_str[::-1])


def digits_are_odd(num: int) -> bool:
    """
    Function checks odd confirmation for every digit
    :param num:
    :return:
    """
    return all(int(figure) % 2 for figure in str(num))


def num_of_odd_sums(numbers: list):
    """
    Counts number of cases, that match the condition:
    sum of number and "reversed" number consists of odd figures
    :param numbers:
    :return:
    """
    return sum(digits_are_odd(int(num_str) + reverse(num_str))
               for num_str in numbers)


def main():
    n = int(input("Insert number of cases: "))
    numbers = [input("Print number: ") for _ in range(n)]
    print(num_of_odd_sums(numbers))


if __name__ == '__main__':
    main()
