import sys
input = sys.stdin.readline

n = int(input())
grade = list(map(int, input().split()))

print(((sum(grade) / max(grade)) * 100) / n)