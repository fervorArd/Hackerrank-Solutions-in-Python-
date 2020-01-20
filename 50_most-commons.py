import math
import os
import random
import re
import sys
from collections import Counter 

if __name__ == '__main__':
    s = sorted(input().strip())
    s_counter = Counter(s).most_common()
    for i in range(3):
        print(s_counter[i][0], s_counter[i][1])
