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
def repeatedString(s, n):
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

if __name__ == '__main__':
    #s = 'abcac'
    s = 'a'
    n = 1000000000000

    result = repeatedString(s, n)
    print(str(result) + '\n')
