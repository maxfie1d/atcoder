def solve(list):
    sorted_list = sorted(list)
    v1 = max(sorted_list)
    v2 = min(sorted_list)
    return v1 - v2


n = int(input())
arr = map(int, input().split())

print(solve(arr))
