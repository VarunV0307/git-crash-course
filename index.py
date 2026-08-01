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

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a > b:
    print(a, "is greater than", b) 
elif a < b:
    print(b, "is greater than", a)
else:
    print(a, "is equal to", b)
print("The sum of", a, "and", b, "is:", a + b)

name = input("Enter your name: ")
print("Hello", name, "!")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: ")) 
print("The sum of", num1, "and", num2, "is:", num1 + num2)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# AND operator
print("\nAND Operator:")
print("a > 0 and b > 0 =", a > 0 and b > 0)

# OR operator
print("\nOR Operator:")
print("a > 0 or b > 0 =", a > 0 or b > 0)

# NOT operator
print("\nNOT Operator:")
print("not(a > b) =", not(a > b))