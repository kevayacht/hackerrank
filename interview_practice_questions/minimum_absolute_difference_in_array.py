

def minimum_absolute_difference(arr):
    finalist = []
    arr.sort()
    for i in range(len(arr)-1):
        finalist.append(abs(arr[i] - arr[i + 1]))
    return min(finalist)


def main():
    # myarray = [-2, 2, 4]
    myarray = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
    result = minimum_absolute_difference(myarray)
    print(result)


if __name__ == "__main__":
    main()
