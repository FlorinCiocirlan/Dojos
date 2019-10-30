user_input = input("Enter a number :  ").split(" ")
print(user_input)

list_of_binary = []
number_to_convert = int(user_input[0])
print("You want to convert",user_input[0],  "into base",user_input[1])
if user_input[1] == "10":
    while number_to_convert != 0:
        list_of_binary.append(number_to_convert % 2)
        number_to_convert = number_to_convert // 2
    new_string = "".join(str(a) for a in list_of_binary[::-1])
    print("Your converted number is %s  2" % new_string)
elif user_input[1] == "2":
    c=str(user_input[0])
    j = 1
    n = 0
    while j <= len(c):
        for i in c:
            n = n + int(i) * (2 ** (len(c) - j))
            j+=1
    print(n,10)