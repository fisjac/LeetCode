#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getPotentialOfWinner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY potential
#  2. LONG_INTEGER k
#
from collections import deque

def getPotentialOfWinner(potential, k):
  if k > len(potential):
    return max(potential)

  queue = deque(potential)
  wins = 0
  while wins < k:
    left = queue.popleft()
    right = queue.popleft()
    if left > right:
      wins += 1
      queue.appendleft(left)
      queue.append(right)
    else:
      wins = 1
      queue.appendleft(right)
      queue.append(left)
  return queue[0]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    potential_count = int(input().strip())

    potential = []

    for _ in range(potential_count):
        potential_item = int(input().strip())
        potential.append(potential_item)

    k = int(input().strip())

    result = getPotentialOfWinner(potential, k)

    fptr.write(str(result) + '\n')

    fptr.close()
