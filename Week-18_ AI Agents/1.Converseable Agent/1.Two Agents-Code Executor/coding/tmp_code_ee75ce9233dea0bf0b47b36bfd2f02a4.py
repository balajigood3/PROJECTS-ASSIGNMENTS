num_permutations = factorial(len(word))
for letter_count in letter_counts.values():
    num_permutations //= factorial(letter_count)