# 트리, 재귀

import sys

def pre_tra(t):
    pre_list.append(t)
    
    if tree[t][0] != 0:
        pre_tra(tree[t][0])
    
    if tree[t][1] != 0:
        pre_tra(tree[t][1])
        
def ino_tra(t):
    if tree[t][0] != 0 and tree[t][1] != 0:
        ino_tra(tree[t][0])
        ino_list.append(t)
        ino_tra(tree[t][1])
    
    if tree[t][0] != 0 and tree[t][1] == 0:
        ino_tra(tree[t][0])
        ino_list.append(t)
        
    if tree[t][0] == 0 and tree[t][1] != 0:
        ino_list.append(t)
        ino_tra(tree[t][1])
        
    if tree[t][0] == 0 and tree[t][1] == 0:
        ino_list.append(t)

def pos_tra(t):
    if tree[t][0] != 0 and tree[t][1] != 0:
        pos_tra(tree[t][0])
        pos_tra(tree[t][1])
        pos_list.append(t)
    
    if tree[t][0] != 0 and tree[t][1] == 0:
        pos_tra(tree[t][0])
        pos_list.append(t)
        
    if tree[t][0] == 0 and tree[t][1] != 0:
        pos_tra(tree[t][1])
        pos_list.append(t)
        
    if tree[t][0] == 0 and tree[t][1] == 0:
        pos_list.append(t)
    
pre_list = []
ino_list = []
pos_list = []

tree = {}
n = int(sys.stdin.readline())

for _ in range(n):
    n1, n2, n3 = sys.stdin.readline().split()
    
    if n2 == '.':
        n2 = 0
    
    if n3 == '.':
        n3 = 0
        
    if n1 not in tree:
        tree[f'{n1}'] = (n2, n3)

pre_tra('A')
ino_tra('A')
pos_tra('A')

for i in pre_list:
    print(i, end = '')
print()
for i in ino_list:
    print(i, end = '')
print()
for i in pos_list:
    print(i, end = '')