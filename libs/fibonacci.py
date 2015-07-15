#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fibonacci():
    """Fibonacci numbers generator
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
