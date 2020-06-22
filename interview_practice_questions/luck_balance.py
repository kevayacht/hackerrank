

def luck_balance(k, contests):
    contests.sort(reverse=True)
    luck_stat = 0

    for contest in contests:
        if contest[1] == 0: # always take the unimportant matche's luck
            luck_stat += contest[0]
        elif k > 0:
            luck_stat += contest[0]
            k -= 1
        else:
            luck_stat -= contest[0]
    return luck_stat


def main():
    n = 6
    k = 3
    contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
    result = luck_balance(k, contests)
    print(result)


if __name__ == "__main__":
    main()