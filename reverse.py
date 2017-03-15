# Takes in a string and prints the reverse

input_string = input("Enter a string: ")

output_string=""

for i in range(0,len(input_string)):
    output_string+=input_string[len(input_string)-1-i]

print(output_string)
