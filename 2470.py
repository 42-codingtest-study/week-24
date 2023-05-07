N = int(input())
lst = [*map(int, input().split())]
lst.sort()
closed = 999999999999
s, e = 0, len(lst) - 1
start, end = 0, len(lst) - 1
while start < end:
    if abs(closed) > abs(lst[start] + lst[end]):
        closed = lst[start] + lst[end]
        s, e = start, end
    if lst[start] + lst[end] < 0:
        start += 1
    else:
        end -= 1
print(lst[s], lst[e])
