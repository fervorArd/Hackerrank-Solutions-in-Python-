groups = int(input())
room_numbers = input().split(' ');count = {}
for i in room_numbers:
    count.setdefault(i,0);count[i] += 1
[print(i) for i in count if count[i]==1]
