from collections import Counter

n = int(input())
country_list = []
for i in range(n):
    country_list.append(input())
total = list(set(country_list))
print(len(total))
