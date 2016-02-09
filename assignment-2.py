#! /usr/bin/env python


from __future__ import division, print_function
import operator


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
    if not args:
        raise ValueError("Please enter some numbers")

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

    return max_finder(iter(args[0] if len(args) == 1 else args))


def my_map(fn, elements, **kwargs):
    result = []
    for element in elements:
        result.append(fn(element, **kwargs))
    return result


def calculate(numbers, operations):
    if len(numbers) != len(operations) + 1:
        raise ValueError("Too many operations")
    operation_dict = {
        "+": operator.add,
        # "-": lambda operator.add,
        "*": operator.mul,
        "/": operator.div
        }
    numbers_iter = iter(numbers)
    acc = next(numbers_iter)
    for num, oper in zip(numbers_iter,operations):
        oper_func = operation_dict.get(oper)
        if not operation_dict.get(oper):
            raise ValueError("Operation {} is not supported".format(oper))
        acc = oper_func(acc, num)
    return acc


calculate([1, 3, 2], ["+", "*"])


def calculate2(numbers, operations):
    if len(numbers) != len(operations) + 1:
        raise ValueError("qqq")
    operation_dict = {
        "+": operator.add,
        # "-": lambda operator.add,
        "*": operator.mul,
        "/": operator.div
        }
    # Find string in Lesson5 from Ilia
    return reduce(lambda acc, (num, oper): operation_dict[oper](acc,num),
                  zip(numbers,operations))


def new_max(iterable):
    return reduce(lambda cur_max, num: num if num > cur_max else cur_max,
                  iterable)

# Homework 2 part 2
# Task 3 part 2


def my_filter(fn, elements, **kwargs):
    """
    Function my_filter returns list of elements, for which result of
    function fn returns True.
    :param fn is name of function, which returns True or False
    :param elements: list of elements to work with
    :param kwargs: parameters of function fn
    :return: List of elements
    """
    true_elements = []
    for element in elements:
        if fn(element, **kwargs):
            true_elements.append(element)
    return true_elements


def evaluate_string(expression):
    """
    Calculates
    :param expression:
    :return:
    """
    if not isinstance(expression, str):
        raise ValueError("Please enter the string")
    numbers = []
    operations = []
    operation_dict = {
        "+": operator.add,
        "-": operator.sub
    }
    ignore_list = {
        "(": None,
        ")": None,
        " ": None
    }
    for arg in expression:
        if ignore_list.get(arg):
            continue
        if operation_dict.get(arg):
            operations.append(arg)
            continue
        if arg.isdigit:
            arg_int = int(arg)
            numbers.append(arg_int)
            continue
        else:
            raise ValueError("Operation {} is not supported".format(arg))
    if len(numbers) != len(operations) + 1:
        raise ValueError("Too many operations")
    numbers_iter = iter(numbers)
    acc = next(numbers_iter)
    for num, oper in zip(numbers_iter, operations):
        oper_func = operation_dict.get(oper)
        acc = oper_func(acc, num)
    return acc

evaluate_string("2+7-3")

evaluate_string("2+7 -3")