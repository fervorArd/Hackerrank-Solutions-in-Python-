import re
for i in range(int(input())):
    print('YES') if re.match(r'(7|8|9)(\d{9})$',input())!=None else print('NO')
