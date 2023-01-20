# 자료구조, 스택
import sys

stack = []
count = 0
n = int(sys.stdin.readline())

for _ in range(n):
    l = sys.stdin.readline().split()
    
    if l[0] == 'push':
        stack.append(int(l[1]))
    
    elif l[0] == 'pop':
        if len(stack) == 0:
            print(-1)
            count += 1
            continue
        print(stack.pop())
        count += 1
    
    elif l[0] == 'size':
        print(len(stack))
        count += 1
    
    elif l[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
        count += 1
    
    elif l[0] == 'top':
        if len(stack) == 0:
            print(-1)
            count += 1
            continue
        print(stack[-1])
        count += 1