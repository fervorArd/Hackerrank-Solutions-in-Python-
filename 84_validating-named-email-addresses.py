import re
for i in range(int(input())):
    string = input()
    mo = re.search(r'<[a-zA-Z][a-zA-Z0-9-_.+]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>',string)
    if mo!=None:
        print(string) 
