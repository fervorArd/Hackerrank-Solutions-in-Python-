n,m = input().split()
arr = input().split()
A = set(input().split())
B = set(input().split())
happiness = 0
for i in range(int(n)):
    if arr[i] in A:
        happiness += 1
    elif arr[i] in B:
        happiness -= 1
print(happiness)
