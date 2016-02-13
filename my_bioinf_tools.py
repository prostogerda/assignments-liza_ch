#! /usr/bin/env python


from __future__ import division, print_function
import sys
import os


def fasta_reader(fp):
    """
    Reads fasta-files.
    :param fp: absolute path to file
    :return: tuples of sequences in format (name, seq)
    """
    FASTA_START_SYM = ">"
    FASTA_COMMENT_SYM = "#"
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
                if name_seq_list[0]:
                    yield tuple(name_seq_list)
                seq_list = []
                name_seq_list = []
                name_seq_list.append(line.strip())
            else:
                seq_list.append(line.strip())
        name_seq_list.append("".join(seq_list))
        yield tuple(name_seq_list)


def main():
    file_path = os.path.abspath(sys.argv[1])
    fasta_reader(file_path)
    fasta_reader("/home/liza/Documents/test.fasta")


if __name__ == "__main__":
    main()
