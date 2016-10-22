def p11():
    inputFile = open("../input/input_problem11", "r")
    arr = []
    
    for line in inputFile:
        arr.append(line.replace('\n','').split(" "))


    maxTotal = current = 0
    
    
    #Horizontal
    for i in range(len(arr)):
        for j in range(len(arr[0]) - 3):
            current = int(arr[i][j]) * int(arr[i][j+1]) * int(arr[i][j+2]) * int(arr[i][j+3])
            if(current > maxTotal):
                maxTotal = current
                a = "h"
    
    #Vertical
    for i in range(len(arr) - 3):
        for j in range(len(arr[0])):
            current = int(arr[i][j]) * int(arr[i+1][j]) * int(arr[i+2][j]) * int(arr[i+3][j])
            if(current > maxTotal):
                maxTotal = current
                a = "v"
                
    #Diagonal1
    for i in range(len(arr) - 3):
        for j in range(len(arr[0]) - 3):
            print(arr[i][j] + " " + arr[i+1][j+1] + " " + arr[i+2][j+2] + " " + arr[i+3][j+3])
            current = int(arr[i][j]) * int(arr[i+1][j+1]) * int(arr[i+2][j+2]) * int(arr[i+3][j+3])
            print(current)
            if(current > maxTotal):
                a = "d1"
                maxTotal = current

    #Diagonal1
    for i in range(1, len(arr) - 3, 1):
        for j in range(len(arr[0]) - 3):
            current = int(arr[i][j]) * int(arr[i+1][j-1]) * int(arr[i+2][j-2]) * int(arr[i+3][j-3])
            if(current > maxTotal):
                a = "d2"
                maxTotal = current


    print(a)
    print(maxTotal)
    
    

def main():
    p11()

if __name__ == '__main__':
    main()
