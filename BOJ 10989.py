# 정렬

import sys

l = [0 for _ in range(10001)]
n = int(sys.stdin.readline())

for _ in range(n):
    N = int(sys.stdin.readline())
    l[N] += 1

for i in range(10001):
    for _ in range(l[i]):
        print(i)