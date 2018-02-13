def p13():
    inputFile = open('../input/problem13', 'r')
    totalSum = 0
    for line in inputFile:
        totalSum += int(line)
    return(str(totalSum)[:10])
def main():
    print(p13())

if __name__ == '__main__':
    main()
