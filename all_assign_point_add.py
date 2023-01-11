# Difficulty: 559
import copy

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
qli = []
for i in range(Q):
    qli.append(list(map(int, input().split())))

last_pos = -1
last_value = copy.copy(A)
last_pos = [-1] * N
for q in range(Q):
    query = qli[q]
    if query[0] == 3:
        # クエリ1か、last_posか、先頭のところまで戻る
        start = None
        vv = 0
        for j in range(q - 1, last_pos[query[1] - 1], -1):
            backward_query = qli[j]
            if backward_query[0] == 1:
                start = backward_query[1]
                break
            if backward_query[0] == 2 and query[1] == backward_query[1]:
                vv += backward_query[2]
        if start == None:
            start = last_value[query[1] - 1]
        r = start + vv
        print(r)
        last_pos[query[1] - 1] = q
        last_value[query[1] - 1] = r
