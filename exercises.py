"""     print(sum(list)) """
""" numbers=[]
for a in range(101):
    print(a)
    numbers.append(a)
    b=numbers[a]+1
    print(b)
     print("The multiplication is" , a+b) """

""" list=range(11)
a=list[len(list)-1]
for i in list:
    a-=1
    print(a)

for a in range(0,10,2):


for c in range(1,10): """
""" list=[] 
for a in range(100,200)
    list.append(a)
    print(a) """

""" list1=["a","b",[0,1,2],"c","d"]
list2=list1[:]
list2[0]="z"
list2[2][0]=4
print(list1)
print(list2) """

""" from copy import deepcopy
list1=["a","b","c","d"]
list2=deepcopy(list1) """

""" try:
    def the_number_is(number):
        print("Data ta de nastere este " ,number)
    while True:
        user_input =(input("Data de nastere: "))
        if int(user_input) in range(1000):
            the_number_is(user_input)
except ValueError:
    print(user_input , " nu este un numar") """
""" def max(x,y):
    if x >= y:
        return x
    else:
        return y
print(max(4,5))
z=max(8,3)
print(z) """

""" def addition(x,y):
    return x+y
a=1
b=2
operation=addition
print(operation(a,b)) 

def multiply(a,b):
    return a*b

def multiply_twice(func,a,b):
    return func(func(a,b),func(a,b))
x=1
y=2

print(multiply_twice(multiply,x,y)) 


import random
for a in range(3):
    value=random.randint(1,10)
    print(value) 