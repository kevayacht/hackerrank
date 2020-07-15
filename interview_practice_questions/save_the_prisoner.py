def save_the_prisoner(n, m, s):
    return ((s - 2 + m) % n) + 1


# s=4,m=4,n=5;

# 3 7 3
# 3

# 5 2 1
# 2

# 5 2 2
# 3

# 7 19 2
# 6

# 352926151 380324688 94730870  # 122129406
# 94431605 679262176 5284458
def main():
    # n = 94431605
    # m = 679262176
    # s = 5284458
    s = 4
    m = 4
    n = 5
    res = save_the_prisoner(n, m, s)
    if res == 23525398:
        print("YES")
    print(res)


if __name__ == "__main__":
    main()
