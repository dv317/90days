def fib(n):
    if n == 0:
        return 0
    if n == 2 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)


a = int(input())
b = fib(a)
print(b)