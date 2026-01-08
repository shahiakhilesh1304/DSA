
import math

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (1/math.sqrt(5)) * ((((1 + math.sqrt(5)) / 2) ** n) - (((1 - math.sqrt(5)) / 2) ** n))
    
    
if __name__ == "__main__":
    n = input("Input the number for which you want the fibonacci number")
    n = float(n)
    print(round(fibonacci(n)))