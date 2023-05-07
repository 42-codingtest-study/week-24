# N * M 크기의 얼음 틀이 있고
# 구멍은 0, 칸막이는 1
# 몇 덩이 아이스크림 만들어지는지

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y) :
    if x < 0 or x >= N or y < 0  or y >= M:
        return False
    if graph[x][y] == 0 :
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

ice = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            ice += 1
            
print(ice)