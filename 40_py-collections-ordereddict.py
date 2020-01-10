from collections import OrderedDict

ordered_dict = OrderedDict()

for i in range(int(input())):
    returnedList = input().split()
    price = int(returnedList[-1])
    returnedList.pop()
    item = ' '.join(returnedList)
    if item in ordered_dict:
        price = ordered_dict[item] + price
        ordered_dict[item] = price
    else:
        ordered_dict[item] = price
        
for keys,values in ordered_dict.items():
    print(keys + ' ' + str(values))
