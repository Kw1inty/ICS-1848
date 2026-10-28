def digit_sum(n):
    s = 0
    for d in str(n):
        s += int(d)
    return s


def max_digit(n):
    return max(int(d) for d in str(n))


def min_digit(n):
    return min(int(d) for d in str(n))
