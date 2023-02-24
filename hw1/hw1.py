def funky_sum(a, b, mix):
    """
    Returns a mixture between a and b.

    If mix is 0, returns a. If mix is 1, returns b. Otherwise returns a linear
    interpolation between them. If mix is outside the range of 0 and 1, it is
    capped at those numbers.
    """
    if mix < 0:
        return a
    elif mix > 1:
        return b
    else:
        return (1 - mix) * a + mix * b

def count_divisible_digits(n, m):
    if (m == 0):
        return 0
    count = 0
    n = abs(n)
    while (n > 0):         
        val = n % 10
        if (val % m == 0):
            count += 1
        n = n // 10
    return count

def is_relatively_prime(n, m):
    factors_of_n = []
    factors_of_m = []

    for i in range(1, n + 1):
        if n % i == 0:
            factors_of_n.append(i)
    for i in range(1, m + 1):
        if m % i == 0:
            factors_of_m.append(i)

    set_of_factors = set(factors_of_m) & set(factors_of_n)
    return (len(set_of_factors) == 1)


