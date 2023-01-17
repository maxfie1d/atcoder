a, b = map(int, input().split())

r = b == 2 * a or b == 2 * a + 1
print("Yes" if r else "No")
