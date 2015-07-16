#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Autor: Alexey V. Polurotov
# e-mail: niimailtah@gmail.com
# Common nick: Niimailtah
# ----------------------------------------------------------------------------
# https://projecteuler.net/problem=15
# Lattice paths
# Problem 15
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
#  +-->-->  +-->--+  +-->--+  +--+--+  +--+--+  +--+--+
#  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
#  +--+--v  +--V-->  +--V--+  V-->-->  V-->--+  V--+--+
#  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
#  +--+--v  +--+--V  +--V-->  +--+--V  +--V-->  V-->-->
#
# How many such routes are there through a 20×20 grid?
