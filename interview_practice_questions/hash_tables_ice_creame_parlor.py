def what_flavors_bf(cost, money):
    for i in range(0, len(cost)):
        for j in range(i + 1, len(cost)):
            if cost[i] > money or cost[j] > money:
                pass
            elif cost[i] + cost[j] == money:
                return [i, j]


def what_flavors_map(cost, money):
    hash_map = {cost[i]: i + 1 for i in range(0, len(cost))}

    for j in range(0, len(cost)):
        key_ = money - cost[j]
        if key_ in hash_map and hash_map[key_] != j + 1:
            return [j + 1, hash_map[key_]]


def main():
    cost = [1, 4, 5, 3, 2]
    money = 4
    result = what_flavors_map(cost, money)
    print(f"{result[0]} {result[1]}")

    cost = [2, 2, 4, 3]
    money = 4
    result = what_flavors_map(cost, money)
    print(f"{result[0]} {result[1]}")


if __name__ == "__main__":
    main()
