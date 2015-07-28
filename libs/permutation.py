import itertools


# -------------------------------------------------------------------------
# https://docs.python.org/2/library/itertools.html#itertools.permutations
def all_perms2(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms2(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


def permutations2(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in itertools.product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


if __name__ == "__main__":
    print('-' * 40)
    for i1 in all_perms2([1, 2, 3]):
        print(i1)
    print('-' * 40)
    for i2 in permutations2([1, 2, 3]):
        print(i2)
    print('-' * 10, ' instant tool (string) ', '-' * 10)
    for i3 in itertools.permutations('ABC', 3):
        print(i3)
    print('-' * 10, ' instant tool (list)', '-' * 10)
    for i4 in itertools.permutations([1, 2, 3], 3):
        print(i4)
