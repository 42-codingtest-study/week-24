# 세 막대

stick = sorted(list(map(int, input().split())))
if stick[0] + stick[1] > stick[2]:
    print(sum(stick))
else:
    print((stick[0] + sitck[1]) * 2 - 1)