N = int(input())
for i in range(N):
    x, y = input().split()
    try:
        print(int(x)//int(y))
    except ZeroDivisionError as e:
        print("Error Code:",e) 
    except ValueError as v:
        print("Error Code:",v)
