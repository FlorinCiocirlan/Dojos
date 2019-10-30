x = [-5, 23, 0, -9, 12, 99, 105, -43]
max = x[0]
min = x[0]
i =  1
sum = x[0]
while i<len(x):
    if x[i] > max:
        max=x[i]
    elif x[i] < min:
        min=x[i]
    sum = sum+x[i]
    i += 1
print(max, min , "Suma este", sum)
print("Media este", sum/len(x))





    

