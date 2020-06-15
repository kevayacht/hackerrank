def two_strings(s1, s2):
    lookup = dict()
    for i in range(0, len(s1)):
        if lookup.get(s1[i], None) is None:
            lookup.update({s1[i]: 1})
        else:
            lookup[s1[i]] += 1

    for j in range(0, len(s2)):
        if lookup.get(s2[j], 0) != 0:
            return "YES"
    return "NO"


def main():
    s1 = "Hello"
    s2 = "world"
    result = two_strings(s1, s2)
    print(result)


if __name__ == "__main__":
    main()
