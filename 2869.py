from math import ceil
A, B, V = map(int, input().split())
last = (V-A) / (A-B)
print(ceil(last) + 1)
