A = set(map(int,input().split()))
flag = 0
for i in range(int(input())):
    B = set(map(int,input().split()))
    if not A.issuperset(B):
        flag = 1 
print('True') if flag==0 else print('False')
