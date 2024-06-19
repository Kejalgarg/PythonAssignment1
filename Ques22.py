numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
min_value = min(numbers)
max_value = max(numbers)
print("The minimum value is: ", min_value)
print("The maximum value is: ", max_value)
