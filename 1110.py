cnt = 0

a = int(input())
num = [0] * 2
num[0] = a // 10
num[1] = a % 10
b = 10 * num[0] + num[1]

while cnt == 0 or a != b :
    temp = num[0]
    num[0] = num[1]
    num[1] = (temp + num[1]) % 10
    cnt += 1
    b = 10 * num[0] + num[1]

print(cnt)