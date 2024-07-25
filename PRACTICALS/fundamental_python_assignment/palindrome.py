def check_palindrome(string):
    reversed_string = ""

    for i in reversed(string):
        reversed_string += i

    if string == reversed_string:
        print(string, "is palindrome")
    else:
        print(string, "is not palindrome")

check_palindrome("level")