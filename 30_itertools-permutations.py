from itertools import permutations

S,k = input().split()
result = sorted(list(permutations(list(S),int(k))))
for i in result:
    print(''.join(list(i)))
