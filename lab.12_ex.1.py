#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def rec(n):
    if n == 1:
        return 1
    return n + rec(n - 1)


if __name__ == '__main__':
    n = int(input("Enter n: "))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(f"Сумма без рекурсии: {sum}")
    print(f"Сумма с рекурсией: {rec(n)}")
