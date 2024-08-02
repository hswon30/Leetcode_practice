#https: // www.acmicpc.net / problem / 1456

# finding prime num, only need to search for n**0.5 space
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# finding all almost prime numbers (any a <= n**i <= b where n = prime and i >= 2)
def is_almost_prime(a, b):
    res = 0

    for num in range(2, int(b ** 0.5) + 1):
        if is_prime(num):
            exp = 2
            mult = num
            while num <= b:
                num = pow(mult, exp)
                exp += 1
                if num >= a and num <= b:
                    res += 1
        else:
            continue
    return res

# test case
print(is_almost_prime(5324, 894739))


