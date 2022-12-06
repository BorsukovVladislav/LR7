#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(int, input().split()))

    if len(a) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    a[(a.index(max(a)))], a[0] = a[0], a[(a.index(max(a)))]
    print(a)
