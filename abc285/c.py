S = input()

r = 0

while len(S) > 0:
    S, head = S[1:], S[0:1]
    v = ord(head) - ord("A") + 1
    r = r * 26 + v

print(r)