#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    countn=0 
    countp=0
    counto=0
    for i in range (n):
        if arr[i] < 0:
            countn += 1
        elif arr[i] > 0:
            countp += 1
        else:
            counto +=1
    print(str(countp/n).format(1.6))
    print(str(countn/n).format(1.6))
    print(str(counto/n).format(1.6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
