def p14():
    a = lambda x: x/2
    b = lambda x: 3*x+1
    
    maxSteps = 0
    for i in range(2, 1000000, 1):
        steps = 1
        num = i
        while(num != 1):
            if(num%2 == 0):
                num = a(num)
            else:
                num = b(num)
            steps += 1
        if(steps > maxSteps):
            maxSteps = steps
            maxNum = i
        if(i%100000==0):
            print(i)
    return(maxNum)
def main():
    print(p14())

if __name__ == '__main__':
    main()
