N,X = list(map(int,input().split()));Z = []
for i in range(X):
    Z.append(list(map(float,input().split())))
[print(sum(i)/X) for i in zip(*Z)]
