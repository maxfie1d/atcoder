H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(input()))
Q = int(input())
qli = []
for i in range(Q):
    qli.append(tuple(map(int, input().split())))


def flip_h(A, i, j, w, h):
    for dj in range(w // 2):
        for di in range(h):
            temp = A[i + di][j + dj]
            A[i + di][j + dj] = A[i + di][j + w - 1 - dj]
            A[i + di][j + w - 1 - dj] = temp


def flip_v(A, i, j, w, h):
    for di in range(h // 2):
        for dj in range(w):
            temp = A[i + di][j + dj]
            A[i + di][j + dj] = A[i + h - 1 - di][j + dj]
            A[i + h - 1 - di][j + dj] = temp


def rotate180(A, i, j, w, h):
    flip_v(A, i, j, w, h)
    flip_h(A, i, j, w, h)


def compute(A, a, b, W, H):
    rotate180(A, 0, 0, b, a)
    rotate180(A, 0, b, W - b, a)
    rotate180(A, a, 0, b, H - a)
    rotate180(A, a, b, W - b, H - a)


for query in qli:
    a, b = query
    compute(A, a, b, W, H)

for i in range(H):
    print("".join(A[i]))
