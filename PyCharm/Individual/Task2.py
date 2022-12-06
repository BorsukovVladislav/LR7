#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list()
    sum_item = 0
    proizv_item = 1
    max_id = a.index(max(a))
    min_id = a.index(min(a))

    for i, item in enumerate(a):
        if item < 0:
            sum_item += item
    print(f"Сумма отрицательных элементов: {sum_item}")

    if max_id < min_id:
        b = a[max_id + 1:min_id]
    else:
        b = a[min_id + 1:max_id]

    for i, item in enumerate(b):
        proizv_item *= item
    print(f"Произведение элементов между максимальным и минимальным: {proizv_item}")
