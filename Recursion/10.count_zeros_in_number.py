def count_zeros(num, count=0):
    if num == 0 and count == 0:
        return 1
    elif num == 0:
        return count
    else:
        ld = num % 10
        if ld == 0:
            count += 1
        return count_zeros(num//10, count)


print(count_zeros(1050))