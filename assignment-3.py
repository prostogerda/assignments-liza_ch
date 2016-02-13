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
    FASTA_START_SYM = ">"
    FASTA_COMMENT_SYM = "#"
    output_list = []
    name_seq_list = []
    seq_list = []
    with open(fp) as fasta_file:
        for line in fasta_file:
            if not line.strip():
                continue
            if line.startswith(FASTA_COMMENT_SYM):
                continue
            if line.startswith(FASTA_START_SYM):
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
    bracket_counter = 0
    long_num = []
    operation_dict = {
        "+": operator.add,
        "-": operator.sub
    }
    ignore_list = [" "]
    for char in expression:
        if char in ignore_list:
            continue
        if char is ".":
            raise ValueError("Function doesn't support float numbers")
        if char == "(":
            bracket_counter += 1
            continue
        if char == ")":
            bracket_counter -= 1
            if bracket_counter >= 0:
                continue
            raise ValueError("Incorrect brackets")
        # PyCharm doesn't give to write 3 previous lines as ternary operator
        if char.isdigit():
            long_num.append(char)
            continue
        if operation_dict.get(char):
            if not long_num:
                raise ValueError("Too many operations")
            numbers.append(int("".join(long_num)))
            long_num = []
            operations.append(char)
            if numbers == []:
                # if not numbers?
                numbers = [0]
            continue
        raise ValueError("Operation {} is not supported".format(char))
    numbers.append(int("".join(long_num)))
    if bracket_counter != 0:
        raise ValueError("Incorrect brackets")
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
