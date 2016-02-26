#! /usr/bin/env python


from __future__ import division, print_function
from itertools import imap


STOP_CODONS = ["TAG", "TAA", "TGA"]
NUCLEOTIDES = ["A", "T", "G", "C"]
GAP_SYMBOL = "-"


def genetic_code(codon):
    """
    Dictionary.
    Returns one-letter name of amino-acid, which corresponds to codon
    :type codon: str
    :param codon: 3-letter string
    :return: string
    """
    codons = {
        "ATG": "M",
        "TTT": "F",
        "TTC": "F",
        "TTA": "L",
        "TTG": "L"
    }
    return codons[codon]


def reconstruct_protein_alignment(*args):
    """
    Reconstructs protein alignment by nucleotide alignment
    "aa" in names of variables means "amino acid"
    :type args: str
    :param args:
    :return: tuple of translated sequences.
    Each 3 gaps are "translated" to one gap
    :return: ValueError, if strings have different length
    :return: ValueError, if length is not multiple of 3
    :return: ValueError, if there are incorrect symbols
    :return: ValueError, Amount of gaps is not multiple of 3
    """
    if len(set(imap(len, args))) != 1:
        raise ValueError("Strings in alignment have different length")
    if not len(args) % 3:
        raise ValueError("Length is not multiple of 3")
    gap_counter = 0
    codon = []
    aa_seq = []
    aa_alignment = []
    for seq in args:
        for char in seq.upper():
            if char == GAP_SYMBOL:
                gap_counter += 1
                if gap_counter < 3:
                    continue
                aa_seq.append(GAP_SYMBOL)
                gap_counter = 0
                continue
            if char not in NUCLEOTIDES:
                raise ValueError("Incorrect symbol {}".format(char))
            codon.append(char)
            if len(codon) == 3:
                if "".join(codon) in STOP_CODONS:
                    aa_seq.append(GAP_SYMBOL * (len(seq) // 3 -
                                                len("".join(aa_seq))))
                    break
                aa_seq.append(genetic_code("".join(codon)))
                codon = []
        if gap_counter:
            raise ValueError("Amount of gaps is not multiple of 3")
        aa_alignment.append("".join(aa_seq))
        aa_seq = []
    return aa_alignment


q = "TTTTTTTTTTTT"
w = "TTATTTTTTTTT"
e = "TTATTTTGAGGG"
r = "TTT---TTTTTG"
t = "TT-T-T-TTTTC"
reconstruct_protein_alignment(q, w, e, r, t)


