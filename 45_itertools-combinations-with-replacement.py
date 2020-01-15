from itertools import combinations_with_replacement

string = input().split()
string[0] = sorted(list(string[0]))
returnedList = list(combinations_with_replacement(string[0],int(string[1])))
for j in sorted(returnedList):
    print(''.join(list(j)))
