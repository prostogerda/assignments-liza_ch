#! /usr/bin/env python


from __future__ import division, print_function


# Мне тут Женя говорит, что ты ему сказал, что my_max(одно число) должно
#  выдавать это число. А в задании написано, что должен выдавать ошибку,
# что это не список. Написала пока для второго варианта. Над вложением
# функции в функцию пока думаю :)


def my_max(*args):
    """
    my_max(*args) finds maximum in some values,
    list or tuple of integer numbers
    """
    if not args:
        raise ValueError("Please enter some numbers")
    if len(args) == 1:
        for iterated_list in args:
                pass
        if not isinstance(iterated_list, (tuple, list)):
            raise ValueError("There is only one value {}"
                             ", and it isn't tuple or list".format(*args))
        current_max = iterated_list[0]
        for num in iterated_list:
            if not isinstance(num,int):
                raise ValueError("Input value {}"
                                 " is not integer".format(num))
            if num > current_max:
                current_max = num
    if len(args) > 1:
        current_max = args[0]
        for num in args:
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
        for iterated_list in args:
                pass
        if not isinstance(iterated_list, (tuple, list)):
            raise ValueError("There is only one value {}"
                             ", and it isn't tuple or list".format(*args))
        current_min = iterated_list[0]
        for num in iterated_list:
            if not isinstance(num,int):
                raise ValueError("Input value {}"
                                 " is not integer".format(num))
            if num < current_min:
                current_max = num
    if len(args) > 1:
        current_min = args[0]
        for num in args:
            if not isinstance(num, int):
                raise ValueError("Input value {}"
                                 " is not integer".format(num))
            if num < current_min:
                current_min = num
    return current_min


def test(*args):
    """
    my_max(*args) finds maximum of values,
    list or tuple of integer numbers
    """
    def inner_func(*inner_args):
        current_max = inner_args[0]
        for num in inner_args:
            if not isinstance(num, int):
                raise ValueError("Input value {}"
                                 " is not integer".format(num))
            if num > current_max:
                current_max = num
        return current_max
    if not args:
        raise ValueError("Please enter some numbers")
    if len(args) == 1:
        for iterated_list in args:
                pass
        if not isinstance(iterated_list, (tuple, list)):
            raise ValueError("There is only one value {}"
                             ", and it isn't tuple or list".format(*args))
        maximum = inner_func(iterated_list)
    if len(args) > 1:
        maximum = inner_func(args)
    return maximum

