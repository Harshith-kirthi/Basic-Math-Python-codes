n = int(input("Enter a digit to reverse: "))
dup = n
revNum = 0
while (n > 0):
    ld = n % 10
    revNum =  (revNum * 10) + ld
    n = n // 10
if (revNum == dup) :
    print("The Number is Palindrome")
else:
    print("The number is not palindrome")