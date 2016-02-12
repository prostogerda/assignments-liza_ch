#! /usr/bin/env python


from __future__ import division, print_function


# Task 1. Fasta-reader


def fasta_reader(fp):
    """
    Reads fasta-files.
    :param fp: absolute path to file
    :return: tuples of sequences in format (name, seq, comments)
    """
    fasta_list = []
    name_seq_comm_list = []
    seq = ""
    comment = ""
    with open(fp) as fasta_file:
        for line in fasta_file:
            if len(line) == 1:
                continue
            if line.startswith(">"):
                fasta_list.append(tuple(name_seq_comm_list))
                name_seq_comm_list = ["", "", ""]
                name_seq_comm_list[0] = line.strip('\n')
                # Do this ^ with "append"?
                seq = ""
                comment = ""
            if line.startswith("#"):
                comment.strip('\n')
                comment.join(line)
                name_seq_comm_list[2] = comment
            seq.strip('\n')
            seq.join(line)
            name_seq_comm_list[1] = seq
    print(*fasta_list[1:] if fasta_list[0] == () else fasta_list)
    # variant for case, when file starts not from ">"
    # print(*fasta_list[1:] if fasta_list[0][0] == "" else fasta_list)

    #where shall I use "split"?


fasta_reader("/home/liza/Documents/test.fasta")


def test(fp):
    seq = ""
    with open(fp) as fasta_file:
        for line in fasta_file:
            seq.join(line)
        print(seq.strip('\n'))

test("/home/liza/Documents/test.fasta")


#Task fom previous HW

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
    long_num = ""
    operation_dict = {
        "+": operator.add,
        "-": operator.sub
    }
    ignore_list = ["(", ")", " "]
    for arg in expression:
        if arg in ignore_list:
            continue
        if arg is ".":
            raise ValueError("Function doesn't support float numbers")
        if operation_dict.get(arg):
            operations.append(arg)
            if not numbers:
                numbers = [0]
            numbers_list.append(long_num)
            long_num = ""
            continue
        if arg.isdigit():
            numbers_list = []

            # sub_expression = expression[int(arg):]

                    arg = next(iter(expression))
                # arg = next(iter(expression))
                long_num.join(numbers_list)
                arg_int = int(long_num)
                numbers.append(arg_int)
                continue
            # arg_int = int(arg)
            # numbers.append(arg_int)
            continue
        raise ValueError("Operation {} is not supported".format(arg))
    if len(numbers) != len(operations) + 1:
        raise ValueError("Too many operations")
    numbers_iter = iter(numbers)
    acc = next(numbers_iter)
    for num, oper in zip(numbers_iter, operations):
        oper_func = operation_dict.get(oper)
        acc = oper_func(acc, num)
    return acc

evaluate_string("3+2-1")
evaluate_string("2+7*0-3")
evaluate_string("-3+(2    -1")
evaluate_string("2++(7  -3")
evaluate_string("233+7-3")
evaluate_string("2+7.0-3")
