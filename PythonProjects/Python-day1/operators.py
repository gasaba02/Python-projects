# Operators:
#
# Arithmetic Operators: + - * / \\ % **
#
# Assignment Operators: = += -= *= /= %= **=
#
# Comparison Operators:== != > < >= <=
#
# Logical Operators: and or not
#
# Bitwise Operators: & | ~ >> <<
#
# Special Operators: is and is not


# Arithmetic Operators: + - * / \\ % **

a = 3
b = 5
empty = ""

print("a is",a,"and b is", b)
print("Sum of a and b is", a+b)
print("Difference of b and a is", b-a)
print("Multiplication of a and b is", a*b)
print("Division of a and b is", b/a)

#This removes the decimal point after dividing
print("Floor division of b and a is", b//a)

# This prints only the remainder after diving two numbers
print("a Modulo b is", a%b)

# a^b
print("a to the power of b is", a**b)
print(empty)

# Assignment Operators: = += -= *= /= %= **=

a = 10
b = 5
c = a+b
print("a =",a)
print("b =",b)
print("a + b =",c)

print(empty)

print("a is", a)

# same as a = a+b
a+=b
print("After doing a+=b")
print("what is a now",a)

print(empty)

# Comparison Operators:== != > < >= <=

a=20
b=10

print("a is",a, "and b is",b)
print("is a equal to b?", a==b)
print("is a NOT equal to b?", a!=b)
print("is a greater than b?", a>b)
print("is a less than b?", a<b)
print("is a greater than or equal to b?", a>=b)
print("is a less than or equal to b?", a<=b)













