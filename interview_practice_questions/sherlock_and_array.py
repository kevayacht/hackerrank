def balance(arr):
    final = sum(arr)
    left = 0
    for i in arr:
        left += i
        if left == final + i - left:
            return 'YES'
    return 'NO'


def main():
    arr = [5, 6, 8, 11]
    result = balance(arr)
    print(result)  # YES

    arr = [1, 2, 3]
    result = balance(arr)
    print(result)  # NO

    arr = [1, 2, 3, 3]
    result = balance(arr)
    print(result)  # YES

    arr = [1, 1, 4, 1, 1]
    result = balance(arr)
    print(result)  # YES

    arr = [2, 0, 0, 0]
    result = balance(arr)
    print(result)  # YES

    arr = [0, 0, 2, 0]
    result = balance(arr)
    print(result)  # YES


if __name__ == "__main__":
    main()
