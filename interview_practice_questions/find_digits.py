#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the findDigits function below.
def findDigits(n):
    origin = n
    digits = [int(x) for x in str(n)]

    count = 0
    for item in digits:
        if item != 0 and origin % item == 0:
            count += 1

    return count


if __name__ == '__main__':
    n = 1012
    result = findDigits(n)
    print(result)
