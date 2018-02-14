import sys

def p22():
    with open('../input/problem22', 'r') as f:
        read_data = f.read()
    
    nameList = sorted(read_data.replace('"','').split(','))
    total = 0
    it = 0
    while it < len(nameList):
        for i in nameList[it]:
            sys.stdout.write(i)
            sys.stdout.flush()
            total += (ord(i) - 64)*(it+1)
        it += 1
    return(str(total))

def main():
    print(p22())

if __name__ == '__main__':
    main()
