num_of_ele = int(input())
A = set(map(int,input().split()))
for i in range(int(input())):
    operation = input().split()[0]
    B = set(map(int,input().split()))
    if operation == 'intersection_update':
        A.intersection_update(B)
    elif operation == 'update':
        A.update(B)
    elif operation == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    else:
        A.difference_update(B)
print(sum(A))
