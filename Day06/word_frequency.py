import string

sentence = input("Enter a sentence: ")

# Remove punctuation
sentence = sentence.translate(str.maketrans('', '', string.punctuation))

words = sentence.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\n----- Word Frequency -----")
for word, count in frequency.items():
    print(word, ":", count)