#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def subset(a, num, s):
    if num == len(a):
        print(s)
        return
    subset(a, num + 1, s)
    s += str(a[num]) + ' '
    subset(a, num + 1, s)


if __name__ == '__main__':
    my_set = [int(i) for i in input("Enter the set: ").split()]
    subset(my_set, 0, ' ')
