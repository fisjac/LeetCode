#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'two_sum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER target
#

def two_sum(numbers, target):
    # Write your code
    # initialize l and r pointers at 0 and 1
    # if sum of both == target return [l+ 1,r + 1]
    # if sum is greater than target l+= 1 and reset r


    for left_idx in range(len(numbers)-1):
      l, r = left_idx, left_idx + 1
      for right_idx in range(r,len(numbers)):
        total = numbers[left_idx] + numbers[right_idx]
        if total == target:
          return [left_idx + 1, right_idx + 1]
        if total > target:
          break

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    target = int(input().strip())

    result = two_sum(numbers, target)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
