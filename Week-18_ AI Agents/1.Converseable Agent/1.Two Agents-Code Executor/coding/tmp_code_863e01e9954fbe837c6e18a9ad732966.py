def factorial(n):
    return n if n < 2 else n * factorial(n - 1)

def permute(word):
    return factorial(len(word))

print(permute("ALGEBRA"))