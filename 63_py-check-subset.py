for i in range(int(input())):
    ele, A = int(input()),set(map(int,input().split()))
    ele, B = int(input()),set(map(int,input().split()))
    print(A.issubset(B))
