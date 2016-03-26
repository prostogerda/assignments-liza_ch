#! /usr/bin/env python


from __future__ import print_function, division


class Node(object):
    def __init__(self, value, parent=None, l_child=None, r_child=None):
        self._value = value
        self._parent = parent
        self._l_child = l_child
        self._r_child = r_child

    @property
    def value(self):
        return self._value

    @property
    def parent(self):
        return self._parent

    @property
    def l_child(self):
        return self._l_child

    @property
    def r_child(self):
        return self._r_child

    def __str__(self):
        return str((self.value, self._parent, self._l_child, self._r_child))

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value


class SearchTree(object):
    def __init__(self):
        self._node = []

    def push(self, new_node):
        """
        :type new_node: Node
        :param new_node:
        :return:
        """
        if not isinstance(new_node, Node):
            raise ValueError("`new_node` should be a `Node` instance")
        if not SearchTree:
            self._node.append = new_node
        current_node = self._node[0]
        while current_node.l_child or current_node.r_child:
            if new_node > current_node and not current_node.l_child:
                new_node._parent = current_node
                current_node.l_child = new_node
                break
            if new_node <= current_node and not current_node.r_child:
                new_node._parent = current_node
                current_node.r_child = new_node
                break
            if new_node > current_node and current_node.l_child:
                current_node = current_node.l_child
                continue
            if new_node <= current_node and current_node.r_child:
                current_node = current_node.r_child
                continue

    @staticmethod
    def _exchange(self, node1, node2):
        """
        :type node1: Node
        :param node1:
        :type node2: Node
        :param node2:
        :return:
        """
        node1._parent, node2._parent = node2.parent, node1.parent
        node1._l_child, node2._l_child = node2.l_child, node1.l_child
        node1._r_child, node2._r_child = node2.r_child, node1.r_child

    # def _percolate_down(self, ):
    #     while (i * 2) <= len(self):
    #         min_child_index = self._min_child_idx(i)
    #         if self._node[i] > self._node[min_child_index]:
    #             self._exchange(i, min_child_index)
    #         i = min_child_index
    #
    # def _children_indices(self, i):
    #     possible_children = [i * 2, (i * 2) + 1]
    #     return tuple(idx for idx in possible_children if idx <= len(self))
    #
    # def get_min(self):
    #     if not self:
    #         raise ValueError("The heap is empty")
    #     return self._node[1]
    #
    # def pop_min(self):
    #     min_val = self.get_min()
    #     self._exchange(1, len(self))
    #     self._node.pop()
    #     self._percolate_down(1)
    #     return min_val
    #
    # def push(self, item):
    #     if not isinstance(item, Node):
    #         raise ValueError("`item` should be a `Node` instance")
    #     self._node.append(item)
    #     self._percolate_up(len(self))


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

