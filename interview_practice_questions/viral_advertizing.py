
def viral_advertising(n):
    shares = 5
    cumulative = 0

    while n > 0:
        likes = shares//2
        shares = likes*3
        cumulative += likes
        n -= 1

    return cumulative


def main():
    n = 5
    res = viral_advertising(n)
    print(res)

if __name__ == "__main__":
    main()
