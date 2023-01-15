import math

A, B = map(int, input().split())

count = 0


def compute(A, B, count):
    return A / math.sqrt(1 + count) + B * count
