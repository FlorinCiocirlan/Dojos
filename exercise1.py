""" try:
    print("Hello !")
    user_input=float(input("How many degrees are in your city right now ? : "))
    print("Okay so there are " , user_input , "Fahrenheit degrees")
    print("So if you would have been in Europe") 
    celsius=(5/9) * (user_input - 32)
    print("There would have been like" ,float(celsius), "Celsius Degrees right now")
except ValueError as e:
    print("The value of Farenheit Degrees can't be literals") """
""" 
print(float("8.7"))
print(int(8.7))
print(int(float(8.6))) """
print(str(8.6))
print(bool(8))