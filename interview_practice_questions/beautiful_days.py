def int_reversal(n):
    return int(str(n)[::-1])


def beautiful_days(i, j, k):
    beautiful_count = 0

    for n in range(i, j+1):
        numbers = abs(n - int_reversal(n))
        if numbers == 0:
            beautiful_count += 1
        elif numbers % k == 0:
            beautiful_count += 1

    return beautiful_count


def main():
    i = 20
    j = 23
    k = 6
    res = beautiful_days(i, j, k)
    print(res)

    i = 0
    j = 0
    k = 0
    res = beautiful_days(i, j, k)
    print(res)


if __name__ == "__main__":
    main()
