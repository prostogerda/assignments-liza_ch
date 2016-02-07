#! /usr/bin/env python


from __future__ import division, print_function


def my_max(*args):
    """
    my_max(*args) finds maximum in some values,
    list or tuple of integer numbers
    """
    iterated_list = args
    if not args:
        raise ValueError("Please enter some numbers")
    if len(args) == 1:
        iterated_list = args[0]
        if not isinstance(iterated_list, (tuple, list)):
            raise ValueError("There is only one value {}"
                             ", and it isn't tuple or list".format(args[0]))
    current_max = iterated_list[0]
    for num in iterated_list:
        if not isinstance(num, int):
            raise ValueError("Input value {}"
                             " is not integer".format(num))
        if num > current_max:
            current_max = num
    return current_max


def my_min(*args):
    """
    my_min(*args) finds minimum in some values,
    list or tuple of integer numbers
    """
    if not args:
        raise ValueError("Please enter some numbers")
    if len(args) == 1:
        iterated_list = args[0]
        if not isinstance(iterated_list, (tuple, list)):
            raise ValueError("There is only one value {}"
                             ", and it isn't tuple or list".format(args[0]))
        args = iterated_list
    current_min = args[0]
    for num in args:
        if not isinstance(num, int):
            raise ValueError("Input value {}"
                             " is not integer".format(num))
        if num < current_min:
            current_min = num
    return current_min


def my_max_nice(*args):
    """
    Function My_max_nice finds maximum value in iterable object
    when it consists of integer numbers.
    :param args: any iterable object with integer numbers inside it.
    :return: maximum value
    """
    def max_finder(iterated_list):
        current_max = next(iterated_list)
        if isinstance(current_max, int):
            for num in iterated_list:
                if not isinstance(num, int):
                    raise ValueError("Input value {}"
                                     " is not integer".format(num))
                if num > current_max:
                    current_max = num
            return current_max
        raise ValueError("Input value {}"
                        " is not integer".format(current_max))

    if not args:
        raise ValueError("Please enter some numbers")
    return max_finder(iter(args[0] if len(args) == 1 else args))

my_max_nice(777, 675, 6)
my_max_nice(2, 657, 77)
my_max_nice([6, -988, 21])
my_max_nice("QQQQ", 56, 87)
my_max_nice(321, "WWWW", 76)
my_max_nice(43, 21, "EEEE")
my_max_nice(765)
my_max_nice()
