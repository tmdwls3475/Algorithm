# 자료구조, 덱

import sys

deque = []
n = int(sys.stdin.readline())

for _ in range(n):
    l = sys.stdin.readline().split()
    
    if l[0] == 'push_front':
        deque.insert(0, int(l[1]))
    
    elif l[0] == 'push_back':
        deque.append(int(l[1]))
        
    elif l[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
            continue
        print(deque.pop(0))
    
    elif l[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
            continue
        print(deque.pop())
        
    elif l[0] == 'size':
        print(len(deque))
    
    elif l[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    
    elif l[0] == 'front':
        if len(deque) == 0:
            print(-1)
            continue
        print(deque[0])
        
    elif l[0] == 'back':
        if len(deque) == 0:
            print(-1)
            continue
        print(deque[-1])