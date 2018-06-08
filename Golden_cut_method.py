#coding: utf-8
import math
# import numpy as np
def f(x):
    return (3 * (x**2) - 2 * math.tan(x))

def gold(a, b, epsilon, delta, G):
    t = (math.sqrt(5) - 1) / 2
    h = b - a
    fa = f(a)
    fb = f(b)
    p = a + (1-t)*h
    q = a + t*h
    fp = f(p)
    fq = f(q)
    i = 1
    G.append([a, p, q, b])
    while (abs(fb-fa) > delta) or (h > epsilon):
        if fp <= fq:
            b = q
            fb = fq
            q = p
            fq = fp
            h = b - a
            p = a + (1 - t) * h
            fp = f(p)

        else:
            a = p
            fa = fp
            p = q
            fp = fq
            h = b - a
            q = a + t*h
            fq = f(q)
        i += 1
        G.append([a, p, q, b])
    if fp <= fq:
        s = p
        fs = fp
    else:
        s = q
        fs = fq
    ds = abs(b-a)
    df = abs(fb-fa)
    return i, s, fs, ds, df, G
if __name__ == '__main__':
    a = 0
    b = 1
    epsilon = 10 ** -4
    delta = 10 ** -5
    G = []
    i, s, fs, ds, df, G = gold(a, b, epsilon, delta, G)
    print(i, s, fs)
