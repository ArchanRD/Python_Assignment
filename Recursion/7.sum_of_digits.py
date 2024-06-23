def sum_of_digits(num: int):
    if num > 10:
        last_digit = num % 10
        return last_digit + sum_of_digits(num // 10)
    else:
        return num


print(sum_of_digits(12345))