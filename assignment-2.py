#! /usr/bin/env python


from __future__ import division, print_function


# Не уверена, что это оптимальный вариант, но он, по крайней мере,
# уже почти выполняет все условия (пока не получилось с одним аргументом).


"""
my_max(*args) finds current_maxum value in values, list or tuple
"""


def my_max(*args):
    if len(args) > 1:
        current_max = args[0]
        for num in args:
            if num.__class__ == int and num > current_max:
                current_max = num
            elif num.__class__ != int:
                raise ValueError("Input value {}"
                                 " is not integer".format(num))
    elif len(args) == 1:
        if args.__class__ == tuple or list:
            for iterated_list in args:
                pass
            for current_max in iterated_list:
                pass
            for num in iterated_list:
                if num.__class__ == int and num > current_max:
                    current_max = num
                elif num.__class__ != int:
                    raise ValueError("Input value {}"
                                     " is not integer".format(num))
    else:
        raise ValueError("There is only one value {}"
                         "and it isn't tuple or list".format(*args))
    return current_max


def my_min(*args):
    for minim in args:
        pass
    for index in args:
        if index < minim:
            minim = index
    return minim


def test(*args):
    def in_test(args):
        for current_max in args:
            pass
        for index in args:
            if index.__class__ == int and index > current_max:
                current_max = index
            elif index.__class__ != int:
                raise ValueError("Input value {}"
                                 " is not integer".format(index))
        return current_max

    if len(args) > 1:
        in_test(args)
    elif len(args) == 1 and args.__class__ == tuple or list:
        for iterated_list in args:
            pass
        in_test(iterated_list)
    return in_test(args)