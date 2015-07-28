#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Autor: Alexey V. Polurotov
# e-mail: niimailtah@gmail.com
# Common nick: Niimailtah
# ----------------------------------------------------------------------------
# https://projecteuler.net/problem=6
# Sum square difference
# Problem 6
#
# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 55**2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and
# the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# ----------------------------------------------------------------------------


def sum_of_the_squares(n):
    result = 0
    for i in range(1, n + 1):
        result += i ** 2
    return result


def square_of_the_sum(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result ** 2


print(square_of_the_sum(100) - sum_of_the_squares(100))
