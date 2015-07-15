#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Autor: Alexey V. Polurotov
# e-mail: niimailtah@gmail.com
# Common nick: Niimailtah
# ----------------------------------------------------------------------------
# https://projecteuler.net/problem=3
# Largest prime factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# ----------------------------------------------------------------------------
from lib.primes import gen_primes


def factor(l):
    result = 1
    for n in l:
        result *= n
    return result

factors = []
n = 600851475143
for prime in gen_primes():
    if n % prime == 0:
        factors.append(prime)
    if factor(factors) == n:
        break

print("The largest prime factor: {}".format(max(factors)))
