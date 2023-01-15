S = input()
pins = []
li = list(map(int, list(S)))
# 左から列を埋める
retsu = [[], [], [], [], [], [], []]

tuples = [
    (7, 1),
    (4, 2),
    (8, 3),
    (8, 3),
    (5, 4),
    (1, 4),
    (9, 5),
    (3, 5),
    (6, 6),
    (10, 7)
]

for t in tuples:
    a, b = t
    v = li[a - 1] == 1
    retsu[b - 1].append(v)

if li[0] == 1:
    print("No")
else:
    # 条件2を満たすかどうか
    flag = False
    for s in range(6):
        for e in range(s + 1, 7):
            c1 = any(retsu[s])
            c2 = any(retsu[e])
            for l in range(s + 1, e):
                c3 = not any(retsu[l])
                if c1 and c2 and c3:
                    flag = True
    print("Yes" if flag else "No")
