#Giraffe Language:
#vowels -> g
#example:
#dog -> dgg
#cat -> cgt

print("========Giraffe Translator========")
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #sets letter to lower case and checks if it is in the string of vowels
            if letter.isupper() :       #checks if vowel is upper or lower case
                translation = translation + "G"
            else:
                translation = translation + "g"
        else :
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

print("========Giraffe Translator========")
