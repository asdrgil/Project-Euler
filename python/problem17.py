digit = [["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"], ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"], ["hundred"], ["thousand"]]


def p17():
    ans = sum(len(word_number(i)) for i in range(1, 1001))
    return str(ans)
	
def	word_number(n):
    if 0 <= n <= 19:
        return digit[0][n]
    elif 20 <= n <= 99:
        return digit[1][n//10] + (digit[0][n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return digit[0][n // 100] + digit[2][0] + (("and" + word_number(n % 100)) if (n % 100 != 0) else "")
    elif n == 1000:
        return digit[0][1] + digit[3][0]
    
def main():
    print(p17())

if __name__ == '__main__':
    main()
