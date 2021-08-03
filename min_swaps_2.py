import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps_attempt(arr):
    size = arr[0]
    swap = 0
    for i in range(size):
        search = arr[i]
        print("search: "+str(search))
        curr_min_val = arr[i]
        curr_min_index = i
        for j in range(size):
            if arr[j] < curr_min_val:
               curr_min_val = arr[j]
               curr_min_index = j
               print("curr_min: "+ str(curr_min_val))
        arr[i] = arr[curr_min_index]
        arr[curr_min_index] = search
        swap += 1
    print(arr)
    print(str(swap))

def minimumSwaps(arr):
    swaps = 0
    n = len(arr)
    #iterate over entire array
    for i in range(0,n):
        #it's good practice to use a boolean guided function in a long for loop,
        #while will evaluate and IF the statement in it is true it will continue
        #I used the consecutive, increasing values to swap by index
        while arr[i] != (i+1):
            #temp is the correct index of arr[i]
            temp = arr[i]-1
            temp2 = arr[i]
            temp3 = i
            #swap this with whatever element is where arr[temp] is, this will
            #continue to swap until arr[i] == index+1
            arr[i], arr[temp] = arr[temp], arr[i]
            #increase swaps
            swaps+=1
    return swaps



if __name__ == '__main__':
    #ar = [7, 1, 3, 2, 4, 5, 6]
    ar = [1, 3, 5, 2, 4, 6, 7]
    #ar = [2,3,4,1,5]

    result = minimumSwaps(ar)
    print(str(result) + '\n')