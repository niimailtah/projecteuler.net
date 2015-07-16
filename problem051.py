#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Autor: Alexey V. Polurotov
# e-mail: niimailtah@gmail.com
# Common nick: Niimailtah
# ----------------------------------------------------------------------------
# https://projecteuler.net/problem=51
# Prime digit replacements
# Problem 51
#
# By replacing the 1st digit of the 2-digit number *3,
# it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example
#  having seven primes among the ten generated numbers,
#  yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
#  Consequently 56003, being the first member of this family, is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
# is part of an eight prime value family.

"""
So to break it down we need to categorize numbers into families,

A Family is a number that:
- Have the same number of digits
- Have one (or more of the same) digit repeated in the same position(s)

So within a (certain number of digits) there are "Templates" and within each template there are "Families"
 and within each family there are 10 generated numbers (9 if zero is preceding)

For example (*) being the replaced part and (x) being the static part of the number,

A 2 Digits number -> has two templates (*x) and (x*) -> each template has 10 families -> each family has 10 generated
 numbers (Ignore leading zeros)

EDIT: A template DOES NOT have 10 families its much more depending on how many (*) there are however a family does have
 a 10 generated numbers.
----------------------------------------------------------------------------------------------------
Here are the results as well as the generating family form:
1:11 {11} **
2:23 {23,29} 2*
3:41 {41,43,47} 4*
4:2 {2,3,5,7} *
5:11 {11,31,41,51,71} *1
6:13 {13,23,43,53,73,83} *3
7:56003 {56003, 56113, 56333, 56443, 56663, 56773, 56993} 56**3
8:omitted for obvious reason
9: is taking a long time with my VERY inefficient code so didn't get an answer.
"""
