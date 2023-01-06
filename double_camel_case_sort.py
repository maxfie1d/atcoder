def solve(S):
    words = []
    i = 0
    # 次の大文字になる場所を見つける
    while i < len(S):
        j = i + 1

        while S[j].islower():
            j += 1

        words.append(S[i:j + 1])
        i = j + 1

    words.sort(key=str.lower)

    return "".join(words)


S = input()

print(solve(S))
