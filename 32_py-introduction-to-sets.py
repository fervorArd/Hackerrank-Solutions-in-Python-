import statistics

def average(array):
    arr = list(set(array))
    return statistics.mean(arr)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
