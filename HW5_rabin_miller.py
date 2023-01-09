from random import randint


binary_n = "10101001"
binary_n = "1100"
binary_n = "1001111111111"


def miller_test(n, d):
    random_number = randint(2, n - 2)
    x = pow(random_number, d, n)  # (random_number^d) % n

    if x == 1 or x == n - 1:
        return True

    while True:
        x = pow(x, 2, n)

        if x == 1 or d == n - 1:
            return False

        if x == n - 1:
            return True

        d <<= 1


def rabin_miller(n, k=5):

    if n < 2:
        return False

    if n <= 3:
        return True

    if n % 2 == 0:
        return False

    # n - 1 = r * (2 ^ d)
    r = n - 1

    while r and r & 1 == 0:
        r >>= 1

    for i in range(k):
        if not miller_test(n, r):
            return False

    return True


def main(n_binary):
    try:
        n = int(n_binary, 2)
        result = rabin_miller(n)
        print(f'{n_binary} ({n}) is prime? {result}')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main(binary_n)
