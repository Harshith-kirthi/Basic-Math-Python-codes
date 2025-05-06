def checkPrime(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt = cnt + 1
    if cnt == 2:
        return True
    else:
        return False

def main():
    n = int(input("Enter a number: "))
    isPrime = checkPrime(n)
    if isPrime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")

if __name__ == "__main__":
    main()

                                
                            