import re

for i in range(int(input())):
    try:
        sub = input()
        re.sub(sub,sub,sub)
        print('True')
    except Exception as err:
        print('False')
