#!/usr/bin/python3
"""Triangle Triangle"""


def pascal_triangle(n):
    """Triangle"""
    if r <= 0:
        return []
    pas = [[1]]
    for row_number in range(1, r):
        row = [1]
        for i in range(1, row_number):
            element = pas[row_number - 1][i - 1] + pas[row_number - 1][i]
            row.append(element)
        row.append(1)
        pas.append(row)

    return pas
