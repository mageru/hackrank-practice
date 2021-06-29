#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max_sum = -sys.maxsize
    for y_pos in range(4):
        for x_pos in range(4):
            total = arr[y_pos][x_pos] + arr[y_pos][x_pos+1] + arr[y_pos][x_pos+2]
            total = total + arr[y_pos+1][x_pos+1]
            total = total + arr[y_pos+2][x_pos] + arr[y_pos+2][x_pos+1] + arr[y_pos+2][x_pos+2]
            if total > max_sum:
                max_sum = total
    return max_sum

"""
    arr = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    arr = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
"""
if __name__ == '__main__':
    arr = [
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5],
    ]

    result = hourglassSum(arr)
    print(str(result) + '\n')