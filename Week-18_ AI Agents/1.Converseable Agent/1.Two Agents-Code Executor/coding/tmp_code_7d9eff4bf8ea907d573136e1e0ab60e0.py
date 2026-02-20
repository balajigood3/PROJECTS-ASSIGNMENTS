from collections import Counter
def permutation(word):
    """
    This function calculates the number of permutations of a given word.
    """
    word=word.upper()
    # Create a dictionary to store the count of each letter in the word.
    letter_count = Counter(word)

    # Take the product of the factorials of the counts of each letter.
    num_permutations = 1
    for count in letter_count.values():
        num_permutations *= factorial(count)

    # Return the number of permutations.
    return num_permutations

def factorial(n):
    """
    This function calculates the factorial of a given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

word = 'ALGEBRA'
num_permutations = permutation(word)
print(num_permutations)