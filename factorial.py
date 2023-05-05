try:
    number = int(input("Input number to make the factorial: "))
    res = 1
    for i in range(number):
        res *= i+1
    print("El factorial de {0} es {1}".format(number, res))
except:
    print("Something went wrong")