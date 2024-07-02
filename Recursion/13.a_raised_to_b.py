def find_power(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * find_power(a, b-1)

print(find_power(2, 4))