import textwrap
from collections import OrderedDict
def merge_the_tools(string, k):
    t = textwrap.wrap(text=string,width=k)
    for i in t:
        print(''.join(OrderedDict.fromkeys(i)))
          
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
