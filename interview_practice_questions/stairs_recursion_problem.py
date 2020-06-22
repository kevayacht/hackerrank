def step_perms(n):
    memo = {}

    def num_ways(n):
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            if memo.get(n):
                return memo.get(n)
            else:
                result = num_ways(n - 1) + num_ways(n - 2) + num_ways(n - 3)
                memo.update({n: result})
                return result

    return num_ways(n)


def main():
    n = 32  # 181997601
    # n = 4  # 7
    result = step_perms(n)
    print(result)


if __name__ == "__main__":
    main()
