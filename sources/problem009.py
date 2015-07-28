#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Autor: Alexey V. Polurotov
# e-mail: niimailtah@gmail.com
# Common nick: Niimailtah
# ----------------------------------------------------------------------------
# https://projecteuler.net/problem=9
# Special Pythagorean triplet
# Problem 9
# 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
#
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product a*b*c.
# ----------------------------------------------------------------------------


def find_triplet(N):
    for x in range(1, N):
        y = x + 1
        z = y + 1
        while z <= N:
            while z*z < x*x + y*y:
                z += 1
            if z*z == x*x + y*y and z <= N and x+y+z == 1000:
                return [x, y, z]
            y += 1
    return []

l = find_triplet(1001)
if len(l):
    print(l, '->', l[0]*l[1]*l[2])
