from math import *

def p9():
    number = 1000

    for i in range(1, number):
        for j in range(1, number):
            for k in range(number, 1, -1):
                if(i+j+k==number and i**2 + j**2 == k**2 and i<j<k):
                    return([i, j, k])
        print(i)

def main():
    print(p9())

if __name__ == '__main__':
    main()
