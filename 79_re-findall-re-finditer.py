import re
mo = re.findall(r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})[^aeiouAEIOU]',input())
[print(i) for i in mo] if mo!=[] else print('-1')
