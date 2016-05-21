import operator as op
from typing import Tuple


NUCLEOTIDES = ("A", "C", "G", "T")

GC = ("G", "C")

COMPLEMENTARY_NUCL = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}


def gc_content(seq: str) -> float:
    return round(sum(nucl in GC for nucl in seq.upper())/len(seq), 2)


def max_gc(fasta_list: Tuple[str, str]) -> Tuple[str, float]:
    # nearly working
    """
    Sequences after fasta-reader
    :param fasta_list:
    :return:
    """
    gc_and_names = ((name, gc_content(seq)) for name, seq in fasta_list)
    return max(enumerate(gc_and_names), key=op.itemgetter(1))[1]

#
# many_seq = [("line1", "atgcatgcatgcatgc"), ("line2", "atggagcgatgcatgc"),
#             ("line3", "gggcagggggccgccgcgtgc"), ("line4", "atacatatttt")]
#
# max_gc(many_seq)


def hamming_dist(seq1: str, seq2: str) -> int:
    """
    Calculates number of mismatches in two DNA strings.
    :param seq1:
    :param seq2:
    :return:
    """
    return sum(char1 != char2 for char1, char2 in zip(seq1.upper(), seq2.upper()))
