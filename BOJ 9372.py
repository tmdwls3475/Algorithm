# 그래프, 트리

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    N, M = map(int, sys.stdin.readline().split())
    
    for _ in range(M):
        a, b = map(int,sys.stdin.readline().split())
    
    print(n - 1)