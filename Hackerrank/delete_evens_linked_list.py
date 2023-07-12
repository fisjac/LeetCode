#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



#
# Complete the 'deleteEven' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST listHead as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteEven(listHead):
    # create dummy node and point it to none
    # look through linked list and if value is odd prev.next = curr
    # shift forward
    dummy = SinglyLinkedListNode(0)
    prev = dummy
    curr = listHead

    while curr:
      # print(curr.data)
      if curr.data % 2 != 0:
        # print('linking')
        prev.next = curr
        prev = curr
        curr = curr.next
        # print('snipping tail')
        prev.next = None
      else:
        # print('skipping')
        curr = curr.next
    return dummy.next


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    listHead_count = int(input().strip())

    listHead = SinglyLinkedList()

    for _ in range(listHead_count):
        listHead_item = int(input().strip())
        listHead.insert_node(listHead_item)

    result = deleteEven(listHead.head)

    print_singly_linked_list(result, '\n', fptr)
    fptr.write('\n')

    fptr.close()
