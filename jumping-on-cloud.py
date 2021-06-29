#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#
def jumpingOnClouds(path):
    jump_to = 0
    ans = 0
    steps = len(path)
    path.append('#')

    while jump_to < steps-1:
        jump_to += (path[jump_to + 2] == 0) + 1
        ans += 1
    return ans




if __name__ == '__main__':
    #steps = 7
    #path = [0,0,1,0,0,1,0]

    steps = 6
    path = [0,0,0,1,0,0]

    result = jumpingOnClouds(path)

    print(str(result) + '\n')