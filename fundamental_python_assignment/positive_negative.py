def check_positive(num):
    if num == 0:
        return "Zero"
    elif num > 0:
        return "Positive"
    else:
        return "Negative"
    
print(check_positive(0))
print(check_positive(-2))
print(check_positive(2))