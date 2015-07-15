#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Autor: Alexey V. Polurotov
# e-mail: niimailtah@gmail.com
# Common nick: Niimailtah
# ----------------------------------------------------------------------------
# https://projecteuler.net/problem=10
# Summation of primes
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# ----------------------------------------------------------------------------
from libs.primes import gen_primes


s = 0
for prime in gen_primes():
    if prime > 2 * 10 ** 6:
        print("Sum: {}".format(s))
        break
    s += prime
