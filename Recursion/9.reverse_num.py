def reverse_number(num, rv_num=0):
    if num != 0:
        ld = num % 10
        rv_num = rv_num * 10 + ld
        return reverse_number(num // 10, rv_num)
    else:
        return rv_num
print(reverse_number(num=1234))
