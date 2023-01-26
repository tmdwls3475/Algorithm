# 구현, 정렬

import sys

l = []
n = int(sys.stdin.readline())

for i in range(n):
    N = int(sys.stdin.readline())
    l.append(N)
    
l.sort()

for i in range(n):
    print(l[i])