def fibbonnacci(n):
    nums = [0,1]
    if n == 0 or n == 1:
        return nums
    else:
        for i in range(1, n):
            sum = nums[-1] + nums[-2]
            nums.append(sum)
            print(sum)
            
            
fibbonnacci(10)