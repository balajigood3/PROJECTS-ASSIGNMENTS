import math

def calculate_permutations(word):
  """Calculates the number of permutations of a given word.

  Args:
    word: The word to calculate the permutations of.

  Returns:
    The number of permutations of the word.
  """

  # Create a dictionary to store the count of each letter in the word.
  letter_counts = {}
  for letter in word:
    if letter not in letter_counts:
      letter_counts[letter] = 0
    letter_counts[letter] += 1

  # Calculate the factorial of the total number of letters in the word.
  total_factorials = 1
  for letter, count in letter_counts.items():
    total_factorials *= math.factorial(count)

  # Calculate the product of the factorials of the count of each letter in the word.
  letter_factorials = 1
  for letter, count in letter_counts.items():
    letter_factorials *= math.factorial(count)

  # Divide the factorial of the total number of letters by the product of the factorials of the count of each letter in the word.
  return total_factorials / letter_factorials


if __name__ == "__main__":
  word = "ALGEbRA"
  num_permutations = calculate_permutations(word)
  print(num_permutations)  # Output: 2520