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
        for numb in args:
            if numb.__class__ == int and numb > current_max:
                current_max = numb
            elif numb.__class__ != int:
                raise ValueError("Input value {}"
                                 " is not integer".format(numb))
    elif len(args) == 1:
        if args.__class__ == tuple or list:
            for iteratedList in args:
                pass
            current_max = iteratedList[0]
            for numb in iteratedList:
                if numb.__class__ == int and numb > current_max:
                    current_max = numb
                elif numb.__class__ != int:
                    raise ValueError("Input value {}"
                                     " is not integer".format(numb))
    else:
        raise ValueError("There is only one value {}"
                         "and it isn't tuple or list".format(*args))
    return current_max


def my_min(*args):
    if len(args) > 1:
        current_min = args[0]
        for numb in args:
            if numb.__class__ == int and numb < current_min:
                current_min = numb
            elif numb.__class__ != int:
                raise ValueError("Input value {}"
                                 " is not integer".format(numb))
    elif len(args) == 1:
        if args.__class__ == tuple or list:
            for iteratedList in args:
                pass
            current_min = iteratedList[0]
            for numb in iteratedList:
                if numb.__class__ == int and numb < current_min:
                    current_min = numb
                elif numb.__class__ != int:
                    raise ValueError("Input value {}"
                                     " is not integer".format(numb))
    else:
        raise ValueError("There is only one value {}"
                         "and it isn't tuple or list".format(*args))
    return current_min


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
        for iteratedList in args:
            pass
        in_test(iteratedList)
    return in_test(args)