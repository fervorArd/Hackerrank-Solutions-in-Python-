import re
for i in range(int(input())):
    print(bool(re.match(r'^[+-]?\d*\.\d+$',input())))
