import sys


def say_hello(x):
    arguments=len(sys.argv)-1
    if arguments >= 1 :
        index=1
        while (index<=arguments):
            print("Hello" , x[index] , "!")
            index+=1

    else:
        print("Hello world!")
        
say_hello(sys.argv)


