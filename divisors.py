def divisors(num):
    n = num
    sum = []
    for i in range(1, n+1):
        if n % i == 0:
            sum.append(i)
    return sum

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    divisor = divisors(number)
    print("divisors of", number , "is: ",divisor)