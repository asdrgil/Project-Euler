def p6():
    top = 100
    sum = [0, 0]

    for i in range(1, top+1):
        sum[0] += i**2;
        sum[1] += i;
        
    sum[1] = sum[1]**2;
    return(sum[1] - sum[0])
    

def main():
    print(p6())

if __name__ == '__main__':
    main()
