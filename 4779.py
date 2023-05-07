while True :
    try:
        n = int(input())
        a = 3 ** n
        result = [' ' for _ in range (a)]
        pick = []
        pick.append(0)
        for i in range (1, n+1):
            new = []
            for j in range(len(pick)) :
                new.append(pick[j] + (3**(i-1) * 2))
            pick += new
        for p in pick:
            result[p] = '-'
        print(''.join(result))
    except EOFError: #'except:' 도 가능
        break