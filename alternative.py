sentence = "Hello World"

new_sentence = ""
upper_lower_sentence = ""

""" 
for loop to iterate through the range of the sentence 
changing every even character to uppercase and odd to lowercase

"""
for i in range (len(sentence)):
    if i % 2 == 0:
        new_sentence += sentence[i].upper()
    else:
        new_sentence += sentence[i].lower()

print(new_sentence)

# Splits the sentence to be able to access each element separately
alt_words = sentence.split(" ")

""" 
for loop to iterate through each word in the sentence and 
print each even word as lower case and each even as uppercase
"""
for i, word in enumerate(alt_words):
    if i % 2 == 0:
        alt_words[i] = word.lower()
    else:
        alt_words[i] = word.upper()

# joins each element together to create 1 string
alt_words_new = " ".join(alt_words)

print(alt_words_new)