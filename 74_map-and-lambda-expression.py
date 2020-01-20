cube = lambda x: int(x)**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fibo = []
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        b,c = 0,1
        for i in range(2,n):
            a = b
            b = c
            c = a + b
            fibo.append(c)
        return [0, 1] + fibo
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
