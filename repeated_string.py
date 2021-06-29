#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

# need to optimize - thinking calc per cycle then divide cycle size by total and multiply that 
def repeatedString_unoptimized(s, n):
    a_count = 0
    counter = 0
    orig_size = len(s)

    while counter <= n:
        repeat = s
        counter = counter + orig_size
        for i in range(orig_size):
            if repeat[i] == 'a':
                a_count += 1
            if counter >= n:
                break
    return a_count

# optimized passable solution
def repeatedString(s, n):
    a_count = 0
    counter = 0
    size_s = len(s)

    for i in range(size_s):
        if s[i] == 'a':
            a_count += 1

    total_repetitions = n // size_s
    a_total = total_repetitions * a_count
    remainder = n % size_s
    for x in range(remainder):
        print(x)
        if s[x] == 'a':
            a_total += 1
    return a_total

if __name__ == '__main__':
    #s = 'abcac'
    #n = 10
    #s = 'a'
    #n = 1000000000000
    s = 'aba'
    n = 10

    result = repeatedString(s, n)
    print(str(result) + '\n')
