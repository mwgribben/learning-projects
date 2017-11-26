
input_string = input("Enter a string: ");
words = len(input_string.split(" "))

if words == 1:
    print("This string has " + str(len(input_string.split(" "))) + " word");
else:
    print("This string has " + str(len(input_string.split(" "))) + " words");
