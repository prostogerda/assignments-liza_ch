#! /usr/bin/env python


from __future__ import division, print_function
import operator

# Task 1. Fasta-reader


def fasta_reader(fp):
    """
    Reads fasta-files.
    :param fp: absolute path to file
    :return: tuples of sequences in format (name, seq)
    """
    fasta_start_sym = ">"
    fasta_comment_sym = "#"
    output_list = []
    name_seq_list = []
    seq_list = []
    with open(fp) as fasta_file:
        for line in fasta_file:
            if not line.strip():
                continue
            if line.startswith(fasta_comment_sym):
                continue
            if line.startswith(fasta_start_sym):
                name_seq_list.append("".join(seq_list))
                output_list.append(tuple(name_seq_list))
                # output_list.append(tuple(name_seq_list.append
                # ("".join(seq_list))))
                seq_list = []
                name_seq_list = []
                name_seq_list.append(line.strip())
            else:
                seq_list.append(line.strip())
        name_seq_list.append("".join(seq_list))
        output_list.append(tuple(name_seq_list))
    return output_list[1:]


print (fasta_reader("/home/liza/Documents/test.fasta"))


# Task fom previous HW

def evaluate_string(expression):
    """
    Calculates result of arithmetical expression, which may consist on integer
    numbers, addition and subtraction. Branches and spaces are ignored.
    :param expression: string of numbers and "+" and "-" signs.
    :return: result of arithmetical expression, integer number
    """
    if not isinstance(expression, str):
        raise ValueError("Please enter the string")
    numbers = []
    operations = []
    branch_counter = 0
    long_num = []
    operation_dict = {
        "+": operator.add,
        "-": operator.sub
    }
    ignore_list = [" "]
    for arg in expression:
        if arg in ignore_list:
            continue
        if arg is ".":
            raise ValueError("Function doesn't support float numbers")
        if arg == "(":
            branch_counter += 1
            continue
        if arg == ")":
            branch_counter -= 1
            if branch_counter >= 0:
                continue
            raise ValueError("Incorrect branches")
        # PyCharm doesn't give to write 3 previous lines as ternary operator
        if arg.isdigit():
            long_num.append(arg)
            continue
        if operation_dict.get(arg):
            if not long_num:
                raise ValueError("Too many operations")
            numbers.append(int("".join(long_num)))
            long_num = []
            operations.append(arg)
            if numbers == []:
                # if not numbers?
                numbers = [0]
            continue
        raise ValueError("Operation {} is not supported".format(arg))
    numbers.append(int("".join(long_num)))
    if branch_counter != 0:
        raise ValueError("Incorrect branches")
    if len(numbers) != len(operations) + 1:
        raise ValueError("Too many operations")
    numbers_iter = iter(numbers)
    acc = next(numbers_iter)
    for num, oper in zip(numbers_iter, operations):
        oper_func = operation_dict.get(oper)
        acc = oper_func(acc, num)
    return acc

evaluate_string("333+2-1")
evaluate_string("2+7*0-3")
evaluate_string("-3+(2    -1")
evaluate_string("2++(7  -3")
evaluate_string("23(3+)7-3")
evaluate_string("2+7.0- 3 ")
