from eulerlib import Divisors

def p21():
    a = 1
    totalSum = 0
    mydiv = Divisors(10000)
    while a < 10000:
        
        divisors = mydiv.divisors(a)
        if(len(divisors) > 1):
            divisors = divisors[:-1]
        b = sum(divisors)
        
        divisors2 = mydiv.divisors(b)
        if(len(divisors2) > 1):
            divisors2 = divisors2[:-1]
        d2 = sum(divisors2)
        
        if (a < b and a == d2):
            print "a: %i, b: %i, d2: %i" % (a, b, d2)
            totalSum += (a + b)
        
        a += 1
                
    return(str(totalSum))

def main():
    print(p21())

if __name__ == '__main__':
    main()
