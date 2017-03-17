# Converts an English string into Pig Latin 
# See rules: https://en.wikipedia.org/wiki/Pig_Latin 

import re

vowels = "aeiouy"

input_string = input("Enter a phrase: ")

output_string = input_string

for word in re.split("[^A-Za-z]+",input_string):
	if (word[0] in vowels) and (word[0]!="y"):
		new_word = word+"way"
	else:
		first_cons = re.split("["+vowels+"]+",word)[0]
		new_word = word[len(first_cons):] + first_cons + "ay"
	

	split_string = output_string.split(word)
	output_string = split_string[0]+new_word+"".join(split_string[1:])

print(output_string)
