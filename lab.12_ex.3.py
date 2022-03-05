#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import sys


class TailRecurseException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func



def factorial_rec(n, acc=1):
    if n == 0:
        return acc
    return factorial_rec(n - 1, n * acc)



def fib_rec(i, current=0, next=1):
    if i == 0:
        return current
    else:
        return fib_rec(i - 1, next, current + next)


def factorial_iter(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def fib_iter(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a


if __name__ == '__main__':
    number = int(input("Enter the number: "))

    start_time = timeit.default_timer()
    factorial_rec(number)
    print("Recursive factorial time is: ",
          timeit.default_timer() - start_time
          )

    start_time = timeit.default_timer()
    factorial_iter(number)
    print("Iterative factorial time is :",
          timeit.default_timer() - start_time
          )

    start_time = timeit.default_timer()
    fib_rec(number)
    print("Recursive Fibonacci time is :",
          timeit.default_timer() - start_time
          )

    start_time = timeit.default_timer()
    fib_iter(number)
    print("Iterative Fibonacci time is :",
          timeit.default_timer() - start_time
          )

