t = int(input())

def fill_0_floor(ho):
    global home
    for i in range(ho):
        home[0][i] = i+1

def fill_floor(f, ho):
    global home
    for i in range(1, f + 1):
        for j in range(ho):
            home[i][j] = sum(home[i-1][:j+1])

for _ in range (t):
    f = int(input())
    ho = int(input())
    home = [[0 for _ in range(ho)] for _ in range(f + 1)]
    fill_0_floor(ho)
    fill_floor(f, ho)
    print(home[f][ho - 1])