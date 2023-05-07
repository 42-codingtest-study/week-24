import sys

temp = {
    "1": "Yakk",
    "2": "Doh",
    "3": "Seh",
    "4": "Ghar",
    "5": "Bang",
    "6": "Sheesh",
    "11": "Habb Yakk",
    "22": "Dobara",
    "33": "Dousa",
    "44": "Dorgy",
    "55": "Dabash",
    "66": "Dosh",
}

n = int(sys.stdin.readline().rstrip())
input_list = [
    sorted([int(j) for j in sys.stdin.readline().rstrip().split(" ")], reverse=True)
    for _ in range(n)
]

for k, i in enumerate(input_list):
    temp3 = "Case {}: ".format(k + 1)
    a = "".join([str(j) for j in i])
    if len(set(i)) == 1:
        print(temp3 + temp[a])
    else:
        if a == "65":
            temp2 = "Sheesh Beesh"
            print(temp3 + temp2)
        else:
            temp2 = []
            for j in a:
                temp2 += [temp[j]]
            print(temp3 + " ".join(temp2))
