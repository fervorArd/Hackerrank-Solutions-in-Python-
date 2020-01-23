import re
flag = 0
for i in range(int(input())):
    s = input()
    if re.search(r'.*{',s)!=None:
        flag = 1
    elif s=='}':
        flag = 0
    elif flag:
        mo = re.findall(r'(#[a-fA-F0-9]{3,6})',s)
        [print(i) for i in mo if mo!=[]]
