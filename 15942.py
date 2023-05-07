import sys
input = sys.stdin.readline
sys.setrecursionlimit(999999)

def dfs(now, pre):
    global res
    count = 0
    for next_node in graph[now]:
        if next_node != pre:
            count = max(count,dfs(next_node, now))
    if count >= d:
        res += 1
    return count + 1

n, s, d = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
res = 0
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs(s,0)