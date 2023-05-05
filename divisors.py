# return all divisors of all numbers from a given range
try:
    minNum = int(input("Input the start of the range: "))
    maxNum = int(input("Input the end of the range: "))

    if minNum>maxNum:
        minNum,maxNum = maxNum,minNum

    for number in range(minNum, maxNum+1):
        divisors = []
        for divisor in range(1, number+1):
            if number % divisor == 0:
                divisors.append(divisor)
        print(number, " -> ", divisors)

except ValueError:
    print("You didn't write a number...")