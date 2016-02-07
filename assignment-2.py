#! /usr/bin/env python


from __future__ import division, print_function

#Теперь ведет себя по разному на my_max(одно число) и my_max([одно число])


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


def my_