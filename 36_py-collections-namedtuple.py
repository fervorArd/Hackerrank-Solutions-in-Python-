from collections import namedtuple

n = int(input())
Student = namedtuple('Student',input().split())
total = 0
for i in range(n):
    S = Student(*(input().split()))
    total += int(S.MARKS)
print(total/n)
