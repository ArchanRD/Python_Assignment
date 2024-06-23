def sum_using_recursion(n):
    if n == 0 or n == 1:
        return n
    else:
        if n > 0:
            return n + sum_using_recursion(n-1)
print(sum_using_recursion(5))
