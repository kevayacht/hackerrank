
from collections import Counter


def sherlockAndAnagrams(s):
    counter = 0

    for chunk in range(1, len(s)):

        arr = ["".join(sorted(s[i:i + chunk])) for i in range(0, len(s)) if
               i + chunk <= len(s)]
        c = Counter(arr)

        for key in c:
            counter += (c[key] * (c[key] - 1)) // 2

    return counter


def sherlock_and_anagrams(s):
    counter = 0

    for index in range(1, len(s)):

        arr = []
        for i in range(0, len(s)):

            if i + index <= len(s):
                arr.append("".join(sorted(s[i:i+index])))

        count = Counter(arr)

        for key in count:
            counter += (count[key] * (count[key] - 1) / 2)

    return counter


def main():
    s = "kkkk"
    # s = "abba"

    result = sherlock_and_anagrams(s)
    print(result)


if __name__ == "__main__":
    main()
