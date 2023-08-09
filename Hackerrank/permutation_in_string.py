#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'check_inclusion' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def check_inclusion(s1, s2):
  if len(s1) > len(s2):
    return False
    # could try sorting
    # sort s1, then for each cross section resort (len(s1)log(len(s1)) + len(s1)) * len(s2 - s1)

    # could try building a dict with counts for each len(s1)
    # copy dict and remove each from count.
    # delete key from dict if count drops to 0
    # if dict is ever empty, return current slice
    # mem len(s1) time len(s1) * len(s2 - s1)
    # lets go with option 2

  counts = dict()
  for char in s1:
    counts[char] = counts.get(char, 0) + 1

  for left in range(len(s2) - len(s1) + 1):
    counts_copy = counts.copy()
    subsection = s2[left:left+len(s1)]
    for char in subsection:
      if char in counts_copy:
        counts_copy[char] -= 1
        if counts_copy[char] == 0:
          del counts_copy[char]
      else:
        break
    if len(counts_copy.keys()) == 0:
      return True
  return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = check_inclusion(s1, s2)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
