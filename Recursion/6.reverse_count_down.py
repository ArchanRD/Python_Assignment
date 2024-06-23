def count_down(n):
    if n > 0:
        count_down(n-1)
        print(n)


count_down(5)