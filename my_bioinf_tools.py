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
    name_seq, seq = [], []
    with open(fp) as fasta_file:
        for line in fasta_file:
        # for line in (l for l in fasta_file if l.strip()):
        # doesn't need not line.strip()
            if not line.strip() or line.startswith(FASTA_COMMENT_SYM):
                continue
            if line.startswith(FASTA_START_SYM):
                name_seq.append("".join(seq))
                if name_seq[0]:
                    yield tuple(name_seq)
                seq, name_seq = [], []
                name_seq.append(line.strip("> \n"))
            else:
                seq.append(line.strip())
        name_seq.append("".join(seq))
        yield tuple(name_seq)


def main():
    file_path = os.path.abspath(sys.argv[1])
    fasta_reader(file_path)
    fasta_reader("/home/liza/Documents/test.fasta")


if __name__ == "__main__":
    main()
