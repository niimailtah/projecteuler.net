#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Autor: Alexey V. Polurotov
# e-mail: niimailtah@gmail.com
# Common nick: Niimailtah
# ----------------------------------------------------------------------------
# https://projecteuler.net/problem=14
# Longest Collatz sequence
# Problem 14
#
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def seq(n):
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        result.append(n)
    return result


max_length = 1
start_number = 1
for current_number in range(1, 10**6):
    chain_length = len(seq(current_number))
    print(max_length, current_number, chain_length)
    if chain_length > max_length:
        max_length = chain_length
        start_number = current_number

print(start_number)
