def jumping_on_clouds(c):
    """
    Cloud jumping algorithm.

    Assumptions:
     1. always possible to win.
     2. index 0 will never be a 1, and is by default a 0.

     O(n): a single for loop, will scale linearly as array size increases.

    :param c: list: input array
    :return: jumps: (int): total jumps needed.
    """
    path: list = []

    for i, val in enumerate(c):

        if c[i] == 0:
            if len(path) > 1 and i-2 == path[-2] and i-1 == path[-1]:
                path.pop()
            path.append(i)

    return len(path) - 1


def main():
    # c: list = [0, 0, 1, 0, 0, 1, 0]
    c: list = [0, 1, 0, 0, 0, 1, 0]
    result = jumping_on_clouds(c)
    print(result)


if __name__ == "__main__":
    main()
