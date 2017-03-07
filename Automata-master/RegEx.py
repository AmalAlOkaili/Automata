import re

def find_consonant(word): #Checks TWO consecutive consonants
    for match in re.findall(r"\w+[^ouieaOUIEA]{2}\b", word):
          print (match)


def find_vowel(word):  #Checks FIRST and LAST chars
        for match in re.findall("\w{5,}", word):
            if re.findall(r"(^[ouieaOUIEA].+[ouieaOUIEA]$)", match):
                 print (match)


def find_consonant_vowel(word):    #Checks FIRST and LAST chars {consonant , vowel}
     for match in re.findall("\w{7,}", word):
         if re.findall(r"(^[^ouieaOUIEA].+[ouieaOUIEA]$)", match):
          print (match)


def find_after_vowel(word): #Checks letter after VOWELS
    for match in re.findall(r"[ouieaOUIEA](\w+)", word):
          print (match)



def eXtract(word): #Abbreviates 2-3 words in a sentence
    match = re.sub(r"([A-Z][a-z]+(?=\s[A-Z])(?:\s[A-Z][a-z]+){1,2})", replacement, word)
    print(match)


def replacement(m):
    return ''.join(y[0] for y in m.group(0).split())

def Camel(word): #Camel
    match = re.sub(r"(\w)([A-Z])", r"\1 \2", word)
    print(match)
    # for match in re.findall(r"([A-Z][a-z]+(?=[A-Z])(?:[A-Z][a-z]+)+)", word):
    #     print(match)


DATA = []
input_DATA = input("Enter the data\n")

print("find constant")
find_consonant(input_DATA)
print("find vowel")
find_vowel(input_DATA)
print("find constant_vowel")
find_consonant_vowel(input_DATA)
print("find after vowel")
find_after_vowel(input_DATA)
print("Abbreviate")
eXtract(input_DATA)
print("Camel")
Camel(input_DATA)

'''
re.sub
Can be used to abbreviate King Saud University to KSU
'''
'''
find_consonant("Returning to physics")

print("\n************\n")

find_vowel("Thirty years agooooo ")

print("\n************\n")

find_consonant_vowel("Fameeeeee is fleeting ")

print("\n************\n")

find_after_vowel("Take it sleazy - Adam.")
'''
