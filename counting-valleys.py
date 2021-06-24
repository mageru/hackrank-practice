#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    level = 0
    valleys = 0
    in_valley = False
    for i in range(steps):
        if path[i] == 'D':
            level -= 1
        else:
            level += 1
        if level < 0:
            in_valley = True
        elif level >= 0:
            print(in_valley)
            if in_valley == True:
                valleys += 1
                in_valley = False
        print(level)
    print("Valleys: " + str(valleys))

if __name__ == '__main__':
    steps = 8
    path = ["U", "D", "D", "D", "U", "D", "U", "U"]

    result = countingValleys(steps, path)

    print(str(result) + '\n')
