def fibonacci(n):
    if n <= 1:
        return n
    else:
        a = fibonacci(n - 1) + fibonacci(n - 2)
        return a


print(fibonacci(30))
