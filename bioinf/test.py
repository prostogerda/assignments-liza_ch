#! /usr/bin/env python3


FASTA_START_SYM = ">"

FASTA_COMMENT_SYM = "#"


def fasta_reader(fp):
    """
    Reads fasta-files. Parses them into tuples (name, seq) lazy.
    :param fp: absolute path to file
    :return: tuples of sequences in format (name, seq)
    """
    name_seq, seq = [], []
    with open(fp) as fasta_file:
        for line in fasta_file:
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