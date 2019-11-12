import nltk
from nltk.tokenize import word_tokenize

from spellchecker import SpellChecker

spell = SpellChecker()
input_string=[]
# find those words that may be misspelled
misspelled = input("enter the word or string")
input_string=word_tokenize(misspelled)
final_string=''
#print(misspelled)
for word in input_string:
    # Get the one `most likely` answer
    print(spell.correction(word))
    
    final_string+=spell.correction(word)
    final_string+=' '
    # Get a list of `likely` options
    print(spell.candidates(word))
print("final string is"+final_string)