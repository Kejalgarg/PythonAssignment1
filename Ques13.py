from datetime import datetime
thisyear = datetime.now().year
yr=int(input("Enter birth year: "))
age= thisyear-yr
print("age: ", age)