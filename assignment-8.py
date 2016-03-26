#! /usr/bin/env python


from __future__ import print_function, division
import random


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
        if not self._node:
            self._node.append(new_node)
        else:
            current_node = self._node[0]
            self._node.append(new_node)
            while current_node:
                if new_node > current_node and not current_node.r_child:
                    new_node._parent = current_node
                    current_node._r_child = new_node
                    break
                if new_node <= current_node and not current_node.l_child:
                    new_node._parent = current_node
                    current_node._l_child = new_node
                    break
                if new_node > current_node and current_node.r_child:
                    current_node = current_node.r_child
                elif new_node <= current_node and current_node.l_child:
                    current_node = current_node.l_child

    # @staticmethod
    # def _exchange_links(node1, node2):
    #     """
    #     :type node1: Node
    #     :param node1:
    #     :type node2: Node
    #     :param node2:
    #     :return:
    #     """
    #     node1._parent, node2._parent = node2.parent, node1.parent
    #     node1._l_child, node2._l_child = node2.l_child, node1.l_child
    #     node1._r_child, node2._r_child = node2.r_child, node1.r_child

    @staticmethod
    def _exchange_values(node1, node2):
        """
        :type node1: Node
        :param node1:
        :type node2: Node
        :param node2:
        :return:
        """
        node1._value, node2._value = node2.value, node1.value

    def __contains__(self, item):
        search_node = Node(item)
        current_node = self._node[0]
        while current_node:
            if search_node == current_node:
                return True
            elif search_node > current_node:
                if not current_node.r_child:
                    return False
                current_node = current_node.r_child
            else:
                if not current_node.l_child:
                    return False
                current_node = current_node.l_child
        return False

    def pop(self, value):
        pop_value = Node(value)
        if pop_value not in self._node:
            return None
        current_node = self._node[0]
        while current_node:
            if pop_value == current_node:
                if not current_node.r_child:
                    current_node.parent._r_child = current_node.l_child
                    current_node.l_child._parent = current_node.parent
                elif not current_node.l_child:
                    current_node.parent._r_child = current_node.r_child
                    current_node.r_child._parent = current_node.parent
                else:
                    self._exchange_values(current_node, current_node.r_child)
            elif pop_value <= current_node:
                current_node = current_node.l_child
            else:
                current_node = current_node.r_child
        return value if current_node else None


def make_search_tree(lst):
    root = lst[random.randint(0, len(lst)-1)]
    tree = SearchTree()
    for i in xrange(len(lst)):
        if i != root:
            tree.push(Node(lst[i]))
    return tree


def test_tree():
    tree = SearchTree()
    nodes = [8, 4, 10, 2, 3, 1, 9, 11, 15]
    for num in nodes:
        tree.push(Node(num))
    for node in nodes:
        tree.pop(node)
        # node in tree
    # nodes2 = [8, 4, 10, 2, 3, 1, 9, 11, 15]
    # make_search_tree(nodes2)
    # tree = SearchTree()
    # nodes = [Node(random.randint(1, 20)) for _ in xrange(10)]
    # while tree:
    #     print(tree.pop(random.randint(1, 20)))


def main():
    test_tree()

if __name__ == "__main__":
    main()

