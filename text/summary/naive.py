
while True:
    try:
        file_name = input("Enter the .txt file name: ");
        file = open(file_name,"r");
    except:
        print("Couldn't find that file. Try again.");
        continue
    break

summary = "";
words = 0;

for line in file.readlines():
    summary += line.split(".")[0]
    words += len(line.split(" "))

file.close();

print("\nThis file has " + str(words)+ " words\n");
print("Summary:\n"+summary);
