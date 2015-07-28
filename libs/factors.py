#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# -----------------------------------------------------------------------
# http://rosettacode.org/wiki/Factors_of_an_integer#Python
from math import sqrt
from itertools import chain, cycle, accumulate  # last of which is Python 3 only


def factors1(n):
    return [i for i in range(1, n + 1) if not n % i]


def factors2(n):
    return [i for i in range(1, n//2 + 1) if not n % i] + [n]


def factors3(n):
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)


def factors4(n):
    def prime_powers(number):
        # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
        for c in accumulate(chain([2, 1, 2], cycle([2, 4]))):
            if c*c > number:
                break
            if number % c:
                continue
            d,p = (), c
            while not number % c:
                number, p, d = number//c, p*c, d + (p,)
            yield(d)
        if number > 1:
            yield((number,))

    r = [1]
    for e in prime_powers(n):
        r += [a*b for a in r for b in e]
    return r
