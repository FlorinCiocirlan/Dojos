def find_multiples(integer, limit):
    list1= [ ]
    for i in range(integer,limit+1):
        if limit % i == 0:
            list1.append(i)
    return list1


print(find_multiples(3,26))