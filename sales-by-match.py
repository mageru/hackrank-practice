#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs = {}
    for x in range(n):
        try:
            pairs[ar[x]] = pairs[ar[x]]+1
        except KeyError:
            pairs[ar[x]] = 1
    pair_count = sum([value // 2 for value in pairs.values()])
    return pair_count

if __name__ == '__main__':
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)
    print(str(result) + '\n')

