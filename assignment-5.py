#! /usr/bin/env python


from __future__ import division, print_function
from itertools import imap


NUCLEOTIDES = ["A", "T", "G", "C"]
GAP_SYMBOL = "-"


CODONS = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "ACT": "U",
    "ACC": "U",
    "ACA": "U",
    "ACG": "U",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "TAT": "Y",
    "TAC": "Y",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "TGT": "C",
    "TGC": "C",
    "TGG": "W",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
    "TAG": None,
    "TAA": None,
    "TGA": None
    }


def translate_dna_to_aa(seq):
    gaps = []
    codon = []
    aa_seq = []
    for char in seq.upper():
        if char == GAP_SYMBOL:
            gaps.append(char)
            if len(gaps) < 3:
                continue
            aa_seq.append(GAP_SYMBOL)
            gaps = []
            continue
        if char not in NUCLEOTIDES:
            raise ValueError("Incorrect symbol {}".format(char))
        codon.append(char)
        if len(codon) == 3:
            if not CODONS["".join(codon)]:
                aa_seq.append(GAP_SYMBOL * (len(seq) // 3 -
                                            len("".join(aa_seq))))
                break
            aa_seq.append(CODONS["".join(codon)])
            codon = []
    if len(gaps):
        raise ValueError("Amount of gaps is not multiple of 3")
    return "".join(aa_seq)


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
    if len(args[0]) % 3:
        raise ValueError("Length is not multiple of 3")
    return tuple((translate_dna_to_aa(seq) for seq in args))


q = "CttAtcAgtGcg"
w = "TTAaaaaTTTcT"
e = "TTATTcTGAGGG"
r = "TTT---TTTTTG"
t = "TT-T-T-TTtTC"
reconstruct_protein_alignment(q, w, e, r, t)

