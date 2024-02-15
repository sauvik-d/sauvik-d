def gcd(m, n):
    cf = []
    for i in range(1, min(m, n)+1):
        if m % i == 0 and n % i == 0:
            cf.append(i)
    return cf[-1]


print(gcd(14, 77))


def new_gcd(m, n):
    mrcf = 1
    for i in range(1, min(m, n)+1):
        if m % i == 0 and n % i == 0:
            mrcf = i

    return mrcf


def scan_back_gcd(m, n):
    i = min(m, n)
    while i > 0:
        if m % i == 0 and n % i == 0:
            return i
        else:
            i = i - 1


print(new_gcd(34, 51))
print(scan_back_gcd(85, 34))
