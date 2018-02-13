def p20():
    
    it = 1
    fact = 1
    while it <= 100:
        fact *= it
        it += 1
    
    sumDigits = 0
    while fact:
        sumDigits += fact % 10
        fact //= 10

    return(str(sumDigits))
def main():
    print(p20())

if __name__ == '__main__':
    main()
