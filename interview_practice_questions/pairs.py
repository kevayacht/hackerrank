def pairs(k, arr):
    hash_map = {arr[i]: i for i in range(0, len(arr))}
    hash_list = []

    for i in range(0, len(arr)):
        key_ = k + arr[i]
        if key_ in hash_map:
            hash_list.append([arr[i], key_])

    return len(hash_list)


def main():
    k = 1
    arr = [1, 2, 3, 4]
    result = pairs(k, arr)
    print(result)

    k = 2
    arr = [1, 5, 3, 4, 2]
    result = pairs(k, arr)
    print(result)


if __name__ == "__main__":
    main()
