from eulerlib import Divisors

def p12():
    it1 = 1
    triangularValue = 0
    while True:
        triangularValue += it1
        mydiv = Divisors(triangularValue)
        divisors = mydiv.divisors(triangularValue)
        #print "%i: %i" % (it1, len(divisors))
        if len(divisors)> 500:
            return(str(triangularValue))
        it1 += 1


def main():
    print(p12())

if __name__ == '__main__':
    main()
