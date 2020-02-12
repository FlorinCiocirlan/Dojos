n = 78
count = 0
string_nr = str(n)
prod = 1
for nr in string_nr:
    print(nr)
    if len(string_nr) > 1:
        prod *= int(nr)
        count += 1
        if string_nr[-1] == nr:
            string_nr = str(prod)
            print(string_nr)
            prod = 1
    else:
       print(count)
