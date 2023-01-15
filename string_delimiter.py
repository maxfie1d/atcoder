N = int(input())
S = input()

flag = False

li = list(S)
ans = [""] * len(S)
for i in range(len(li)):
    v = li[i]
    if v == '"':
        flag = not flag

    if v == ",":
        ans[i] = "," if flag else "."
    else:
        ans[i] = v

print("".join(ans))
