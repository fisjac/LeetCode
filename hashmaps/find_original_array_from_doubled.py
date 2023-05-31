#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findOriginalArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY changed as parameter.
#

def findOriginalArray(changed):
    if len(changed) % 2 != 0 or len(changed) < 2:
        return []
    seen = set()
    res = []

    for val in changed:
        if val % 2 == 0:
            if int(val/2) in seen:
                res.append(int(val/2))
                seen.remove(int(val/2))
            elif int(val * 2) in seen:
                res.append(val)
                seen.remove(int(val * 2))
            else:
                seen.add(val)
        else:
            if val in seen:
                res.append(val)
                seen.remove(val)
            else:
                seen.add(val)
        print(val, seen, res)
    if len(seen) > 0:
        return []
    else: return res


if __name__ == '__main__':
