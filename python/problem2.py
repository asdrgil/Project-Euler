def p2():
    first = 1
    second = 2
    total = second
    currentFib = 0
    
    while(currentFib < 4000000):
        currentFib = first + second
        first = second
        second = currentFib
        if(currentFib % 2 == 0):
            total += currentFib
    
    return(total)

def main():
    print(p2())

if __name__ == '__main__':
    main()
