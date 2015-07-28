#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Autor: Alexey V. Polurotov
# e-mail: niimailtah@gmail.com
# Common nick: Niimailtah
# ----------------------------------------------------------------------------
# https://projecteuler.net/problem=5
# Smallest multiple
# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# ----------------------------------------------------------------------------


def check(n):
    for i in range(2, 21):
        if n % i != 0:
            return False
    return True


for number in range(1, 10 ** 9):
    if check(number):
        print(number)
        break
