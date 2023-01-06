def solve(N, li):
    bag = set()
    for v in li:
        bag.add(v)
    return len(bag)


N = int(input())
li = []
for i in range(N):
    li.append(input())

print(solve(N, li))
