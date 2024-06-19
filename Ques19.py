import string
user_input = input("Enter a string: ")
cleaned_string = ''.join(char for char in user_input if char not in string.punctuation)
print("The string without punctuation is: ",cleaned_string)
