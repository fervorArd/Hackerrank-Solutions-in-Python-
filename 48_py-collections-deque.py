from collections import deque
N = int(input())
d = deque()
for i in range(N):
    op_list = input().split()
    if op_list[0]=='append':
        d.append(op_list[1])
    elif op_list[0]=='appendleft':
        d.appendleft(op_list[1])
    elif op_list[0]=='pop':
        d.pop()
    elif op_list[0]=='popleft':
        d.popleft()
print(' '.join(d))
