x, y = map(int, input().split())
temp = []
for _ in range(int(input())):
    t_x, t_y = map(int, input().split())
    temp += [[t_x, t_y, abs(x - t_x) + abs(y - t_y)]]

min_d = min(temp, key=lambda x: x[2])
print(min_d[0], min_d[1])
