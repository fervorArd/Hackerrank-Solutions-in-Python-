from itertools import product
k, m = map(int, input().split())
mylist = []
for i in range(k):
    mylist.append(list(map(int, input().split()))[1:])
maxi = -1
for i in product(*mylist):
    op = sum(x**2 for x in i)%m
    if op>maxi:
        maxi = op
print(maxi)
