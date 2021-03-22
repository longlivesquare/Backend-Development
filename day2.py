vowels = ['a', 'e', 'i', 'o', 'u']

def pigLatin(word):
    for idx, letter in enumerate(word.lower()):
        if letter in vowels:
            return word[idx:] + word[:idx] + 'ay'
    return word

def pigLatinSentence(sentence):
    pigLatSentence = ''
    for word in sentence.split():
        pigLatSentence += pigLatin(word) + ' '
    return pigLatSentence

print(pigLatinSentence("Hello my name is Steven Duran"))