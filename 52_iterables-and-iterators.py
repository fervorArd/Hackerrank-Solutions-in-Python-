from itertools import combinations
num = int(input())
count = 0
combine = list(combinations(input().split(' '),int(input())))
for i in combine:
    if 'a' in i:
        count += 1
print(count/len(combine))
