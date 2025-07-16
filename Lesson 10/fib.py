# Fibonacci
# 0, 1, 1, 3, 5, 8, 13, 21...

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print('testing fib function')
print(fib(6))
#fib(0)
#print(fib(1))