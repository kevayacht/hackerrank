def alternating_characters(s):
    count = 0

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1

    return count


def main():
    s = "ABABBABAABBAA"
    s = "AAAAABBB"
    result = alternating_characters(s)
    print(result)


if __name__ == "__main__":
    main()