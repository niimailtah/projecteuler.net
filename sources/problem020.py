#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Autor: Alexey V. Polurotov
# e-mail: niimailtah@gmail.com
# Common nick: Niimailtah
# ----------------------------------------------------------------------------
# https://projecteuler.net/problem=20
# Factorial digit sum
# Problem 20
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!


def factor(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result


s = str(factor(100))
factors_sum = 0
for i in range(len(s)):
    factors_sum += int(s[i])
print(factors_sum)
