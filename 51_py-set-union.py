n = int(input())
s = set(list(map(int,input().split())))
b = int(input())
k = set(list(map(int,input().split())))
print(len(list(s.union(k))))
