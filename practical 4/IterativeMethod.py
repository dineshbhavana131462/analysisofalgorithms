# Factorial using Iterative Method

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial of", n, "=", fact)

# Factorial using Recursive Method

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter a number: "))

print("Factorial of", n, "=", factorial(n))
