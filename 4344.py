k = int(input())

for _ in range (k):
    arr = list(map(int, input().split()))
    n = arr[0]
    del arr[0]
    good = 0
    avg = sum(arr) / n
    for i in range(n):
        if arr[i] > avg:
            good += 1
    print(round(good / n * 100, 3), '%', sep='')