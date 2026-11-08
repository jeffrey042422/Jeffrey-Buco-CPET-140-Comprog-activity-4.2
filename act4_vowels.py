#BUCO JEFFREY G
#BAET 2B 2102
#Vowel Counter


sentence = input("Sentence: ")

vowels = "aeiouAEIOU"
count = 0

for character in sentence:
    if character in vowels:
        count += 1

print("Vowels:", count)
