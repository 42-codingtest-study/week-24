try:
    while True:
        N = int(input())
        lst = ["-" * (3**N)]
        while lst[0] != "-":
            tmp = []
            for i in lst:
                if "-" in i:
                    tmp.append("-" * (len(i) // 3))
                    tmp.append(" " * (len(i) // 3))
                    tmp.append("-" * (len(i) // 3))
                else:
                    tmp.append(i)
            lst = tmp
        print("".join(lst))
except:
    exit(0)
