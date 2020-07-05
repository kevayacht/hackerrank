def find_number(arr, k):
    for index, value in enumerate(arr):
        print(f"Index: {index}; Value: {value}")
        if value == k:
            return True

    return False


def odd_numbers(l, r):
    # Write your code here
    finalist = []
    for i in range(l, r + 1):
        if i % 2 != 0:  # means its odd
            finalist.append(i)

    return finalist


def odd_numbers_preamble():
    l = 2
    r = 5
    result = odd_numbers(l, r)
    print(result)


def find_number_preamble():
    a = [1, 2, 3, 4, 5]
    k = 6
    result = find_number(a, k)

    if result:
        print("YES")
    else:
        print("NO")


def main():
    # find_number_preamble()
    odd_numbers_preamble()


if __name__ == "__main__":
    main()
