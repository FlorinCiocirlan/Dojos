user_input = input("Enter a number :  ").split(" ")

list_of_binary = []
number_to_convert = int(user_input[0])
print("You want to convert %d into base 10" % (number_to_convert))
if user_input[1] == "10":
    while number_to_convert != 0:
        list_of_binary.append(number_to_convert % 2)
        number_to_convert = number_to_convert // 2
    new_string = "".join(str(a) for a in list_of_binary[::-1])
    print("Your converted number is %s  2" % new_string)
