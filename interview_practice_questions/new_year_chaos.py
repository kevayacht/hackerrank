def minimum_bribes_old(q):
    count = 0
    negative_count = 0
    for index, value in enumerate(q):
        print(index + 1, value, abs(value - (index + 1)))

        test = value - (index + 1)
        print(test)
        if 0 <= test < 3:
            count += test
        elif test < 0:
            negative_count += test
        else:
            return "Too chaotic"

    return count


def minimum_bribes(q):

    count = 0
    for index, value in enumerate(q):

        if value - (index + 1) >= 3:
            return "Too chaotic"

        for i in range(max(value-2, 0), (index+1)):
            if q[i] > value:
                count += 1

    return count


def main():
    # q = [2, 1, 5, 3, 4]
    # q = [2, 5, 1, 3, 4]
    # q = [5, 1, 2, 3, 7, 8, 6, 4]
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    # q = [1, 2, 3, 4, 5, 6, 7, 8]
    # q = [1, 2, 5, 3, 7, 8, 4, 6]
    result = minimum_bribes(q)
    print(result)


if __name__ == "__main__":
    main()
