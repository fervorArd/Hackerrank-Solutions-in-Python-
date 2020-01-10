from collections import defaultdict

n,m = list(map(int,input().split()))
d = defaultdict(list)
for i in range(n):
    d['A'].append(input())
for i in range(m):
    alpha = input()
    num = 0
    for i in d['A']:
        num += 1
        if alpha==i:
            print(num,end=' ')
    if alpha not in d['A']:
        print('-1',end='')
    print()
