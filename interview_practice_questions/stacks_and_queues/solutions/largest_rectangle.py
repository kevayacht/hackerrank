import math
import os
import random
import re
import sys


def rectangle_area(q):
    height = min(q, key=int)
    length = len(q)
    return height * length


# Complete the largestRectangle function below.
def largest_rectangle(h):
    """
    Notes:
        Since technically actual order doesnt matter and we need the are of the rectangle by using the min height in
        a queue or list, we can just bank on that, but if we did need to order an list into an intelligible output
        we would just need to loop through an use the queue and stack functions to build one that is accurate,
        remember stacks: LIFO, Queues: FIFO.

    :param h:
    :return:
    """
    largest = 0
    queue = []

    for i in range(0, len(h)):
        # print(f"Outer loop Index: {i}; Variable: {h[i]}")

        j = 0
        adjacent_queue = []
        while i + j < len(h):
            # print(f"i: {i}; j: {j}; h[i-j]: {h[i-j]}; h[i]: {h[i]}")
            if h[i+j] >= h[i]:
                adjacent_queue.append(h[i+j])
                j += 1
            else:
                break
        # print(f"Forward Queue: {adjacent_queue}")

        j = 1
        adjacent_stack = []
        while i - j >= 0:
            # print(f"i: {i}; j: {j}; h[i-j]: {h[i-j]}; h[i]: {h[i]}")
            if h[i-j] >= h[i]:
                adjacent_stack.append(h[i-j])
                j += 1
            else:
                break
        # print(f"Backward Queue: {adjacent_stack}")

        queue = adjacent_queue + adjacent_stack
        temp = rectangle_area(queue)
        if temp > largest:
            largest = temp
        # print(f"Full queue: {queue}; Area: {temp}; Current Largest: {largest}")

    return largest





def main():
    # input_list = [1, 2, 3, 4, 5]
    input_list = [1, 3, 6, 8, 7, 2, 4, 1]
    #
    result = largest_rectangle(input_list)
    print(result)


if __name__ == '__main__':
    main()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input())
    #
    # h = list(map(int, input().rstrip().split()))
    #
    # result = largestRectangle(h)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()

    # def largestRectangle(h):
    #     h.append(0)
    #     stack = []
    #     maxArea = (0, 0, 0, 0)
    #     for i, height in enumerate(h):
    #         j = i
    #         while stack and stack[-1][1] >= height:
    #             j, last = stack.pop()
    #             area = (i - j) * last
    #             if area > maxArea[0]:
    #                 maxArea = (area, j, i, last)
    #         stack.append((j, height))
    #     print
    #     maxArea
    #     return maxArea[0]

    # def largestRectangle(h):
    #     s = []
    #     ans = len(h)
    #     h.append(0)
    #
    #     for i in range(len(h)):
    #         left_index = i
    #         while len(s) > 0 and s[-1][0] >= h[i]:
    #             last = s.pop()
    #             left_index = last[1]
    #             ans = max(ans, h[i] * (i + 1 - last[1]))
    #             ans = max(ans, last[0] * (i - last[1]))
    #         s.append((h[i], left_index))
    #
    #     return ans

#     if h[i+j] >= h[i]:
#         print(f"h[i+j]: {h[i+j]}; h[i]: {h[i]}")
#         adjacent_queue.append(h[i+j])
#         j += 1
#     else:
#         break
#
# print(f"Queue: {adjacent_queue}")


# while True:
#     if h[j-1] >= h[i]:
#         adjacent_stack.append(h[j-1])
#     if h[j+1] >= h[i]:
#         adjacent_queue.append(h[j+1])
#     print(f"h[i]: {h[i]}; h[j]: {h[j]}")
#     print(f"Queue: {adjacent_queue}")
#     print(f"Stack: {adjacent_stack}")
#     j += 1

# height that was seen * (value.now - where.is.started)

# if current >= h[i-1]:
#     adjacent_queue.append(current)

# adjacent_queue = []
# for j in range(0, len(h)):
#     if h[j] >= h[i]:
#         adjacent_queue.append(h[j])
#     else:
#         pass

# print(f"Made Queue: {adjacent_queue}; Area: {rectangle_area(adjacent_queue)}")
