def simple_recursion(n):
    if n == 1:
        return 1
    else:
        return n + simple_recursion(n - 1)


print(simple_recursion(5))


# Fibonacci number
def fibonacci(n):
    if n <= 1:
        return (n)
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


print(fibonacci(5))
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(4))
