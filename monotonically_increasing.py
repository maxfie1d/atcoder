N, M = map(int, input().split())

stack = []


def solve(start, end, rest_keta):
    global stack

    for v in range(start, end + 1):
        stack.append(v)
        if rest_keta == 0:
            print(" ".join(map(str, stack)))
        else:
            solve(v + 1, M - (rest_keta - 1), rest_keta - 1)
        stack.pop()


solve(1, M - N + 1, rest_keta=N - 1)
