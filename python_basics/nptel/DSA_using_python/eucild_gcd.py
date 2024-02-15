def euclid_gcd(m, n):
    if m < n:
        (m, n) = (n, m)
    if m % n == 0:
        return n
    else:
        diff = m - n
        # diff > n ? Possible!
        return euclid_gcd(max(n, diff), min(n, diff))


print(euclid_gcd(15, 36))
