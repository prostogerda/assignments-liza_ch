#! /usr/bin/env python3


class DinArray:
    def __init__(self, *values):
        self._value = [None] * 8
        while len(values) > len(self):
            self._increase_len()
        for value in values:
            self._value.append(value)
            self._last_nonempty_idx += 1

    def __setitem__(self, i, value):
        self._value[i] = value

    def __getitem__(self, i):
        return self._value[i]

    def __len__(self):
        return len(self._value)

    def append(self, value):
        if self.last_nonempty_idx + 1 == len(self):
            self._increase_len()
        self._value[self.last_nonempty_idx + 1] = value
        self.last_nonempty_idx += 1

    def _increase_len(self):
        self._value += [None] * len(self)

    # @staticmethod
    def _last_nonempty_idx(self, idx):
        self._idx = idx

    @property
    def last_nonempty_idx(self):
        return self._last_nonempty_idx

    @last_nonempty_idx.setter
    def last_nonempty_idx(self, idx):
        self._idx = idx


class MySet:
    """
    Hash table for strings.
    Length of hash table and polynomial base may be changed.
    Calculates hash of string and contains this string (or many strings with
    same hashes) in cell with appropriate number in list.
    """
    HASH_TABLE_LEN, POLYNOM_BASE = 57, 11  # numbers are "random"

    def __init__(self, strings, h=HASH_TABLE_LEN):
        """
        :type strings: list(str)
        :param strings:
        :return:
        """
        self._str_hashes = [None] * h
        self._nonempty_hashes = 0
        for string in strings:
            if not isinstance(string, str):
                raise ValueError("Input must contain 'string' instances")
            cur_hash = self._hash(string)
            if self._str_hashes[cur_hash] is None:
                self._str_hashes[cur_hash] = [string]
                self._nonempty_hashes += 1
            else:
                self._str_hashes[self._hash(string)].append(string)

    def _hash(self, string, p=POLYNOM_BASE, l=HASH_TABLE_LEN):
        return sum(ord(string[i]) * (p ** i) for i in range(len(string))) % l

    def __len__(self):
        """
        Length of set in number of existing unique hashes.
        :return:
        """
        return self._nonempty_hashes

    def __contains__(self, item):
        return True if self._str_hashes[self._hash(item)] is not None else False

    # Set methods:
    # len
    # x in s
    # x not in set
    # issubset
    # issuperset
    # union
    # intersection
    # difference
    # symmetric_difference


def many_matr_mul(*matrices):
    mul_costs = [[None for j in range(len(matrices))]
                 for i in range(len(matrices))]

    new_matr_sizes = [[None for j in range(len(matrices))]
                      for i in range(len(matrices))]

    def mul_cost(matr1, matr2):
            # """
            # :type matr1: list(list)
            # :param matr1:
            # :type matr2: list(list)
            # :param matr2:
            # :return:
            # """
        return len(matr1[0])*len(matr2)*len(matr1)

    def new_matr_size(matr1, matr2):
        return len(matr1[0])*len(matr2)

    for i in range(1, len(matrices)):
        q = 1
        j = i - q
        mul_costs[i][j] = min(mul_cost(matrices[i], matrices[i-1]),
                              (mul_costs[i-1][w] for w in range(1, i+1)),
                              (mul_costs[w][i] for w in range(0, i)))
    pass


qq = [[1, 2], [2, 3], [3, 4]]
ww = [[1, 2, 3],[1, 2, 3], [1, 2, 3]]
ee = [[1], [2], [3]]
many_matr_mul(qq, ww, ee)



def incr_subseq_log(seq):
    pass

def set_test():
    q = ["qwe", "wwwr", "rty", "qwe", "4d", "21ww"]
    w = MySet(q)
    print(w)
    len(w)
    "rty" in w
    "4d" not in w
    e = ["jdsh", "krj", 486, ["erf", "ggfh"]]
    r = MySet(e)


def main():
    set_test()


if __name__ == '__main__':
    main()

