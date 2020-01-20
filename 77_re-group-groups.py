s = input()
flag = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        if s[i].isalnum():
            flag = 1
            print(s[i])
            break
if flag == 0:
    print('-1')
