S = input()

count = 0
while S != "":
    if len(S) >= 2:
        tail = S[-2:]
        if tail == "00":
            S = S[0:-2]
        else:
            S = S[0:-1]
    elif len(S) == 1:
        S = ""
    count += 1

print(count)

