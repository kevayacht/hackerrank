def make_anagram(a, b):
    from string import ascii_letters

    count = 0
    for letter in ascii_letters:
        ia = a.count(letter)
        ib = b.count(letter)
        count += abs(ia - ib)

    return count




def main():
    s1 = ""
    s2 = ""
    result = make_anagram(s1, s2)
    print(result)


if __name__ == "__main__":
    main()