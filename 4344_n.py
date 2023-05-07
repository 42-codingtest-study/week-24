k = int(input())

for _ in range (k):
    arr = list(map(int, input().split()))
    n = arr[0]
    del arr[0]
    good = 0
    avg = sum(arr) / n
    for grade in arr:
        if grade > avg:
            good += 1
    # print(f"{ans:.3f}%")
    print('{:.3f}%'.format(good / n * 100))