def check_prime(num):
    if num > 1:
        for i in range(2, int(num / 2)):
            if num % i == 0:
                print("Num is not prime")
                break
            else:
                print("Num is prime")
    else:
        print("Num is not prime")
   

check_prime(4)