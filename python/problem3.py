def isPrime(number):
    if(number == 2 or number == 3):
        return 1;

    if(number%2==0):
        return 0;    
    
    for i in range(3, number, 2):
        if(number%i == 0):
            return 0;
    return 1;

def p3():
    n = 600851475143
    factor = 3
    greatestDivisor = 1
    
    while (factor <= n):
        if(n%factor != 0):
            if(factor%1000000 == 0):
                print(factor)
            factor += 2
        else:
            n /= factor
            if(isPrime(factor) and factor > greatestDivisor):
                greatestDivisor = factor

    return(greatestDivisor)

def main():
    print(p3())

if __name__ == '__main__':
    main()
