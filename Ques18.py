string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
anagrams = sorted(string1) == sorted(string2)
if anagrams:
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")
