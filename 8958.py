n = int(input())

for _ in range (n):
    arr = list(map(str, input()))
    grade = 0
    cnt = 0
    for i in range (0, len(arr)) :
        if arr[i] == 'O':
            cnt += 1
            grade += cnt
        else :
            cnt = 0
    print(grade)
