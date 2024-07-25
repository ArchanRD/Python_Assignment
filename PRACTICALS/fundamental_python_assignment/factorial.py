def factorial(num):
    fact=0
    if num == 0 or num == 1:
        return 1
    else:
        fact = num * factorial(num-1)
    return fact

print(factorial(3))