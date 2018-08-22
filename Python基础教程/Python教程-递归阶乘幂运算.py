def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print factorial(5)

def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

print power(3, 4)

def poo(x, n):
    if n == 0:
        return 1
    else:
        return x * poo(x, n-1)
print poo(3, 3)

