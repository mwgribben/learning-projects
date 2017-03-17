# Counts the vowels in a string

vowels = "aeiou"

input_string = input("Enter a string: ")

for letter in vowels:
    count = len(input_string.split(letter))-1
    if count>0:
        print (letter + ": " + str(count))
