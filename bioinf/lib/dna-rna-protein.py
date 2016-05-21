from typing import Sequence


NUCLEOTIDES_DNA = ("A", "C", "G", "T")

NUCLEOTIDES_RNA = ("A", "C", "G", "U")

GC = ("G", "C")

COMPLEMENTARY_NUCL = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

GAP_SYMBOL = "-"

CODONS = {
    "UUU": "F",
    "UUC": "F",
    "UUA": "L",
    "UUG": "L",
    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",
    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "AUG": "M",
    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",
    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "ACU": "U",
    "ACC": "U",
    "ACA": "U",
    "ACG": "U",
    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "UAU": "Y",
    "UAC": "Y",
    "CAU": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "AAU": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "GAU": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "UGU": "C",
    "UGC": "C",
    "UGG": "W",
    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGU": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
    "UAG": None,
    "UAA": None,
    "UGA": None
    }


def count_nucleotides(seq: str) -> list:
    """
    Counts amounts of each nucleotide in DNA sequence.
    :param seq:
    :return: nucleotides in order [A, C, G, T]
    """
    return list(seq.upper().count(nucl) for nucl in NUCLEOTIDES_DNA)


def dna_to_rna(seq: str) -> Sequence:
    """
    Transcribes DNA string to RNA by replacing T to U.
    :param seq:
    :return: RNA string
    """
    return seq.upper().replace("T", "U")


def reverse_complement(seq: str) -> Sequence:
    """
    Makes reverse-complement sequence of DNA.
    :param seq:
    :return:
    """
    return "".join(COMPLEMENTARY_NUCL.get(nucl) for nucl in reversed(seq))


def rna_to_protein(seq: str) -> Sequence:
    """
    Translates RNA sequence without gaps to protein.
    After first stop-codon in frame inserts gaps.
    :type seq: str
    :param seq:
    :return: string of amino acids and gaps
    :raise ValueError, if there are incorrect symbols
    :raise ValueError, Length of sequence is not multiple of 3
    """
    if len(seq) % 3:
        raise ValueError("Sequence length is not multiple of 3")
    codon = []
    aa_seq = []
    for char in seq.upper():
        if char not in NUCLEOTIDES_RNA:
            raise ValueError("Incorrect symbol {}".format(char))
        codon.append(char)
        if len(codon) == 3:
            if not CODONS["".join(codon)]:
                aa_seq.append(GAP_SYMBOL * (len(seq) // 3 -
                                            len("".join(aa_seq))))
                break
            aa_seq.append(CODONS["".join(codon)])
            codon = []
    return "".join(aa_seq)
