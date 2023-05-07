a, b = map(int, input().split())
c, d = map(int, input().split())
p = int(input()) - abs(a - c) - abs(b - d)
print("YN"[p < 0 or p % 2])
