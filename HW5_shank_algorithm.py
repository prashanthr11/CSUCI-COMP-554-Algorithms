from math import sqrt, floor


def multiplicative_inverse(m, n):
    return pow(m, -1, n)


def populate_elements(lst, n, last_element, multiplication_factor, p):
    for i in range(n):
        last_element *= multiplication_factor
        last_element %= p
        lst.append(last_element)


def shank_algorithm(p, g, h):
    n = 1 + floor(sqrt(p))

    L1 = [1]
    last_element = 1
    populate_elements(L1, n, last_element, g, p)

    last_element = L1[-1]

    gm = multiplicative_inverse(last_element, p)

    L2 = [h]
    last_element = h
    populate_elements(L2, n, last_element, gm, p)

    ret = None
    for i, a in enumerate(L1):
        if a in L2:
            j = L2.index(a)
            ret = i + j * n
            return ret

    return ret


p, g, h = 101, 3, 22
p, g, h = 101, 2, 6
answer = shank_algorithm(p, g, h)

if answer:
    print(f'{g} ^ {answer} = {h} mod({p})')
else:
    print('Not found')
