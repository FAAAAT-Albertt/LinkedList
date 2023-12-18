from typing import *
import time

class Node:
    """реализация узла"""
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data) + " -> " + str(self.next)


class LinkedList:
    """реализация всего связанного списка"""
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        return str(self.head)


    def merge(self, head1=None, head2=None):
        pass


def romanToInt(nums1: list[int]=[1,2,2,1], nums2: list[int]=[2,2]) -> bool:

    return "asdasdas".count("a")




if __name__ == '__main__':
    linked_list = LinkedList()
    temp = Node(1)
    temp.next = Node(2)
    temp.next.next = Node(3)
    print(romanToInt())
