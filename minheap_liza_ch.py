#! /usr/bin/env python


from __future__ import print_function, division


class Node(object):
    """
    Node consists of it's value (may be any) and priority. Nodes are compared by
     their priority.
    :type _item: any
    :type _priority: int  # and float?
    """
    def __init__(self, item, priority):
        self._item = item
        self._priority = priority

    @property
    def item(self):
        return self._item

    @property
    def priority(self):
        return self._priority

    def __str__(self):
        return str((self.item, self.priority))

    def __ne__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return not self == other

    def __eq__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.priority == other.priority

    def __gt__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.priority > other.priority

    def __ge__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.priority >= other.priority

    def __lt__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.priority < other.priority

    def __le__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.priority <= other.priority


class MinHeap(object):
    """
    Array. It's 0th value is always 0, 1st value is minimal from all other
    values except 0th).
    This is representation of binary tree, in which upper node has minimal
    value, every node has not more than two children and not more than one
    parent.
    Every values have their indices(i) in array. Parent of node i is node
    i // 2. Children of node i are nodes i * 2 and i * 2 + 1.
    :type _heap: list[int, int]  # second value in list - int or float?
    """
    def __init__(self):
        """
        0th value is necessary to easy numeration of nodes.
        :return:
        """
        self._heap = [0]

    def __len__(self):
        return len(self._heap) - 1

    def __nonzero__(self):
        return bool(len(self))

    def _exchange(self, i, j):
        """
        Changes places of two nodes
        :type i: int
        :type j: int
        :return: None
        """
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _percolate_up(self, i):
        """
        Percolates node i upper as it possible (until it's value become more
        than it's parent value)
        :type i: int
        :return: None
        """
        cur_pos = i
        while cur_pos // 2 > 0:
            parent_idx = self._parent_idx(cur_pos)
            if self._heap[cur_pos] >= self._heap[parent_idx]:
                break
            self._exchange(cur_pos, parent_idx)
            cur_pos //= 2

    def _percolate_down(self, i):
        """
        Percolates node i to the lowest level of tree
        :type i: int
        :return: None
        """
        while (i * 2) <= len(self):
            min_child_index = self._min_child_idx(i)
            if self._heap[i] > self._heap[min_child_index]:
                self._exchange(i, min_child_index)
            i = min_child_index

    def _min_child_idx(self, i):
        """
        Finds minimum index of possible children nodes
        :type i: int
        :return: minimum child index
        """
        children_indices = self._children_indices(i)
        if not children_indices:
            return None
        children = [self._heap[idx] for idx in children_indices]
        return sorted(zip(children, children_indices))[0][1]

    @staticmethod
    def _parent_idx(i):
        return i // 2

    def _children_indices(self, i):
        """
        Finds children indices of node i if they are already exist in array.
        :type i: int
        :return: indices ofexisted children
        """
        possible_children = [i * 2, (i * 2) + 1]
        return tuple(idx for idx in possible_children if idx <= len(self))

    def get_min(self):
        """
        Returns 1st node (with minimal value)
        :return: 1st value
        """
        if not self:
            raise ValueError("The heap is empty")
        return self._heap[1]

    def pop_min(self):
        """
        Changes places of 1st and last node, pops minimum and percolates new 1st
         value down.
        :return: minimum value
        """
        min_val = self.get_min()
        self._exchange(1, len(self))
        self._heap.pop()
        self._percolate_down(1)
        return min_val

    def push(self, item):
        """
        Adds new node to the last place and percolates it as up as possible
        :type item: Node
        """
        if not isinstance(item, Node):
            raise ValueError("`item` should be a `Node` instance")
        self._heap.append(item)
        self._percolate_up(len(self))


def test_heap():
    heap = MinHeap()
    nodes = [Node(val, val) for val in xrange(9, -1, -1)]
    for node in nodes:
        heap.push(node)
    while heap:
        print(heap.pop_min())


def main():
    test_heap()

if __name__ == "__main__":
    main()

