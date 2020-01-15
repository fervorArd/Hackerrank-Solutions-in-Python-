from itertools import combinations

string = input().split()
string[0] = sorted(list(string[0]))
for i in range(1,int(string[1])+1):
    returnedList = list(combinations(string[0],i))
    returnedList.sort()
    for j in returnedList:
        print(''.join(list(j)))
