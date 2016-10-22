def p1():
    return(sum(x for x in range(1000) if x%3==0 or x%5==0))

def main():
    p1()

if __name__ == '__main__':
    main()
