n = int(input("Enter a digit to reverse: "))
revNum = 0
while n > 0:
    ld = n % 10
    revNum =  (revNum * 10) + ld
    n = n // 10
print(revNum)