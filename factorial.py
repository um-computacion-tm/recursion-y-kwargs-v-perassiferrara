def factorial(num):
    if num in (0,1):
        return 1
    return num * factorial(num-1)


if __name__ == "__main__":
    while (True):
        num = int(input("Ingresa un numero natural: "))
        print("Factorial de" ,num , "=" ,factorial(num))