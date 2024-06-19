temperature = float(input("Enter the temperature: "))
conversion = input("Convert to (F)ahrenheit or (C)elsius? ").upper()
if conversion == "F":
    converted_temp = (temperature * 9/5) + 32
    print(converted_temp)
elif conversion == "C":
    converted_temp = (temperature - 32) * 5/9
    print(converted_temp)
else:
    print("Invalid conversion choice.")
