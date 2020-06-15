def bubble_sort(arr):
    count = 0
    iterations = 0

    length = len(arr)
    for i in range(length):

        swapped = False
        for j in range(length-1-i):       # don't test the last one, array end.
            iterations += 1

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
                swapped = True

        if not swapped:
            break

    return arr[0], arr[len(arr)-1], count, iterations


def main():
    arr = [1,4, 8, 9, 3, 5, 7, 6, 2]
    first_element, last_element, count, iterations = bubble_sort(arr)
    print("Array is sorted in {count} swaps.".format(count=count))
    print(f"First Element: {first_element}")
    print(f"Last Element: {last_element}")

    print(f"Sorting iterations in {iterations}.")


if __name__ == "__main__":
    main()