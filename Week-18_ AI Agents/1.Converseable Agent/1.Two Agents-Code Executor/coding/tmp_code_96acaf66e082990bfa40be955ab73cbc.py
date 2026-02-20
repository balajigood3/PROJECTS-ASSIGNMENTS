try:
    # Get the word from the user.
    word = input("Enter a word: ")

    # Count the number of permutations.
    permutations = count_permutations(word)

    # Print the number of permutations.
    print("The number of permutations of", word, "is", permutations)
except EOFError:
    print("Please provide a word when prompted.")