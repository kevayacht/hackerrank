
def rot_left(d, arr):

    rem = d % len(arr)
    a = []

    for i in range(len(arr)):
        a.append(arr[(i + rem) % len(arr)])
        print(arr[(i + rem) % len(arr)])

    return a


def main():
    d = 4
    arr = [1, 2, 3, 4, 5]
    result = rot_left(d, arr)
    print(result)


if __name__ == "__main__":
    main()