# Q1. Write a  python program that accepts a string from the user and counts the number of vowels and consonants in it.

# ch = input("Enter a character: ")
# if ch in "aeiouAEIOU":
#     print("vowel")
# else:
#     print("consonant")

# Maths = int(input("Enter a number in Maths "))
# English = int(input("Enter a number in English ")
# Science = int(input("Enter a number in Science "))

# if Maths >=40 and English >=40 and Science >=40:
#     print("pass")
# else:
#     print("fail")



# Q3.
# a=int(input("Enter a First number"))
# b=int(input("Enter a Second number"))
# c=int(input("Enter a third number"))

# if a==b and b==c and a==c:
#     print("All numbers are equal")
# elif a==b or b==c or a==c:
#     print("Two numbers are equal")
# else:
#     print("All numbers are different")



# Q4.Movie ticket discount

# age = int(input("Enter your age: "))

# if age <5:
#     print(" ticket is free ")
# elif age >=5 and age <=17:
#     print("ticket price is 100")
# elif age >=18 and age <=59:
#     print("ticket price is 200")
# else:
#     print("ticket price is 120")

# Q5.
# num = int(input("Enter a number: "))
# if num ==0:
#     print("Zero")
# elif num>0 and num%2!=0:
#     print("Positive odd number")
# elif num>0 and num%2==0:
#     print("Positive even number")
# elif num<0 and num%2!=0:
#     print("Negative odd number")
# else:
#     print("Negative even number")  

# Class_3

# Nested if else statements
#Q1.
# num = int(input("Enter a number: "))    
# if num>0:
#     print("num is positive ")
#     if num>=10:
#         print(" and num>10")
#     else:
#         print(" and num<10")
# else:
#     print("num is negative ")

#Q2.
# num = int(input("Enter a number: "))    
# if num%2==0:
#     if num%4==0:
#         print("num is even and div by 4")
#     else:
#         print("num is even and not div by 4")
# else:
#     print("num is odd ")

#Q3.
# Pin = int(input("Enter your pin : "))
# if Pin == 1234:
#     amount = int(input("Enter your amount "))
#     if amount<=5000:
#         print("Transaction is successful")
#     else:
#         print("Transaction is unsuccessful")
# else:
#     print("Invalid pin")

# Q4.
# num=int(input("Enteer a number"))

# if num>0:
#     print("num is +")
#     if num%2==0:
#         print("num is even")
#         if num%4==0:
#             print("div by 4")
#         else:
#             print("not div by 4")
#     else:
#         print(" num is odd")
# else:
#     print("num is -") 

#Q5.
a=int(input("Enter first number"))
b=int(input("Enter second number"))

if a>=b:
    if a>0:
        print("a is +")
        if a%2==0:
            print("a>b and a is even ")
        else:
            print("a>b and a is odd ")
    else:
        print("a is -")        
elif b>=a:
    if b>0:
        print("b is +")
        if b%2==0:
            print("b>a and b is even ")
        else:
            print("b>a and b is odd ")
    else:
        print("b is -")                        



