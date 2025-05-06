def isArmstrong(num):
    k = len(str(num))
    sum = 0
    n = num
    while n > 0:
        ld = n % 10
        sum += ld ** k
        n = n // 10
    return sum == num

def main():
    number = int(input("Enter a number: "))
    if isArmstrong(number):
        print(number, "is Armstrong number")
    else:
        print(number,"is not Armstrong number")

if __name__ == "__main__":
    main()