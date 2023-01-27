# 자료구조, 큐

import sys

queue = []
n = int(sys.stdin.readline())

for _ in range(n):
    l = sys.stdin.readline().split()
    
    if l[0] == 'push':
        queue.append(int(l[1]))
    
    elif l[0] == 'pop':
        if len(queue) == 0:
            print(-1)
            continue
        print(queue.pop(0))
    
    elif l[0] == 'size':
        print(len(queue))
    
    elif l[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif l[0] == 'front':
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[0])
        
    elif l[0] == 'back':
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[-1])