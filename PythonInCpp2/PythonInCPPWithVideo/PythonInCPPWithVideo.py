
from itertools import islice
from random import random
from time import perf_counter

COUNT = 1600000  # Change this value depending on the speed of your computer
DATA = list(islice(iter(lambda: (random() - 0.5) * 3.0, None), COUNT))

e = 2.7182818284590452353602874713527

def sinh(x):
    return (1 - (e ** (-2 * x))) / (2 * (e ** -x))

def cosh(x):
    return (1 + (e ** (-2 * x))) / (2 * (e ** -x))

def tanh(x):
    tanh_x = sinh(x) / cosh(x)
    return tanh_x

from PythonInCPPWithVideo import fast_tanh
print(fast_tanh(0))
#test(lambda d: [fast_tanh(x) for x in d], '[fast_tanh(x) for x in d] (CPython C++ extension)')

def test(fn, name):
    start = perf_counter()
    result = fn(DATA)
    duration = perf_counter() - start
    print('{} took {:.3f} seconds\n\n'.format(name, duration))

    for d in result:
        assert -1 <= d <= 1, " incorrect values"

if __name__ == "__main__":
    test(lambda d: [tanh(x) for x in d], '[tanh(x) for x in d] (Python implementation)')
    test(lambda d: [fast_tanh(x) for x in d], '[fast_tanh(x) for x in d] (CPython C++ extension)')

