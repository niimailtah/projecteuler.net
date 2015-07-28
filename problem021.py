#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Autor: Alexey V. Polurotov
# e-mail: niimailtah@gmail.com
# Common nick: Niimailtah
# ----------------------------------------------------------------------------
# https://projecteuler.net/problem=21
# Amicable numbers
# Problem 21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
#  and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
from functools import reduce


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def sum_of_factors(n):
    f = factors(n)
    f.remove(n)
    result = 0
    for i in f:
        result += i
    return result


amicable_numbers = []
for number in range(2, 10001):
    candidate = sum_of_factors(number)
    if sum_of_factors(candidate) == number and candidate != number:
        if number not in amicable_numbers:
            amicable_numbers.append(number)
        if candidate not in amicable_numbers:
            amicable_numbers.append(candidate)
s = 0
for i in amicable_numbers:
    s += i
print(s)
