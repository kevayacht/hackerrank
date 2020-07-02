def reverse_array(a):
    finalist = []

    for i in reversed(a):
        finalist.append(i)

    return finalist


def main():
    a = [6676, 3216, 4063, 8373, 423, 586, 8850, 6762]

    result = reverse_array(a)
    print(*result, sep=" ")


if __name__ == "__main__":
    main()
