num = int(input())
words = []
for i in range(num):
    words.append(input())
count = {}
for i in words:
    count.setdefault(i,0)
    count[i] = count[i]+1
sorted_list = list(count.items()).sort()
print(len(count))
for i in count.values():
    print(i,end=' ')
