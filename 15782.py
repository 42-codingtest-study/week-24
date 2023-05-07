# 헬멧과 조끼

n, k = map(int, input().split())
h =list(map(int, input().split()))
j =list(map(int, input().split()))
h.sort()
j.sort()
print(int(h[n - 1]) + int(j[k - 1]))