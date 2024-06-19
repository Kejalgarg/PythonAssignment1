num=int(input("Enter number: "))
sum=0
while num:
    sum += num%10
    num//=10
print(sum)