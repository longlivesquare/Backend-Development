# List to hold all the vowels.
VOWELS = ('a', 'e', 'i', 'o', 'u')

# Function pig latinfies a word. Takes a word as a string as input
# and returns the word with the rules of pig latin applied to it
def pigLatin(word):
    for idx, letter in enumerate(word.lower()):
        if letter in VOWELS:
            return word[idx:] + word[:idx] + 'ay'
    return word

# Function applies rules of pig latin to a sentence. Splits sentence at the space and
# callse pigLatin on each section. Returns new sentence string
def pigLatinSentence(sentence):
    pigLatSentence = ''
    for word in sentence.split():
        pigLatSentence += pigLatin(word) + ' '
    return pigLatSentence

print(pigLatinSentence("Hello my name is Steven Duran"))