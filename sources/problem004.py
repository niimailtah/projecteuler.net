#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Autor: Alexey V. Polurotov
# e-mail: niimailtah@gmail.com
# Common nick: Niimailtah
# ----------------------------------------------------------------------------
# https://projecteuler.net/problem=4
# Largest palindrome product
# Problem 4
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# ----------------------------------------------------------------------------

digits = 3
results = {}
for i in range(10 ** (digits - 1), 10 ** digits):
    for j in range(10 ** (digits - 1), 10 ** digits):
        product = str(i * j)
        if product[:digits] == product[digits * 2:digits - 1:-1]:
            results[product] = [i, j]
if results:
    for result in sorted(results):
        print("{} = {} * {}".format(result, results[result][0], results[result][1]))
