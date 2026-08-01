a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
sum = a + b 
print("The sum of", a, "and", b, "is:", sum)
print("The product of", a, "and", b, "is:", a * b)
print("The difference of", a, "and", b, "is:", a - b)

if a > b:
    print(a, "is greater than", b)
else:
    print(b, "is greater than", a)
if a == b:
    print(a, "is equal to", b)
else:
    print(a, "is not equal to", b)
if a % 2 == 0:
    print(a, "is an even number")
if a % 2 != 0:
    print(a, "is an odd number")