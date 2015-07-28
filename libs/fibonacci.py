#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fibonacci():
    """Fibonacci numbers generator
    """
    a, b, i = 0, 1, 0
    while True:
        yield a, i
        a, b, i = b, a + b, i + 1


if __name__ == "__main__":
    for f, index in fibonacci():
        if index == 10:
            break
    print(f)
