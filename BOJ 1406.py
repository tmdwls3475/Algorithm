# 자료구조, 스택, 연결리스트

import sys

s = list(sys.stdin.readline().rstrip())
s_num = len(s)
com_n = int(sys.stdin.readline())

for _ in range(com_n):
    com = list(sys.stdin.readline().split())

    if com[0] == 'L':
        if s_num == 0:
            continue
        s_num -= 1
        
    if com[0] == 'D':
        if s_num == len(s):
            continue
        s_num += 1
        
    if com[0] == 'B':
        if s_num == 0:
            continue
        # del s[s_num - 1]
        s.pop(s_num - 1)
        s_num -= 1
        
    if com[0] == 'P':
        if s_num == len(s):
            s.append(com[1])
        s.insert(s_num, com[1])
        s_num += 1

for i in s:
    print(i, end = '')