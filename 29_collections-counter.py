from collections import Counter

no_of_shoes = int(input())
dict_shoe = Counter(list(map(int,input().split())))
no_of_customers = int(input())
total = 0
for i in range(no_of_customers):
    size,price = list(map(int,input().split()))
    if dict_shoe[size]!= 0:
        total += price
        dict_shoe[size] = dict_shoe[size]-1
print(total)
