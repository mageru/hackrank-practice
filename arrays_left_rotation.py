#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    rotated = [False] * len(a)
    for x in range(d):
        print("Iteration: "+str(x))
        print("a: "+ str(a))
        for y in range(len(a)):
            if y < (len(a)-1):
                rotated[y] = a[y+1]
            else:
                rotated[y] = a[0]
            print(rotated)
        print(rotated)
        a = rotated.copy()
    return rotated

if __name__ == '__main__':
    #n = 5
    #d = 4
    #a = [1,2,3,4,5]

    n = 15
    d = 13
    a = [33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97]

    result = rotLeft(a, d)

    print(str(result) + '\n')