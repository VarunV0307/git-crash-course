num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
sum = num1 + num2 
print("The sum of", num1, "and", num2, "is:", sum)
print("The product of", num1, "and", num2, "is:", num1 * num2)
print("The difference of", num1, "and", num2, "is:", num1 - num2)

if num1 > num2:
    print(num1, "is greater than", num2)
else:
    print(num2, "is greater than", num1)
if num1 == num2:
    print(num1, "is equal to", num2)
else:
    print(num1, "is not equal to", num2)
if num1 % 2 == 0:
    print(num1, "is an even number")
if num1 % 2 != 0:
    print(num1, "is an odd number")

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

a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 

print("\nArithmetic Operations:")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Exponentiation =", a ** b)
