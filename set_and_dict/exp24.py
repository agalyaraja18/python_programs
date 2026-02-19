import string
from collections import Counter
paragraph = "This is a simple example. This example is meant to be a simple test of the function."
cleaned_paragraph = paragraph.lower().translate(str.maketrans('', '', string.punctuation))
words = cleaned_paragraph.split()
word_counts = Counter(words)
sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
sorted_dict = dict(sorted_word_counts)
print(sorted_dict)

