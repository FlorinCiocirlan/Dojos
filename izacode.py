import random
list2 = ["A", "B", "C", "D", "E", 'F', "G", "H", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "Y", "Z"]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = ["@","#","%","*"]
codes=[]
for a in range(1, 51):
    word = "IVRE" + list2[random.randint(0, len(list2) - 1)].lower() + c[random.randint(0, len(c) - 1)] + str(b[random.randint(0, len(b) - 1)]) + list2[random.randint(0, len(list2) - 1)] + "10%OFF"
    if word not in codes:
        codes.append(word)

for a in range(len(codes)):
    print(a+1 ,codes[a] )

    