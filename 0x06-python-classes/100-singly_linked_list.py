#!/usr/bin/python3
"""Define classes for a singly-linked list"""

class Node:
    """Represents a node"""

    def __init__(self, data, next_node=None):
        """Satrts a new Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the dtata of Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get the next_node of Node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Depicts a singly-linked list"""

    def __init__(self):
        """Starts a new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Put a new Node  to SinglyLinkedList
        Args:
            value/ Node: new Node to be inserted
        """
        nw = Node(value)
        if self.__head is None:
            nw.next_node = None
            self.__head = nw
        elif self.__head.data > value:
            nw.next_node = self.__head
            self.__head = nw
        else:
            t = self.__head
            while (t.next_node is not None and
                    t.next_node.data < value):
                t = t.next_node
            nw.next_node = t.next_node
            t.next_node = nw

    def __str__(self):
        """defines the print() depicting SinglyLinkedList"""
        vals = []
        t = self.__head
        while t is not None:
            vals.append(str(t.data))
            t = t.next_node
        return ('\n'.join(vals))

