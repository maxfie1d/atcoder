import itertools

N = int(input())


def keta(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 2
    return count


# 何ビット目が1か記録する
A = []
for i in range(60):
    v = (1 << i)
    if v & N > 0:
        A.append(i)

results = []
for bits in itertools.product(range(2), repeat=len(A)):
    a = list(bits)
    r = 0
    for i in range(len(a)):
        bit = a[i]
        if bit == 1:
            r += 1 << A[i]
    results.append(r)

for v in sorted(results):
    print(v)
