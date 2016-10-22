from problem3 import isPrime

def getPrime(position):
    numPrime = 0
    i = 1
    while(numPrime < position):
        i += 1
        if(isPrime(i)):
            numPrime +=1    
    return(i)

def p7():
    print(getPrime(10001))

def main():
    p7()

if __name__ == '__main__':
    main()
