""" practice on linked lists
"""
from typing import Union, Any


class LinkedListNode:
    """
    Node to be used in linked list

    === Attributes ===
    next_ - successor to this LinkedListNode
    next_ - successor to this LinkedListNode
    value - data this LinkedListNode represents
    """
    next_: Union["LinkedListNode", None]
    value: object

    def __init__(self, value: object,
                 next_: Union["LinkedListNode", None] = None) -> None:
        """
        Create LinkedListNode self with data value and successor next_.
        """
        self.value = value
        self.next_ = next_

    def __str__(self) -> str:
        """
        Return a user-friendly representation of this LinkedListNode.

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        # start with a string s to represent current node.
        s = "{} ->".format(self.value)
        # create a reference to "walk" along the list
        current_node = self.next_
        # for each subsequent node in the list, build s
        while current_node is not None:
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        # add "|" at the end of the list
        assert current_node is None, "unexpected non_None!!!"
        s += "|"
        return s

    def __eq__(self, other):
        """
        Return whether LinkedListNode self is equivalent to other.

        @param LinkedListNode self: this LinkedListNode
        @param LinkedListNode|object other: object to compare to self.
        @rtype: bool

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """
        left_node = self
        right_node = other

        while (type(other) == type(self)) and (left_node is not None) and\
                (right_node is not None) and \
                (left_node.value == right_node.value):
            left_node = left_node.next_
            right_node = right_node.next_
        return left_node is None and right_node is None


class LinkedList:
    """
    Collection of LinkedListNodes

    === Attributes ==
    front - first node of this LinkedList
    back - last node of this LinkedList
    size - number of nodes in this LinkedList, >= 0
    """
    front: Union[LinkedListNode, None]
    back: Union[LinkedListNode, None]
    size: int

    def __init__(self) -> None:
        """
        Create an empty linked list.
        """
        self.front = None
        self.back = None
        self.size = 0

    def __str__(self) -> str:
        """
        Return a human-friendly string representation of
        LinkedList self.

        >>> lnk = LinkedList()
        >>> print(lnk)
        Empty!
        >>> lnk.prepend(5)
        >>> print(lnk)
        5 ->| Size: 1
        """
        # deal with the case where this list is empty
        if self.front is None:
            assert self.back is None and self.size is 0, "ooooops!"
            return "Empty!"
        # use front.__str__() if this list isn't empty
        return str(self.front) + " Size: {}".format(self.size)

    def __eq__(self, other: Any) -> bool:
        """
        Return whether LinkedList self is equivalent to
        other.

        >>> LinkedList().__eq__(None)
        False
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(5)
        >>> lnk.__eq__(lnk2)
        True
        """
        return (type(self) == type(other)) and (self.front == other.front) and \
               (self.size == other.size)

    def delete_after(self, value: object) -> None:
        """
        Remove the node following the first occurrence of value, if
        possible, otherwise leave self unchanged.

        >>> lnk = LinkedList()
        >>> lnk.append(7)
        >>> lnk.append(6)
        >>> lnk.append(5)
        >>> print(lnk)
        7 -> 6 -> 5 ->| Size: 3

        >>> lnk.delete_after(5)
        >>> print(lnk)
        7 -> 6 -> 5 ->| Size: 3

        >>> lnk.delete_after(7)
        >>> print(lnk)
        7 -> 5 ->| Size: 2

        >>> lnk = LinkedList()
        >>> lnk.append(1)
        >>> lnk.append(2)
        >>> lnk.append(3)
        >>> lnk.append(4)
        >>> lnk.append(5)
        >>> lnk.delete_after(4)
        >>> print(lnk)
        1 -> 2 -> 3 -> 4 ->| Size: 4
        >>> print(lnk.back)
        4 ->|

        """
        current_node = self.front
        while current_node.next_ is not None:
            if current_node.value == value:
                if current_node.next_ == self.back:
                    self.back = current_node
                current_node.next_ = current_node.next_.next_
                self.size -= 1
                break
            current_node = current_node.next_

    def append(self, value: object) -> None:
        """
        Insert a new LinkedListNode with value after self.back.

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk.front)
        5 ->|
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk.front)
        5 -> 6 ->|
        """
        # create the new node
        new_node = LinkedListNode(value)
        # if the list is empty, the new node is front and back
        if self.size == 0:
            assert self.back is None and self.front is None, "ooops"
            self.front = self.back = new_node
        # if the list isn't empty, front stays the same
        else:
            # change *old* self.back.next_ first!!!!
            self.back.next_ = new_node
            self.back = new_node
        # remember to increase the size
        self.size += 1

    def prepend(self, value: object) -> None:
        """
        Insert value before LinkedList self.front.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> str(lnk.front)
        '2 -> 1 -> 0 ->|'
        >>> lnk.size
        3
        """
        # Create new node with next_ referring to front
        new_node = LinkedListNode(value, self.front)
        # change front
        self.front = new_node
        # if the list was empty, change back
        if self.size == 0:
            self.back = new_node
        # update size
        self.size += 1

    def delete_front(self) -> None:
        """
        Delete LinkedListNode self.front from self.

        Assume self.front is not None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.delete_front()
        >>> str(lnk.front)
        '1 -> 0 ->|'
        >>> lnk.size
        2
        >>> lnk.delete_front()
        >>> lnk.delete_front()
        >>> str(lnk.front)
        'None'
        """
        assert self.front is not None, "unexpected None!"
        # if back == front, set it to None
        if self.front == self.back:
            self.back = None
        # set front to its successor
        self.front = self.front.next_
        # decrease size
        self.size -= 1

    def __setitem__(self, index: int, value: object) -> None:
        """
        Set the value of list at position index to value. Raise IndexError
        if index >= self.size or index < -self.size

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> print(lnk)
        5 ->| Size: 1
        >>> lnk[0] = 7
        >>> print(lnk)
        7 ->| Size: 1

        >>> lnk.prepend(6)
        >>> lnk.prepend(5)
        >>> lnk.prepend(4)
        >>> print(lnk)
        4 -> 5 -> 6 -> 7 ->| Size: 4

        >>> lnk[2] = 1
        >>> print(lnk)
        4 -> 5 -> 1 -> 7 ->| Size: 4

        >>> lnk[-1] = 1
        >>> print(lnk)
        4 -> 5 -> 1 -> 1 ->| Size: 4
        """
        if (index >= self.size) or (index < self.size * -1):
            raise IndexError('Index out of range!')
        if index < 0:
            index += self.size

        current_node = self.front

        for _ in range(index):
            current_node = current_node.next_
            assert current_node is not None, "unexpected None!!!!!"
        current_node.value = value

    def __add__(self, other: "LinkedList") -> "LinkedList":
        """
        Return a new list by concatenating self to other.  Leave
        both self and other unchanged.

        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(7)
        >>> print(lnk1 + lnk2)
        5 -> 7 ->| Size: 2
        """
        new_linked_list = LinkedList()

        ll_1 = self.front
        while ll_1 is not None:
            new_linked_list.append(ll_1.value)
            ll_1 = ll_1.next_

        ll_2 = other.front
        while ll_2 is not None:
            new_linked_list.append(ll_2.value)
            ll_2 = ll_2.next_

        return new_linked_list

    def insert_before(self, value1: object, value2: object) -> None:
        """
        Insert value1 into LinkedList self before the first occurrence
        of value2, if it exists.  Otherwise leave self unchanged.
        """
        new_node = LinkedListNode(value1)

        if value2 == self.front:
            self.prepend(value1)
        else:
            val2_found = False

            cur_node = self.front
            prev_node = None
            while cur_node.value is not None and val2_found is False:
                if cur_node.value == value2:
                    prev_node.next_ = new_node
                    new_node.next_ = cur_node

                prev_node = cur_node
                cur_node = cur_node.next_

    def copy(self) -> "LinkedList":
        """
        Return a copy of LinkedList self.  The copy should have
        different nodes, but equivalent values, from self.

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk.prepend(7)
        >>> print(lnk.copy())
        7 -> 5 ->| Size: 2
        """
        return_list = LinkedList()
        current_node = self.front
        while current_node is not None:
            return_list.append(current_node.value)
            current_node = current_node.next_
        return return_list

    def __len__(self) -> int:
        """
        Return the number of nodes in LinkedList self.
        """
        return self.size

    def __getitem__(self, index: int) -> object:
        """
        Return the value at LinkedList self's position index.

        >>> lnk = LinkedList()
        >>> lnk.append(1)
        >>> lnk.append(0)
        >>> lnk.__getitem__(1)
        0
        >>> lnk[-1]
        0
        """
        # deal with a negative index by adding self.size
        if (-self.size > index
                or index > self.size):
            raise IndexError("out of range!!!")
        elif index < 0:
            index += self.size
        current_node = self.front
        # walk index steps along from 0 to retrieve element
        for _ in range(index):
            assert current_node is not None, "unexpected None!!!!!"
            current_node = current_node.next_
        # return the value at position index
        return current_node.value

    def __contains__(self, value: object) -> bool:
        """
        Return whether LinkedList self contains value.

        >>> lnk = LinkedList()
        >>> lnk.append(0)
        >>> lnk.append(1)
        >>> lnk.append(2)
        >>> 2 in lnk
        True
        >>> lnk.__contains__(3)
        False
        """
        current_node = self.front
        # "walk" the linked list
        while current_node is not None:
            # if any node has a value == value, return True
            if current_node.value == value:
                return True
            current_node = current_node.next_
        # if you get to the end without finding value,
        # return False
        return False

    # def swap(self, i: int, j: int) -> None:
    #     """
    #     Swap the values at indicies i and j.
    #
    #     >>> linky = LinkedList()
    #     >>> linky.append(10)
    #     >>> linky.append(20)
    #     >>> linky.append(30)
    #     >>> linky.append(40)
    #     >>> linky.append(50)
    #     >>> print(linky)
    #     10 -> 20 -> 30 -> 40 -> 50 ->| Size: 5
    #
    #     >>> linky.swap(0, 3)
    #     >>> print(linky)
    #     40 -> 20 -> 30 -> 10 -> 50 ->| Size: 5
    #     """
    #     if (i or j >= self.size) or (i or j < self.size * -1):
    #         raise IndexError('wtf')
    #
    #     if i < 0:
    #         i += self.size
    #     if j < 0:
    #         j += self.size
    #
    #     first_swap_node = self.front
    #     for z in range(i):
    #         first_swap_node = first_swap_node.next_
    #
    #     second_swap_node = self.front
    #     for t in range(j):
    #         second_swap_node = second_swap_node.next_
    #     val2 = second_swap_node.value
    #
    #     second_swap_node.value = first_swap_node.value
    #     first_swap_node.value = val2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="pylint.txt")
