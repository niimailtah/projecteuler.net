#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import math


# -----------------------------------------------------------------------
# http://rebrained.com/?p=458
def prime1(up_to=100):
    return filter(lambda num: (num % numpy.arange(2, 1 + int(math.sqrt(num)))).all(), range(2, up_to + 1))


def prime2(up_to=100):
    return filter(lambda num: numpy.array([num % factor for factor in range(2, 1 + int(math.sqrt(num)))]).all(),
                  range(2, up_to + 1))


def prime3(up_to=100):
    return list[2] + filter(lambda num: (num % numpy.arange(3, 1 + int(math.sqrt(num)), 2)).all(),
                            range(3, up_to + 1, 2))


def prime4(up_to=100):
    primes = [2]
    for num in range(3, up_to + 1, 2):
        is_prime = True
        for factor in range(3, 1 + int(math.sqrt(num)), 2):
            if not num % factor:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def prime5(up_to):
    primes = numpy.arange(2, up_to + 1)
    is_prime = numpy.ones(up_to - 1, dtype=bool)
    for factor in primes[:int(math.sqrt(up_to))]:
        if is_prime[factor - 2]:
            is_prime[factor * 2 - 2::factor] = 0
    return primes[is_prime]


def prime6(up_to):
    primes = numpy.arange(3, up_to + 1, 2)
    is_prime = numpy.ones((up_to - 1) / 2, dtype=bool)
    for factor in primes[:int(math.sqrt(up_to))]:
        if is_prime[(factor - 2) / 2]:
            is_prime[(factor * 3 - 2) / 2::factor] = 0
    return numpy.insert(primes[is_prime], 0, 2)


def fast_prime_sieve(up_to):
    possible_primes = range(3, up_to + 1, 2)
    curr_index = -1
    max_index = len(possible_primes)
    for latest_prime in possible_primes:
        curr_index += 1
        if not latest_prime: continue
        for index_variable_not_named_j in range((curr_index + latest_prime), max_index, latest_prime):
            possible_primes[index_variable_not_named_j] = 0
    possible_primes.insert(0, 2)
    return [x for x in possible_primes if x > 0]


# -----------------------------------------------------------------------
# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1
