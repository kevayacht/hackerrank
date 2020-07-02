
def is_valid(s):

    booklet = {}

    # cater for the zero string case
    if s == "":
        return True

    for i in range(len(s)):
        if booklet.get(s[i]) is None:
            booklet[s[i]] = 1
        else:
            booklet[s[i]] += 1

        min_value = 0
        max_value = 0
        min_key = 0
        max_key = 0
    for key, value in booklet.items():
        print(key, value)
        if min_value >= value:
            min_key = key
        if max_value <= value:
            max_key = key

    print(booklet)


def main():
    s = "abc"
    result = is_valid(s)

    if result:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()