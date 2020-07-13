def angry_prof(a, k):
    on_time = 0

    for i in range(0, len(a)):
        if a[i] <= 0:
            on_time += 1

        if on_time >= k:
            return "NO"

    return "YES"


def main():
    arr = [-1, -3, 4, 2]
    target = 3
    res = angry_prof(arr, target)
    print(res)

    arr = [0, -1, 2, 1]
    target = 2
    res = angry_prof(arr, target)
    print(res)


if __name__ == "__main__":
    main()
