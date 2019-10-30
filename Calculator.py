while True:
    number1=int(input("Enter a number: "))
    sign=input("Enter a sign: ")
    number2=int(input("Enter the second number: "))
    if sign == "+" :
        print("The result of" ,number1, sign, number2, "is", number1+number2)
    elif sign == "-":
        print("The result of" ,number1, sign, number2, "is", number1-number2)
    elif sign == "*":
        print("The result of" ,number1, sign, number2, "is", number1*number2)
