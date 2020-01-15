len_a = int(input())
a = set(input().split())
len_b = int(input())
b = set(input().split())
result = sorted(list(map(int,list(a.union(b)-a.intersection(b)))))
for i in result:
    print(i)
