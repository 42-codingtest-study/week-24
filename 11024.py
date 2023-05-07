# 더하기 4

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    num = list(map(int, input().split()))
    print(sum(num))