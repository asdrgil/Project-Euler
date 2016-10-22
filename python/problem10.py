
def p10():
    total = 3
    primes = [2]
    for i in range(3, 2000000, 2):
        if(i%20001 == 0):
            print(i)
        for j in range(len(primes)):
            if(i%primes[j] == 0):
                break
        if(j == len(primes) - 1):
            primes.append(i)
            total += i
                
    return total

def main():
    print(p10())

if __name__ == '__main__':
    main()
