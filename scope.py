def solve(S):
    stack = []
    bag = set()
    for i in range(len(S)):
        c = S[i]
        if c == "(":
            stack.append(i)
        if c.islower():
            if c in bag:
                return "No"
            else:
                bag.add(c)
        if c == ")":
            j = stack.pop()
            for n in range(i - 1, j, -1):
                cc = S[n]
                if cc == ')':
                    break
                if cc in bag:
                    bag.remove(cc)
    return "Yes"


S = input()

print(solve(S))
