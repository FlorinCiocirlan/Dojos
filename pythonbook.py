
def factorial(n):
    if n<0:
        raise ValueError ("Enter a positive number")
    else:
        n*factorial(n-1)

print(factorial(5))