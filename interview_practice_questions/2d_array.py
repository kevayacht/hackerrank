def hour_glass_sum(arr):
    """
    O(n^2)
    :return:
    """
    max_sum = -99999

    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):
            hour_glass = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i][j] + arr[i + 1][j - 1] + arr[i + 1][
                j] + arr[i + 1][j + 1]

            if max_sum < hour_glass:
                max_sum = hour_glass

    return max_sum


def main():
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    result = hour_glass_sum(arr)
    print(result)


if __name__ == "__main__":
    main()

#
# import math
# import os
# import random
# import re
# import sys
#
# # Complete the hourglassSum function below.
# def hourglassSum(arr):
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     arr = []
#
#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))
#
#     result = hourglassSum(arr)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
