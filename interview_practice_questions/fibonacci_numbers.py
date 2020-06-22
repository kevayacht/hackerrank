def rec_fib(n):
    if n <= 1:
        return n
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)


def fibonacci(n):
    series = []
    for i in range(n + 1):
        series.append(rec_fib(i))

    return series[n]


def main():
    n = 6
    result = fibonacci(n)
    print(result)


if __name__ == "__main__":
    main()
