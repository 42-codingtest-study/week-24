#23278 영화 평가

N, L, H = map(int, input().split())
scores= sorted(list(map(int, input().split())))
res = sum(scores[1:N - H])/(N - 1 - H)

print(res)