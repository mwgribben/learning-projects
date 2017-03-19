# Checks if a string is a palindrome

input_string = input("Enter a string: ")

if input_string==input_string[::-1]:
    print("This is a palindrome!")
else:
    print("This is not a palindrome")
