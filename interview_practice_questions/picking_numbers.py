def picking_numbers(arr):
    ll = []
    cl = []

    arr.sort()

    for i in range(0, len(arr)):

        if len(cl) == 0:
            cl.append(arr[i])
        elif abs(arr[i] - cl[0]) <= 1:
            cl.append(arr[i])
        else:
            if len(ll) < len(cl):
                ll = []
                ll = ll + cl
            cl.clear()
            cl.append(arr[i])

    if len(ll) < len(cl):
        return len(cl)
    return len(ll)


def main():
    # arr = [1, 1, 2, 2, 4, 4, 5, 5, 5]
    # arr = [1, 1, 2, 2, 4, 4, 5, 5, 5]
    arr = [6, 6, 6, 6, 6, 6, 6]
    res = picking_numbers(arr)
    print(res)


if __name__ == "__main__":
    main()
