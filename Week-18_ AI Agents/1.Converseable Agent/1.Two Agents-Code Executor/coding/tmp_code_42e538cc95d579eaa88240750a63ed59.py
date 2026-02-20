def count_permutations(word):
    """Counts the number of permutations of a given word.

    Args:
        word (str): The word to count the permutations of.

    Returns:
        int: The number of permutations of the word.
    """

    # Create a dictionary to store the count of each letter in the word.
    letter_counts = {}
    for letter in word:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1

    # Calculate the factorial of the total number of letters in the word.
    total_factorials = 1
    for count in letter_counts.values():
        total_factorials *= count

    # Calculate the factorial of the count of each letter in the word.
    letter_factorials = 1
    for count in letter_counts.values():
        letter_factorials *= math.factorial(count)

    # Calculate the number of permutations.
    permutations = total_factorials // letter_factorials

    return permutations


# Get the word from the user.
word = input("Enter a word: ")

# Count the number of permutations.
permutations = count_permutations(word)

# Print the number of permutations.
print("The number of permutations of", word, "is", permutations)