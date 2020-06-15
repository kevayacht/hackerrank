def do_count(s):
    count = 0
    for i, c in enumerate(s):
        if c == "a":
            count += 1
    return count


def repeated_string(s, n):
    """

    :return:
    """

    single_string_count = do_count(s)

    string_length = len(s)
    quotient = n // string_length
    remainder = n % string_length

    single_string_count*quotient

    remainder_string_count = do_count(s[:remainder])

    return single_string_count*quotient + remainder_string_count


def main():
    s = "aba"
    n = 10
    result = repeated_string(s, n)
    print(result)


if __name__ == "__main__":
    main()
