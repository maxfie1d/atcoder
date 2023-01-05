def solve(s, t):
    ss = "".join(sorted(list(s), reverse=False))
    tt = "".join(sorted(list(t), reverse=True))

    return "Yes" if ss < tt else "No"


s = input()
t = input()
print(solve(s, t))
