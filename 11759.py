import sys

s, v1, v2 = map(int, sys.stdin.readline().rstrip().split(" "))
temp = []
for x in range((s // v1) + 1):
    y = (s - (v1 * x)) // v2
    if s == v1 * x + v2 * y:
        temp += [(x, y)]

if not temp:
    print("Impossible")
else:
    temp = tuple(temp)
    print(" ".join([str(i) for i in min(temp, key=lambda x: x[0] + x[1])]))
