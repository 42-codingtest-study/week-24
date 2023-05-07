# 두 용액

n = int(input())
num = list(map(int, input().split(' ')))
num.sort()

first = 0
last = n - 1
res = abs(num[first] + num[last])
r1 = [num[first], num[last]]

while first < last :
    r_last = num[last]
    r_first = num[first]
    sum = r_first + r_last
    if abs(sum) < res :
        res = abs(sum)
        r1 = [r_first, r_last]
    if sum < 0 :
        first += 1
    elif sum > 0 :
        last -= 1
    else :
        break
print(r1[0], r1[1])