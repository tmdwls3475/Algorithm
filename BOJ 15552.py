# 수학, 구현, 사칙연산

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    N, M = map(int, sys.stdin.readline().split())
    print(N + M)