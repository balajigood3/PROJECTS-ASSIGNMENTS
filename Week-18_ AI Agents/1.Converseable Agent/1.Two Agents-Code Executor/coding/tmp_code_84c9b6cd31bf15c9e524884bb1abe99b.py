word = 'ALGEbRA'
unique_chars = set(word)
char_counts = {char: word.count(char) for char in unique_chars}
count = 1
for count_char in char_counts.values():
    count *= factorial(count_char)
print(count)