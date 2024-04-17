def fibonacci(num):
    if num in (0,1):
        return num
    return fibonacci(num-1) + fibonacci(num-2)


if __name__ == "__main__":
    while (True):
        num = int(input("Ingresa un numero natural: "))
        print("Fibonacci de" ,num , "=" ,fibonacci(num))