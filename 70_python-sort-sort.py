import math
import os
import random
import re
import sys
from operator import itemgetter


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    [print(' '.join(map(str, i))) for i in sorted(arr, key = itemgetter(k))]
         
