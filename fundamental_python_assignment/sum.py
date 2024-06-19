def find_sum(num):
    sum=0
    while num != 0:
        sum += num
        num -= 1
    return sum

print(find_sum(5))