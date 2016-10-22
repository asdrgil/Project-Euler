from problem3 import isPrime

def p5():
    top = 20
    factor = 1
    for i in range(2, top+1, 1):
        if(isPrime(i)):
            exponent = 1
            while(i**(exponent+1) <= top):
                exponent += 1
            
            factor *=  i**exponent
    return(factor)
    
    
    
def main():
    print(p5())

if __name__ == '__main__':
    main()
