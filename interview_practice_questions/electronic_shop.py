
def getMoneySpent(keyboards, drives, b):  # brute force

    maximum_in_budget = -1
    for n in range(len(keyboards)):
        for m in range(len(drives)):
            if keyboards[n] + drives[m] <= b:
                if maximum_in_budget < keyboards[n] + drives[m]:
                    maximum_in_budget = keyboards[n] + drives[m]

    return maximum_in_budget


def main():
    print("Hello")
    keyboards = [3, 1]
    drives = [5, 2, 8]
    b = 10
    result = getMoneySpent(keyboards, drives, b)
    print(result)

    keyboards = [4]
    drives = [5]
    b = 5
    result = getMoneySpent(keyboards, drives, b)
    print(result)


if __name__ == "__main__":
    main()
