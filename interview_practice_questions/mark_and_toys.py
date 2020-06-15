def greedy_selection_sort(arr, k):
    count = 0

    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            print(f"arr[j]: {arr[j]}; arr[minimum]: {arr[minimum]}")
            if arr[j] < arr[minimum]:
                minimum = j

        print(f"Swop: {arr[minimum]} // {arr[i]}")
        arr[minimum], arr[i] = arr[i], arr[minimum]
        k -= arr[i]
        print(f"Res: {k}")
        if k >= 0:
            count += 1
        else:
            break
    return count


def max_toys(arr, k):
    count = 0
    for i in range(len(arr)):
        k -= arr[i]
        if k >= 0:
            count += 1
        else:
            break
    return count


def maximumToys(price, k):
    count = 0
    price.sort()
    print(price)
    for i in range(len(price)):
        print(price)
        k -= price[i]
        if k >= 0:
            count += 1
        else:
            break
    return count


def main():
    # arr = [1, 2, 3, 4, 5, 7, 10, 15, 20]
    arr = [1, 12, 5, 111, 200, 1000, 10]
    k = 50
    # arr = selection_sort(arr)
    # result = max_toys(arr, k)
    result = maximumToys(arr, k)
    print(result)


if __name__ == "__main__":
    main()
