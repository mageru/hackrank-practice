arr = [1,4,8,9,11,15,17]

def binary_search(aList, tgt):
    lo = 0
    hi = len(aList) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if tgt < aList[mid]:
            hi = mid - 1
        elif tgt > aList[mid]:
            lo = mid + 1
        else:
            return True
    return False

print(binary_search(arr, 15))