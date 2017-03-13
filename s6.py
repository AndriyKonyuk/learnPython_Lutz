def fib(n):
    if n > 3:
        return fib(n-1)+fib(n-2)
    elif n==2 or n==3:
        return 1
    elif n==1:
        return 0

print(fib(10))
