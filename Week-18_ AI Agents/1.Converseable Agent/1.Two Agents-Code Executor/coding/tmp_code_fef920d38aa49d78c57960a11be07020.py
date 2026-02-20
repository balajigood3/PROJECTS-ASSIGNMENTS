import math
from collections import Counter

word = 'ALGEBRA'
letter_counts = Counter(word)

# Compute the factorials
numerator = math.factorial(len(word))
denominator = math.prod(math.factorial(count) for count in letter_counts.values())

# Compute the number of permutations
num_permutations = numerator // denominator

print(num_permutations)