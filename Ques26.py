user_input = input("Enter a string: ")
prefix = input("Enter a prefix: ")
suffix = input("Enter a suffix: ")
if user_input.startswith(prefix):
    print("The string starts with ", prefix)
else:
    print("The string does not start with", prefix)

if user_input.endswith(suffix):
    print("The string ends with ", suffix)
else:
    print("The string does not end with ", suffix)
