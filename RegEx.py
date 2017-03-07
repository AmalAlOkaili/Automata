import re


DATA = []
input_DATA = raw_input("Enter the data\n")


def find_consonant(word): #Checks TWO consecutive consonants
    for match in re.findall(r"\w+[^ouieaOUIEA]{2}\b", word):
          print match


def find_vowel(word):  #Checks FIRST and LAST chars
        for match in re.findall("\w{5,}", word):
            if re.findall(r"(^[ouieaOUIEA].+[ouieaOUIEA]$)", match):
                 print match




def find_consonant_vowel(word):    #Checks FIRST and LAST chars {consonant , vowel}
     for match in re.findall("\w{7,}", word):
         if re.findall(r"(^[^ouieaOUIEA].+[ouieaOUIEA]$)", match):
          print match



def find_after_vowel(word): #Checks letter after VOWELS
    for match in re.findall(r"[ouieaOUIEA](\w+)", word):
          print match


#def find_abbrv:

#def fin_cameCase:



find_consonant(input_DATA)
find_vowel(input_DATA)
find_consonant_vowel(input_DATA)
find_after_vowel(input_DATA)


'''
re.sub
Can be used to abbreviate King Saud University to KSU
'''
'''
find_consonant("Returning to physics")

print("\n************\n")

find_vowel("Thirty years agooooo")

print("\n************\n")

find_consonant_vowel("Fameeeeee is fleeting")

print("\n************\n")

find_after_vowel("Take it sleazy - Adam.")
'''