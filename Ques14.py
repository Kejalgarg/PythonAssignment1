lines = []
print("Enter multiple lines of text: ")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
print("You entered:")
for line in lines:
    print(line)
