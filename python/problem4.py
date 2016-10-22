def p4():
    result = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            print("i: " + str(i) + ", j: " + str(j))
            current = i*j
            if(str(current) == str(current)[::-1] and current > mul):
                result = current
    return(result)
                
def main():
    print(p4())

if __name__ == '__main__':
    main()
