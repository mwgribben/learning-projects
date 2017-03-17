# Counts the vowels in a string

vowels = "aeiou"

input_string = input("Enter a string: ")

for letter in vowels:
    count = input_string.count(letter)
    if count>0:
        print (letter + ": " + str(count))
