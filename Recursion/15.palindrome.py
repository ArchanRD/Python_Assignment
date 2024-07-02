def palindrome(string):
    if len(string) == 1:
        print("Palindrome")
    else:
        if string[::-1] == string:
            print("Palindrome")
        else:
            print("Not palindrome")

palindrome("level")
palindrome("archan")