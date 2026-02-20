import math
from collections import Counter

def permutations(word):
    counts = Counter(word)
    total = math.factorial(len(word))
    
    for count in counts.values():
        total //= math.factorial(count)
        
    return total

word = 'ALGEbRA'

print(permutations(word))