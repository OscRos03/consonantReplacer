import random

vowels = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
inputfile = open("input.txt","r")
words = list(inputfile.read().lower())
replaceConsonants = True
replaceVowels = False
consonantReplacement = "b" # consonants[random.randint(1, len(consonants))-1]
vowelReplacement = vowels[random.randint(1, len(vowels))-1]

for i in range(0, len(words)):
    if replaceConsonants:
        for x in range(0, len(consonants)):
            if words[i] == consonants[x]:
                words[i] = consonantReplacement
    
    if replaceVowels:
        for x in range(0, len(vowels)):
            if words[i] == vowels[x]:
                words[i] = vowelReplacement

outputfile = open("output.txt", "w")
outputfile.write(''.join(words))