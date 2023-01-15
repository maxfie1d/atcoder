# https://atcoder.jp/contests/abc275/tasks/abc275_c
# 9x9のマスである
# 可能なマスの一辺は 1~9
# sqrt(4)

matrix = []


def solve(matrix):
    x, y = (0, 0)
    for dx in range(9):
        for dy in range(9 - dx):
            a = (x, y)
            b =

def view():
    for i in range(9):
        for j in range(9):
            print([matrix[50 + i][50 + j]], end="")
        print()


for i in range(100):
    matrix.append(["."] * 100)

for i in range(9):
    li = list(input())
    for j in range(9):
        matrix[50 + i][50 + j] = li[j]

view()
