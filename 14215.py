lst = [*map(int, input().split())]
lst.sort()
print(
    lst[0] + lst[1] + (lst[0] + lst[1] - 1 if lst[0] + lst[1] - 1 < lst[2] else lst[2])
)
