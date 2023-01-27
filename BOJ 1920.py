# 자료구조, 정렬, 이분탐색

import sys

def binary_search(arr, value):
    first, last = 0, len(arr) - 1

    while first <= last:
        mid = (first + last) // 2
        
        if arr[mid] == value:
            return True
        
        if arr[mid] > value:
            last = mid - 1
            
        else:
            first = mid + 1
    
    return False

n = int(sys.stdin.readline())
N = list(sys.stdin.readline().split())
N.sort()

m = int(sys.stdin.readline())
M = list(sys.stdin.readline().split())

for i in M:
    if binary_search(N, i):
        print(1)
    else:
        print(0)