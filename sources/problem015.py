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
#
#graph = {'0,0': ['0,1', '1,0'],
#         '0,1': ['0,2', '1,1'],
#         '0,2': ['1,2'],
#         '1,0': ['1,1', '2,0'],
#         '1,1': ['1,2', '2,1'],
#         '1,2': ['2,2'],
#         '2,0': ['2,1'],
#         '2,1': ['2,2'],
#         '2,2': []}


def gen_diamond_graph(length):
  result = {}
  for i in range(length + 1):
    for j in range(length + 1):
      key = "{},{}".format(i, j)
      result[key] = []
      if j < length:
        right = "{},{}".format(i, j + 1)
        result[key].append(right)
      if i < length:
        left = "{},{}".format(i + 1, j)
        result[key].append(left)
  return result


def find_path(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return path
  if start not in graph:
    return None
  for node in graph[start]:
    if node not in path:
      newpath = find_path(graph, node, end, path)
      if newpath:
        return newpath
  return None


def find_all_paths(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return [path]
  if start not in graph:
    return []
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
      for newpath in newpaths:
        paths.append(newpath)
  return paths


def find_shortest_path(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return path
  if start not in graph:
    return None
  shortest = None
  for node in graph[start]:
    if node not in path:
      newpath = find_shortest_path(graph, node, end, path)
      if newpath:
        if not shortest or len(newpath) < len(shortest):
          shortest = newpath
  return shortest

length = 4
graph = gen_diamond_graph(length)

for key in sorted(graph.keys()):
  print("Graph[{}] -> {}".format(key, graph[key]))
start, end = "{},{}".format(0, 0), "{},{}".format(length, length)
print(len(find_all_paths(graph, start, end)))
