
"""                             ----------> Operators practice sheet:22-09-2026 <---------- 



1.Take input of two numbers and add them.

Input: 10, 20

Output: 30 

n_1 = int(input("Enter first number :"))
n_2 = int(input("Enter second number :"))

sum = n_1 + n_2
print(f"Sum of two numbers {n_1} + {n_2} are : {sum}") """







"""**2.Take input of two numbers and subtract the second number from the first number.**

**Input:** 20, 8

**Output:** 12 

n_1 = int(input("Enter first number :"))
n_2 = int(input("Enter second number :"))

sub = n_1 - n_2
print(f" Subtraction of two numbers {n_1} - {n_2} are : {sub}") """







"""# **3.Take input of two numbers and multiply them.**

# **Input:** 5, 6

# **Output:** 30 

n_1 = int(input(" Enter first number :"))
n_2 = int(input(" Enter second number :"))

sum = n_1 * n_2
print(f"Multiplication of two numbers {n_1} * {n_2} are : {sum}") """






"""**4.Take input of two numbers and divide the first number by the second number.**

**Input:** 20, 4

**Output:** 5.0

n_1 = int(input(" Enter first number :"))
n_2 = int(input(" Enter second number :"))

div = n_1 / n_2
print(f"Division of two numbers {n_1} / {n_2} are : {div}") """






"""**5.Take input of a price and quantity and calculate the total cost.** 

**Input:** Price = 50, Quantity = 3

**Output:** 150 

price = int(input("Enter the price of the item: "))
quantity = int(input(" Enter the quantity of the item: "))

total_cost = price * quantity
print(f" Total cost of item is {total_cost}")"""







"""

**6.Take input of marks of 3 subjects and calculate the average marks.**

**Input:** 70, 80, 90

**Output:** 80.0 

marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

average = (marks1 + marks2 + marks3) / 3
print(f"Average marks are: {average}")

"""







""" 

**7.Take input of a number and find its square.**

**Input:** 5

**Output:** 25 

n= int(input("Enter a number to find its square: "))

square = n**2
print(f" The square of {n} is: {square}") 

"""







"""

**8.Take input of total minutes and convert them into hours and remaining minutes.**

**Input:** 135

**Output :** 2 hours 15 minutes 


minutes=int(input("Enter total minutes:"))
 
hours=minutes//60
print(f"minuties in hours are {hours}hr{minutes%60}m ") 

"""





""" 

**9.Take input of a number and find its remainder when divided by 5.**

**Input:** 17

**Output:** 2 

n= int(input("Tell your number: "))

remainder=n%5
print(f"Remainder when {n} divided by 5 is:{remainder}") 

"""







"""

**10.Take input of two numbers and calculate the first number raised to the power of the second number.**

**Input:** 2, 3

**Output:** 8 

n_1=int(input(" Enter first number: "))
n_2=int(input(" Enter second number: "))

print(f"the first number {n_1} raised to the power of the second number {n_2} is: {n_1**n_2} ") 

"""






"""                               ----------> Operators practice sheet : 23-09-2026 <----------




Q1. Add Two Numbers
Take input of two numbers and print their sum.
Input: 12, 18
Output: 30 

n_1=int(input(" Enter first number: "))
n_2=int(input(" Enter second number: "))

print(f"The sum of {n_1} and {n_2} is {n_1+n_2}") """







"""Q2. Find Product 
Take input of two numbers and print their product.
Input: 4, 7
Output: 28 

n_1=int(input(" Enter first number: "))
n_2=int(input(" Enter second number: "))

print(f" The product of {n_1} and {n_2} is {n_1*n_2} ") """







"""Q3. Find Remainder
Take input of two numbers and print the remainder of the first number divided by the second number.
Input: 17, 5
Output: 2 

n_1=int(input(" Enter first number: "))
n_2=int(input(" Enter second number: "))

remainder=n_1%n_2
print(f"The Remainder of {n_1} divided {n_2} is {remainder} ") """








"""Q4. Check Greater Than
Take input of two numbers and check whether the first number is greater than the second number.
Input: 25, 15
Output: True 


n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))

print(f"The first number {n1} is greater than second number {n2} : {n1>n2}") """






"""Q5. Check Less Than
Take input of two numbers and check whether the first number is less than the second number.
Input: 8, 20
Output: True 


n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))

print(f"The first number {n1} is less than second number {n2} : {n1<n2}") """




"""Q6. Check Not Equal
Take input of two numbers and check whether both numbers are not equal.
Input: 10, 15
Output: True


n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))

print(f"The first number {n1} is not equal to second number {n2} : {n1!=n2}")"""



"""Q7. Add Using Assignment Operator
Take a number as input and add 10 to it using an assignment operator.
Input: 25
Output: 35

n = int(input("Enter your number: "))
n += 10
print(f"{n}") """





"""
Q8. Subtract Using Assignment Operator
Take a number as input and subtract 5 from it using an assignment operator.
Input: 30
Output: 25 

n = int(input(" Enter your number: "))
n -= 5 
print(n)
"""




""" 
Q9. Check Greater Than or Equal To
Take input of two numbers and check whether the first number is greater than or equal to the second number.
Input: 20, 20
Output: True 

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print(f"{n1 >= n2}")
"""


"""
Q10. Check Equal
Take input of two numbers and check whether both numbers are equal.
Input: 15, 15
Output: True

n1 = int ( input (" Enter first number: "))
n2 = int ( input (" Enter second number: "))

print (f"{n1 == n2}")
"""


"""                           ----------> If else practice sheet : 24-09-2026 <----------



**Q1. Check Positive or Negative**

Take input of a number and check whether it is positive or negative.

**Input:** 5

**Output:** Positive


n = int(input("Enter your number: "))

if n > 0 :
    print("Positive") 
elif n < 0:
    print("Negative")
"""


"""
**Q2. Check Even or Odd**

Take input of a number and check whether it is even or odd.

**Input:** 8 

**Output:** Even

n = int(input("Enter your number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")  

"""
    






"""
**Q3. Check Greater Number**

Take input of two numbers and print the greater number.

**Input:** 10, 20

**Output:** 20


n1 = int(input(" Enter first number: "))
n2 = int(input(" Enter second number: "))

if n1 > n2:
    print(f"{n1}")
else:
    print (f"{n2}")

"""



"""
**Q4. Check Equal Numbers**

Take input of two numbers and check whether they are equal or not.

**Input:** 10, 10

**Output:** Equal

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if n1 == n2:
    print("Equal")
else:
    print("Not Equal")    

"""


"""
**Q5. Check Pass or Fail**

Take marks as input. If marks are 40 or more, print Pass, otherwise print Fail.

**Input:** 55

**Output:** Pass

Marks = int(input("Enter your marks: "))

if Marks >= 40:
    print("Pass")
else:
    print("Fail")

"""




"""
**Q6. Check Zero**

Take input of a number and check whether it is zero or not.

**Input:** 0

**Output:** Zero


n = int(input("Enter your number: "))

if n == 0:
    print("Zero")
else:
    print("Not Zero")

"""




"""
**Q7. Check Age**

Take age as input. If age is 18 or more, print Adult, otherwise print Minor.

**Input:** 16

**Output:** Minor



Age = int(input("Enter your Age: "))

if Age >= 18:
    print("Adult")
else:
    print("Minor")

"""




"""
**Q8. Check Divisible by 2**

Take input of a number and check whether it is divisible by 2 or not.

**Input:** 12

**Output:** Divisible by 2


n = int(input("Enter your number: "))

if n % 2 ==0:
    print(f"{n} is Divisible by 2.")
else:
    print("not")

"""




"""
**Q9. Check Temperature**

Take temperature as input. If it is greater than 30, print Hot, otherwise print Cold.

**Input:** 25

**Output:** Cold


Temprature = int(input("Enter the Temprature:"))

if Temprature > 30:
    print("Hot")
else:
    print("Cold")

"""







"""
**Q10. Check Number**

Take input of a number. If the number is greater than 10, print Greater, otherwise print Smaller.

**Input:** 7

**Output:** Smaller 


n = int(input("Enter your number: "))

if n > 10:
    print("Greater")
else:
    print("Smaller")

"""





"""                                 ----------> If Else Practice sheet :26-09-2026 <----------




**Q1. Check Number is Greater Than 5**

Take input of a number and check whether it is greater than 5 or not.

**Input:** 8

**Output:** Greater than 5



n = int(input("Enter your number: "))

if n < 5 :
    print(" Less than 5 ")
else:
    print(" Greater than 5 ")

"""









"""

**Q2. Check Number is Less Than 100**

Take input of a number and check whether it is less than 100 or not.

**Input:** 75

**Output:** Less than 100


n = int(input(" Enter your number: "))
if n < 100:
    print(" Less than 100 ")
else:
    print(" Not Less than 100 ")

"""







"""

**Q3. Check Age**

Take age as input. If the age is 18 or more, print Can Drive, otherwise print Cannot Drive.

**Input:** 20

**Output:** Can Drive




Age = int(input(" Enter your Age : "))

if Age >= 18 :
    print(" Can Drive ")
else:
    print(" Cannot Drive ")


"""









"""

**Q4. Check Number is Zero or Not**

Take input of a number and check whether it is zero or not.

**Input:** 5

**Output:** Not Zero


n = int(input(" Enter a number : "))

if n == 0:
    print(" Zero ")
else:
    print(" Not Zero ")

"""








"""

**Q5. Check Marks**

Take marks as input. If marks are 50 or more, print Good, otherwise print Try Again.

**Input:** 65

**Output:** Good


Marks = int(input(" Enter your marks : "))

if Marks >= 50:
    print(" Good ")
else:
    print(" Try Again ")

"""








"""

**Q6. Check Price**

Take price as input. If the price is greater than 500, print Expensive, otherwise print Affordable.

**Input:** 400

**Output:** Affordable



Price = int(input(" Enter the price : "))

if Price > 500 :
    print(" Expensive ")
else:
    print(" Affordable ")

"""









"""
**Q7. Check Number Divisible by 5**

Take input of a number and check whether it is divisible by 5 or not.

**Input:** 20

**Output:** Divisible by 5



n = int(input(" Enter your number: "))

if n % 5 == 0:
    print(" Divisible by 5 ")
else:
    print(" Not Divisible by 5 ")

"""







"""

**Q8. Check Password**

Take a password as input. If the password is 12345, print Correct, otherwise print Incorrect.

**Input:** 12345

**Output:** Correct


Password = int(input(" Enter your password : "))

if Password == 12345:
    print(" Correct ")
else:
    print(" Incorrect ")

"""









"""

**Q9. Check Attendance**

Take attendance percentage as input. If it is 75 or more, print Allowed, otherwise print Not Allowed.

**Input:** 80

**Output:** Allowed


Attendance_percentage  = int(input(" Enter your Attendance Parcentage : "))

if Attendance_percentage >= 75:
    print(" Allowed ")
else:
    print(" Not Allowed ")

"""








"""

**Q10. Check Shopping Amount**

Take shopping amount as input. If the amount is 1000 or more, print Free Delivery, otherwise print Delivery Charges.

**Input:** 1200

**Output:** Free Delivery 


Shoping_amount = int(input(" Enter your shoping amount : "))

if Shoping_amount >= 1000:
    print(" Free Delivery ")
else:
    print(" Delivery Charges ")

"""





#                                    ----------> Nested If Else 28/09/2026 <----------



"""
Q1.Number classification 

Take input of two numbers.First wether the first number is
positive.if positive, check whether it is greater than 
the second number.Otherwise, print First number is not positive 

input:10,5

output:First number is greater 

"""
# a = int(input("Enter first number")) 
# b = int(input("Enter second number "))

# if a>0:
#     if a>b:
#         print("First number is greater ")
#     else:
#         print("First number is smaller ")
# else:
#     print("First number is not positive ")







"""Q2.Student Result 

Take marks of two subject as input. 
first check whether the student has passed
the first subject (33 or above ).if yes , check 
whether the student has passed the second subject . 
print pass or fail.

input:45,60

output:pass """ 

# sub_1 = int(input("Enter first subject marks ")) 
# sub_2 = int(input("Enter second subject marks "))

# if sub_1>=33:
#     if sub_2>=33:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Fail")







"""**Q3. Age and Permission**

Take age and permission (1 for Yes, 0 for No) as input. First
check whether age is 18 or above. If yes, check whether permission 
is 1. Print Allowed or Permission Required.

Input: 20, 1

Output: Allowed """   

# Age = int(input("Enter your age ")) 
# Permission = int(input("Enter 1 for Yes, 0 for No "))

# if Age>=18:
#     if Permission==1:
#         print("Allowed")
#     elif Permission==0:
#         print("Permission Required")
# else:
#     print("Minor")         






"""
**Q4. Number Comparison**

Take two numbers as input. First check whether both numbers 
are equal. If not equal, check which number is greater.

Input: 10, 20

Output: Second Number is Greater

"""

# num_1=int(input("enter first number"))
# num_2=int(input("enter second numbe"))

# if num_1!=num_2:
#     print("not equal")
#     if num_1>num_2:
#         print("num1 is > num2")
#     else:
#         print("num2 is > num1")
# else:
#     print(" equal")
    









"""

**Q5. Shopping Discount**

Take shopping amount and membership status (1 for Member, 0 for 
Non-member) as input. First check whether the person is a member. 
If yes, check whether shopping amount is 1000 or more. 
Print Discount Available or No Discount.

Input: 1500, 1

Output: Discount Available

"""

# Membership_amount = int(input("Enter 1 for member, 0 for non member"))
# Shopping_amount = int(input("Enter your shopping amount"))

# if Membership_amount == 1:
#     if Shopping_amount >= 1000:
#         print("Discount Available")
#     else:
#         print("No Discount")
# else:
#     print("Non Member")







#                   -----------> For loop practice sheet :29-09-2026<------------

"""
Q1. Print Numbers from 1 to N

Take an integer N as input and print all numbers from 1 to N.

Input: 5

Output: 1 2 3 4 5

"""

# num=int(input("Tell your number"))

# for i in range(1,num+1,1):
#     print(i)







""""
Q2. Print Numbers from N to 1 

Take an integer N as input and print numbers from N to 1.

Input: 5

Output: 5 4 3 2 1

"""
# n=int(input("Tell your number "))

# for i in range(n,0,-1):
#     print(i)






"""
Q3. Print Even Numbers

Take an integer N as input and print all even numbers from 1 to N.

Input: 10

Output: 2 4 6 8 10
"""
# n = int(input(" Tell your number "))

# for i in range(1,n+1,):
#     if i%2==0:
#         print(i)







"""
**Q4. Print Odd Numbers**

Take an integer N as input and print all odd numbers from 1 to N.

Input: 10

Output: 1 3 5 7 9
"""
# n=int(input("Tell your number "))

# for i in range(1,n+1):
#     if i%2!=0: 
#         print(i)






"""
**Q5. Print Multiplication Table**

Take an integer N as input and print its multiplication table from 1 to 10.

Input: 3

Output:3 6 9 12 15 18 21 24 27 30
"""
# n=int(input("Tell your number"))

# for i in range(1,11):
#     print(n*i)






"""
**Q6. Sum of First N Natural Numbers**

Take an integer N as input and calculate the sum of numbers from 1 to N.

Input: 5

Output: 15
"""
# n=int(input("Tell your number "))
# sum=0
# for i in range(1,n+1):
    
#     sum = sum+i
# print(sum)





"""
**Q7. Count Numbers from 1 to N**

Take an integer N as input and count how many numbers are present from 1 to N.

Input: 7

Output: 7
"""
# n=int(input("Tell your number "))
# count=0

# for i in range(1,n+1):
#     count = count+1

# print(count)    





"""
**Q8. Print Squares of Numbers**

Take an integer N as input and print the square of each number from 1 to N.

Input: 5

Output: 1 4 9 16 25
"""
# n=int(input("Tell your number "))

# for i in range (1,n+1):
#     square=i**2 
#     print(square)    







"""
**Q9. Sum of Even Numbers**

Take an integer N as input and calculate the sum of all even numbers from 1 to N.

Input: 10

Output: 30
"""
# n=int(input(" Tell your number "))
# sum=0

# for i in range (1,n+1):
#     if i%2==0:
#         sum=sum+i

# print(sum)






"""
**Q10. Print Multiples of 5**

Take an integer N as input and print the first N multiples of 5.

Input: 5

Output: 5 10 15 20 25
"""
# n= int(input(" Tell your number "))
# mult=0
# for i in range(1,n+1):
#     mult=n*i
#     print(mult)
    




#                        -----------> For loop practice sheet :30-09-2026 <-----------




""" Q1.Weekly Attendance Analysis

An institution records the attendance status of a student for 7 consecutive days.
 The status is entered as P for Present and A for Absent.
Write a program to determine the total number of days the student was present and absent.

"""  
# 1st time

# Total_Days_Present = 0
# Total_Days_Absent = 0

# for i in range (1,8):
#     Attendance = input (" Enter A for absent or P for present ")
#     if Attendance == "P":
#         Total_Days_Present += 1
#     elif Attendance == "A":
#         Total_Days_Absent += 1

# print(f"Total number of days Present: {Total_Days_Present}")        
# print(f"Total number of days Absent: {Total_Days_Absent}") 








# 2nd time 

# total_days_present = 0
# total_days_absent = 0 
# print(" Enter your attendance below ")
# for i in range (1,8):
#     Attendance = input("Enter A for absent or P for present : ")
#     if Attendance == "A":
#         total_days_absent += 1
#     elif Attendance == "P":
#         total_days_present += 1 
# print(f"Total number of days the student was Present : {total_days_present} ")
# print(f"Total number of days the student was Absent : {total_days_absent}")            




"""

Q2. Product Quality Inspection

A factory inspects **10 products**. For each product, 
enter 1 if it passes inspection and 0 if it fails.

Determine the **number of products that passed and failed** the inspection.

"""

# Passed = 0
# Failed = 0

# for i in range (1,11):
#     n = int(input(" Inspect the product : Enter 1 for Pass,0 if it fail "))
#     if n == 1:
#         Passed_count = Passed + 1
#     else:
#         Failed_count = Failed  + 1
# print(f"Number of products that Passed:{Passed_count} and Failed:{Failed_count}")   

        





"""

**Q3. Monthly Savings Analysis**

A person records the amount saved on **7 different days**.

Write a program to calculate the **total savings** and determine how many days the savings were **greater than ₹500**.

"""
  
# Total_savings = 0
# Days_count = 0 

# for i in range (1,8):
#     savings = int(input(" Enter your saving amount : "))

#     Total_savings += savings

#     if savings > 500:
#         Days_count += 1

# print(f"Total savings : {Total_savings}")
# print(f" Days the saving were greater than 500 is  {Days_count} ")        



"""
**Q4. Electricity Consumption**

A household records its electricity consumption for **7 days**.

Write a program to calculate the total units consumed and count
how many days the consumption was more than 10 units.

"""

# Total_units_consumed = 0
# Days_count = 0

# for i in range (1,8):
#     Units_consumed = int(input(f"Enter the untis consumed : "))
#     Total_units_consumed += Units_consumed
#     if Units_consumed > 10:
#         Days_count += 1
# print (f"Total Units Consumed : {Total_units_consumed} ")
# print (f"Days the consumption was more than 10 units :{Days_count} ")    
















"""
Q5. Attendance Eligibility

A student has 10 classes. For every class, enter P for Present and A for Absent.

Calculate the student's attendance percentage and display whether
 the student has 75% or more attendance.
 
 """

# Total_present_in_classes = 0
# Total_absent_in_classes = 0

# for classes in range (1,11):
#     Attendance = input(f" Enter A for Absent in Class {classes} and P for Present in Class {classes}: ")
#     if Attendance == "A":
#         Total_absent_in_classes += 1
#     elif Attendance == "P":
#         Total_present_in_classes += 1
# Attendance_percentage = Total_present_in_classes / classes * 100
# print(f" The student's attendance percentage is : {Attendance_percentage}% ")            











"""                          ----------> For loop practice sheet :01-10-2026 <----------                                             """







"""

Q1. Count Numbers Divisible by 3

Take an integer N as input and count how many numbers from 1 to N are divisible by 3.

Example:
Input: 15
Output: 5

"""

# N = int(input("Enter a number : "))
# count = 0

# for i in range (1,N+1):
#     if i % 3 == 0:
#         count += 1
# print(f"Numbers from 1 to {N} are divisible by 3 is {count}")        






"""

Q2. Find the Largest Among N Numbers

Take N numbers as input and determine the largest number among them.

Example:
Input:
5
10
25
7
18
12

Output:25

"""

# N = int(input("How many numbers? : "))
# num = int(input("Enter a number : "))
# Largest_number = num

# for i in range(1,N):
#     num = int(input("Enter a number : "))

#     if num > Largest_number:
#         Largest_number = num

# print(f"Largest number among them is {Largest_number}")        





"""

Q3.Take N numbers as input. Calculate their average.

Example:
Input:
5
10
20
30
40
50

Output:

30.0

"""

# N = int(input("How many numbers? : "))
# Sum = 0

# for i in range(N):
#     num = int(input("Enter a number : "))
#     Sum += num
# Average = Sum/N
# print(Average)   






"""


Q4. Check Perfect Number

Take an integer N as input and check whether it is a perfect number.

A perfect number is a number whose proper factors add up to the number itself.

Example:
Input: 6
Output: Perfect Number

"""

# N = int(input("Enter a number : "))
# Sum = 0
# for i in range (1,N):
#     if N %i == 0:
#         Sum += i
# if Sum == N:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")    












"""


Q5. Print Numbers Divisible by 10

Take an integer N as input and print all the numbers from 1 to N that are divisible by 10.

Example:
Input: 50

Output:
10
20
30
40
50 


"""
# N = int(input("Enter a number : "))

# for i in range (1,N+1):
#     if i % 10 == 0:
#         print(i)







"""                            ----------> For loop problems:02-10-2026 <----------                                     """





"""

Q1. Difference between Sum of Odd numbers and Sum of Even Numbers

Take an integer N as input. Calculate the sum of even numbers and 
the sum of odd numbers from 1 to N, then find the difference between the two sums.

Example:
Input: 5
Output: 3  

"""


# n=int(input(" Enter a number:"))

# i=2
# sum_even=0
# sum_odd=0

# for i in range(1,n+1):
#     if i%2==0:
#         sum_even+=i
#         i=i+1 
#     else:
#         sum_odd+=i
#         i=i+1    
# difference=sum_odd-sum_even
# print(f"Difference between sum of even {sum_even} and sum of odd {sum_odd} is {difference}") 

 
    
    
     


""" 

Q2. Difference Between Largest and Smallest

Take N numbers as input and calculate the difference between the largest and smallest number.

Example:
Input:
5
10
25
7
18
12

Output:22

"""
# N = int(input("How many numbers? : "))

# num = int(input(" Enter a number : "))

# Largest_number = num
# Smallest_number = num


# for i in range (1,N):
#     num = int(input(" Enter a number : "))

#     if num > Largest_number:
#         Largest_number = num
#     elif num < Smallest_number:
#         Smallest_number = num       
# Difference = Largest_number - Smallest_number        
# print(f"Difference between the largest and smallest number is : {Difference} ")            
        






"""

Q3. Find the Smallest Number

Take N numbers as input and determine the smallest number among them.

Example:
Input:
5
18
7
25
3
12

Output:
3

"""

# N = int(input("How many numbers? : "))
# number = int(input("Enter a number : "))

# Smallest_number = number 

# for i in range (1,N):
#     number = int(input("Enter a number : "))

#     if number < Smallest_number:
#         Smallest_number = number
# print(f"Smallest number among them is {Smallest_number}")        
    









"""

Q4. Count Numbers Having Digit 0

Take N integers as input and count how many of them contain the digit 0.

Example:
Input:
5
10
25
30
17
40

Output:
3

"""

# N =int(input("How many numbers? : "))
# count_digit_with_zero = 0

# for i in range (1,N+1):
#     num = input("Enter a number: ")

#     if '0' in num:
#         count_digit_with_zero += 1        

# print(f"The numbers that contain the digit 0 is {count_digit_with_zero}")        

    








"""
Q5. Count Numbers Ending with 5

Take an integer N as input and count how many numbers from 1 to N end with the digit 5.

Example:

Input: 30

Output: 3

"""
# N = int(input("Enter a number : "))
# count_num_end_with_5 = 0 

# for i in range (1,N+1):
#     if i % 10 == 5:
#         count_num_end_with_5 += 1

# print(f"Numbers from 1 to {N} end with the digit 5 is {count_num_end_with_5}")        






"""

Q6. Check Equal First and Last Digit

Take an integer N as input and check whether its first digit and last digit are the same.

Example:

Input: 12341

Output: Same 


"""
# N = int(input("Enter a number : "))
# First_Digit = N
# Last_Digit = N % 10

# for i in range (len(str(N))-1):   #   Agar for loop se karna hai to string me convert karna padega
#     First_Digit = First_Digit // 10 
# if First_Digit == Last_Digit:
#     print("Same")
# else:
#     print("Not Same")    



#                               ----------> While loop problems: 03-10-2026 <----------





"""
Q1. Reverse a Number
Take an integer N as input and print its reverse.
Example:
Input: 12345
Output: 54321
"""
# n = int(input("Enter a number : "))
# rev = 0

# while n != 0:
#     last_digit = n%10
#     rev = rev * 10 + last_digit
#     n = n//10
# print(rev)  
  




# n = int(input("Enter a number : "))
# rev = 0

# while n!=0:
#     digit = n % 10 
#     rev = rev * 10 + digit
#     n = n//10
# print(rev)    







"""
Q2. Check Palindrome Number
Take an integer N as input and check whether the number remains the same when its digits are reversed.
Example:
Input: 121
Output: Palindrome
"""
# 1st time

# n = int(input("Enter a number : "))
# temp = n
# rev = 0
# while n != 0:
#     digit = n % 10 
#     rev = rev * 10 + digit
#     n = n // 10
# if rev == temp:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")        








# 2nd time

# n = int(input("Enter a number : "))
# temp = n
# rev = 0
# while n != 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# if rev == temp:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")    







"""
Q3. Count Digits Greater Than 5
Take an integer N as input and count how many digits in the number are greater than 5.
Example:
Input: 583721
Output: 3

"""
# n = int(input("Enter a number : "))
# count = 0
# while n != 0:
#     a = n%10
#     if a > 5:
#         count +=1
#     n = n//10
# print(count)

# 2nd time

# n = int(input("Enter a number : "))
# count = 0
# while n != 0:
#     digit = n % 10
#     if digit > 5:
#         count += 1
#     n = n // 10
# print(count)        






"""

Q4. Product of Digits
Take an integer N as input and calculate the product of all its digits.
Example:
Input: 234
Output: 24
"""

# n = int(input("Enter a number : "))
# product_digit = 1


# while n != 0:
#     product = n % 10
#     product_digit = product_digit * product
#     n = n//10
# print(product_digit)







"""
Q5. Check Whether a Number Contains Digit 7
Take an integer N as input and check whether the digit 7 is present in the number.
Example:
Input: 58371
Output: Present

"""
# n = int(input("Enter a number : "))
# count=0
# while n>0:
#     last=n%10
#     if last==7:
#         count+=1
#     n//=10
# if count>0:
#     print('present')
# else:
#     print('not present')

            





"""
Q6. Count Digits Divisible by 3
Take an integer N as input and count how many digits are divisible by 3, including 0.
Example:
Input: 93621
Output: 3

"""


# n = int(input("Enter a number : "))
# Count = 0

# while n > 0:
#     last_digit = n % 10 

#     if last_digit % 3 == 0:
#         Count += 1
#     n = n // 10
# print(Count)                











"""
Q7. Replace Every Digit with 9
Take an integer N as input and create a new number by replacing every digit with 9.
Example:
Input: 1234
Output: 9999
"""
# 2nd Time

# n = int(input(" Enter a number : "))
# new_number = 0

# while n > 0:
#     last_digit = n % 10 
#     if last_digit > 0:
#         new_number = new_number * 10 + 9    
#     n = n // 10    
# if n == 0:
#         new_number = new_number * 10 + 9    
# print(new_number)        








# n = int(input(" Enter a number : "))
# new_number = 0

# while n != 0:
#     last_digit = n % 10 

#     if last_digit >= 0:
#         new_number = new_number * 10 + 9 
#     n = n // 10
# if n == 0:
#     new_number = new_number*10 + 9    
# print(new_number)            







"""
Q8. Find the Second Largest Digit
Take an integer N as input and find the second largest digit present in N.
Example:
Input: 5832
Output: 5
"""
# n = int(input(" Enter a number : "))
# largest = 0 
# sec_largest = 0
# while n > 0:
#     last = n % 10 
#     if last > largest:
#         largest = last
#     elif sec_largest < largest and sec_largest < last:
#         sec_largest = last        
#     n = n // 10    
# print(largest)
# print(sec_largest)            











"""
Q9. Check Whether All Digits Are Even
Take an integer N as input and check whether every digit of the number is even.
Example:
Input: 2486
Output: Yes

"""
# 1st Time  

# n = 12234

# a=len(str(n))
# count=0
# while n>0:
#     last=n%10
#     if last%2==0:
#         count+=1
#     n//=10
# if a==count:
#     print('yes')
# else:
#     print('no')





# 2nd Time
# n = int (input("Enter a number : "))
# target = (len(str(n)))
# even_count = 0

# while n > 0:
#     last_digit = n % 10 

#     if last_digit % 2 == 0:
#         even_count += 1 
#         n = n // 10
#     else:
#         print("No")
#         break    
# if even_count == target:
#     print("Yes")     



# 3rd time 

# n = int(input(" Enter a number : "))
# target = (len(str(n)))
# count = 0 
# while n > 0 :
#     last = n % 10 

#     if last % 2 ==0 :
#         count += 1
#         n = n // 10     
#     else :
#         print("No")
#         break 
# if count == target:
#     print("Yes")    








"""

Q10. Remove the Last Digit
Take an integer N as input and remove its last digit using arithmetic operations.
Example:
Input: 12345
Output: 1234

"""

# n = int(input("Enter a number : "))

# while n > 0:
#     n=n//10
#     break
# print(n)


# n=1234
# while n>999:
#     n=n//10
# print(n)








#                                  ----------> Functions practice sheet :05-10-2026 <----------





"""
Q1. Add Two Numbers
Create a function add() that takes two numbers as arguments and returns their sum.

Example:
Input: 10 20
Output: 30
"""

# def add(a,b):
#     sum = a+b
#     print(sum)    

# add(10,20)







"""
Q2. Check Even or Odd
Create a function check_even_odd() that takes a number and returns whether it is Even or Odd.

Example:
Input: 7
Output: Odd

"""
# def check_even_odd(number):
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")        


# check_even_odd(7)



"""
Q3. Find Square
Create a function square() that takes a number and returns its square.

Example:
Input: 6
Output: 36
"""

# def square(Number):
#     Number **= 2
#     print(Number)


# square(2)



"""
Q4. Find Maximum
Create a function maximum() that takes two numbers and returns the greater number.

Example:
Input: 15 25
Output: 25

"""
# def maximum(a,b):
#     if a>b :
#         print(a)
#     else:
#         print(b)    

# maximum(15,25)







"""
Q5. Check Number
Create a function check_number() that takes a number and checks whether it is Positive, Negative, or Zero.

Example:
Input: -8
Output: Negative
"""

# def check_number(Number):
#     if Number > 0:
#         print("Positive")
#     elif Number < 0:
#         print("Negative")
#     elif Number == 0:
#         print("Zero")

# check_number(-8)

"""
Q6. Calculate Simple Interest
Create a function simple_interest() that takes P, R, and T and returns the Simple Interest.

Formula:
SI = (P × R × T) / 100

Example:
Input:
P = 1000
R = 5
T = 2

Output:100
"""
# def simple_intrest(P,R,T):
#     print (f"{P*R*T//100}")

# simple_intrest(1000,5,2)    







"""
Q7. Find Cube
Create a function cube() that takes a number and returns its cube.

Example:
Input: 4
Output: 64
"""
# def cube (Number):
#     Number **= 3
#     print(Number)


# cube(4)




"""

Q8. Check Voting Eligibility
Create a function eligible() that takes age as an argument.
If age is 18 or above, return "Eligible", otherwise return "Not Eligible".

Example:
Input: 20
Output: Eligible

"""
# def eligible(age):
#     if age >= 18:
#         print ("Eligible")
#     else:
#         print ("Not Eligible") 

# eligible(20)    










"""
Q9. Find Factorial
Create a function factorial() that takes a number and returns its factorial.

Example:
Input: 5
Output: 120
"""
# def factorial(Number):
#     fact = 1
#     for i in range(1,Number+1):
#         fact *= i
#     print(fact)

# factorial(5)        





"""
Q10. Count Digits
Create a function count_digits() that takes a number and returns the total number of digits.

Example:
Input: 12345
Output: 5

"""
# def count_digit(Number):
#     count = 0
#     while Number > 0:
#         last = Number % 10
#         count += 1
#         Number = Number//10
#     print(count)

# count_digit(12345)







#                                 ----------> Function practice sheet :06-10-2026 <----------




"""

Q1. Find the Largest of Three Numbers
Create a function largest() that takes three numbers and returns the largest number.

Example:
Input: 12 45 23
Output: 45

"""

# def largest(n_1,n_2,n_3):
#     lar = 0        
#     for i in (n_1,n_2,n_3):
#         if i > lar:
#             lar = i
#     print(lar)
# largest(12,45,23)




"""
Q2. Check Prime Number
Create a function is_prime() that takes a number and returns "Prime" if the number is prime, otherwise returns "Not Prime".

Example:
Input: 17
Output: Prime
"""
# def is_prime(number):
#     count = 0
#     for i in range (1,number+1):
#         if number % i == 0:
#             count += 1
#     if count == 2:
#         print("Prime")
#     else:
#         print("Not a Prime")        


# is_prime(17)





"""

Q3. Sum of Digits
Create a function sum_of_digits() that takes a number and returns the sum of its digits.

Example:
Input: 12345
Output: 15

"""
# def sum_of_digits(Number):
#     sum = 0
#     while Number > 0:
#         last = Number % 10
#         sum = sum + last
#         Number=Number//10
#     print(sum)

# sum_of_digits(12345)                







"""
Q4. Reverse a Number
Create a function reverse_number() that takes a number and returns its reverse.

Example:
Input: 1234
Output: 4321

"""
# def reverse_number(number):
#     rev = 0
#     while number > 0:
#         last_digit = number % 10
#         rev = rev * 10 + last_digit
#         number=number//10    
#     print(rev)     


# reverse_number(1234)

"""
Q5. Check Palindrome Number
Create a function is_palindrome() that takes a number and checks whether it is a palindrome.

Example:
Input: 1221
Output: Palindrome

"""
# def is_palindrome(number):
#     temp = number
#     rev = 0
#     while number > 0:
#         last_digit = number%10
#         rev = rev*10 + last_digit
#         number= number//10
#     if rev == temp:
#         print("Palindrome")    
#     else:
#         print("Not a Palindrome")


# is_palindrome(1221)





"""
Q6. Find GCD of Two Numbers
Create a function gcd() that takes two numbers and returns their Greatest Common Divisor (GCD).

Example:
Input: 24 36
Output: 12

"""
# def gcd(number_1,number_2):
#     a = []
#     b = []
#     for i in range(1,number_1+1):
#         if number_1 % i == 0:
#             a.append(i)         #              but while se easy hoga 
#     for i in range(1,number_2+1):
#         if number_2 % i == 0:
#             b.append(i)
#     for i in a:
#         if i in b:
#             gcd_value = i
#     print(gcd_value)
# gcd(24,36)
"""a=int(input("enter first number:"))
b=int(input("enter second number:"))
def gcd(a,b):
    while b > 0:
        remainder = a%b
        a = b
        b = remainder
    return b
print(gcd(a,b))"""

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# def gcd(a,b):
#     while a > 0:
#         remainder = b % a
#         b = a
#         a = remainder
#     return b
# print(gcd(a,b))




"""
Q7. Find the Largest Digit
Create a function largest_digit() that takes a number and returns the largest digit present in it.

Example:
Input: 58321
Output: 8

"""
#              Ban jayega






"""
Q8. Count Even and Odd Digits
Create a function count_even_odd() that takes a number and returns the count of even and odd digits.

Example:
Input: 123456
Output:
Even digits: 3
Odd digits: 3
"""





#              BAN JAYEGA





"""
Q9. Check Armstrong Number
Create a function is_armstrong() that takes a number and checks whether it is an Armstrong number.

Example:
Input: 153
Output: Armstrong

"""

# def is_armstorange(number):
#     Og_number = number
#     sum = 0 
#     digit_count = len(str(number))
#     while number > 0:
#         last_digit = number % 10 
#         sum_power = last_digit ** digit_count
#         sum += sum_power
#         number = number // 10
#     if sum == Og_number:
#         print("Armstrong")
#     else:
#         print("Not a Armstrong")        

# is_armstorange(153)








"""
Q10. Find the Second Largest Digit
Create a function second_largest_digit() that takes a number and returns the second largest digit present in it.

Example:
Input: 58321
Output: 5

"""
# def second_largest_digit(number):
#     largest = 0
#     sec_largest = 0 
#     while number != 0:
#         last_digit = number % 10 
#         if last_digit > largest:
#             largest = last_digit    
#         elif sec_largest < largest and sec_largest < last_digit:
#             sec_largest = last_digit         
#         number = number // 10 
#     print(sec_largest)

# second_largest_digit(58321)    








#                                      List practice sheet :09-10-2026









"""
Q1. Find the Smallest Element

Create a list of numbers and find the smallest element without using the min() function.

Example:

Input: [12, 5, 23, 8, 17]

Output: 5
"""

# l = [12, 5, 23, 8, 17]

# smallest = l[0]

# for elem in l:
#     if elem < smallest:
#         smallest = elem
# print(smallest)









"""
Q2. Count Positive and Negative Numbers

Create a list and count the number of positive and negative elements. Ignore zeros.

Example:

Input: [10, -5, 20, -8, 0, 7]

Output:

Positive: 3

Negative: 2
"""







"""
Q3. Calculate the Average

Create a list of numbers and calculate the average of all its elements.

Example:

Input: [10, 20, 30, 40]

Output: 25.0

Q4. Count Occurrences of an Element

Create a list and count how many times a given number appears in it.

Example:

Input: [2, 4, 2, 6, 2, 8]

Number: 2

Output: 3

Q5. Print Elements at Even Indices

Create a list and print the elements present at even indices (0, 2, 4, …).

Example:

Input: [10, 20, 30, 40, 50, 60]

Output: [10, 30, 50]

Q6. Find the Second Largest Element

Create a list and find the second largest distinct element without using sort() or max().

Example:

Input: [10, 25, 15, 40, 30]

Output: 30

Q7. Replace Negative Numbers with Zero

Create a list and replace every negative element with 0.

Example:

Input: [10, -5, 20, -8, 7]

Output: [10, 0, 20, 0, 7]

Q8. Find the Sum of List Elements

Create a list of numbers and calculate the sum of all its elements.

Example:

Input: [10, 20, 30, 40]

Output: 100

Q9. Find the Largest Element

Create a list of numbers and find the largest element without using the max() function.

Example:

Input: [12, 45, 23, 67, 34]

Output: 67

Q10. Reverse a List

Create a list and reverse its elements without using the reverse() method.

Example:

Input: [10, 20, 30, 40, 50]

Output: [50, 40, 30, 20, 10]

"""

#                                  List practice sheet :12-10-2026



"""
**Q1. Separate Even and Odd Numbers**

Create a list of integers and separate the even and odd numbers into two different lists.

**Example:**

- Input: [1, 2, 3, 4, 5, 6]
- Output:
    - Even: [2, 4, 6]
    - Odd: [1, 3, 5]

**Q2. Remove Duplicates**

Create a list and remove duplicate elements without using set().

**Example:**

- Input: [1, 2, 3, 2, 4, 1, 5]
- Output: [1, 2, 3, 4, 5]

**Q3. Find the Index of an Element**

Create a list and find the index of a given element without using the index() method.

**Example:**

- Input: [10, 20, 30, 40, 50]
- Element: 30
- Output: 2

**Q4. Swap First and Last Elements**

Create a list and swap its first and last elements.

**Example:**

- Input: [10, 20, 30, 40, 50]
- Output: [50, 20, 30, 40, 10]

**Q5. Find the Second Smallest Element**

Find the second smallest distinct element without using sort() or min().

**Example:**

- Input: [15, 5, 20, 8, 12]
- Output: 8

**Q6. Multiply All Elements**

Create a list and calculate the product of all its elements.

**Example:**

- Input: [2, 3, 4, 5]
- Output: 120

**Q7. Count Numbers Greater Than a Given Value**

Create a list and count how many elements are greater than a given number.

**Example:**

- Input: [10, 25, 15, 40, 30]
- Number: 20
- Output: 3

**Q8. Count Numbers Smaller Than a Given Value**

Create a list and count how many elements are smaller than a given number.

**Example:**

- Input: [10, 25, 15, 40, 30]
- Number: 20
- Output: 2

**Q9. Merge Two Lists**

Merge two lists into a single list without using the + operator.

**Example:**

- Input: [1, 2, 3] and [4, 5, 6]
- Output: [1, 2, 3, 4, 5, 6]

**Q10. Print Elements at Odd Indices**

Print all elements present at odd indices (1, 3, 5, …) of a list.

**Example:**

- Input: [10, 20, 30, 40, 50, 60]
- Output: [20, 40, 60]
"""


#                                    Dictionary practice sheet : 15-10-2026



"""
**Q1. Create a Dictionary**

Create a dictionary containing your name, age, and city. Print the dictionary.

**Example Output:**

{'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}

**Q2. Access a Value**

Given a dictionary, print the value associated with the key "name".

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output: Rahul

**Q3. Add a New Key-Value Pair**

Add a new key "course" with value "Python" to the given dictionary.

**Example:**

- Input: {'name': 'Rahul', 'age': 20}
- Output: {'name': 'Rahul', 'age': 20, 'course': 'Python'}

**Q4. Update a Value**

Update the age of a person to 21.

**Example:**

- Input: {'name': 'Rahul', 'age': 20}
- Output: {'name': 'Rahul', 'age': 21}

**Q5. Delete a Key**

Remove the key "city" from the dictionary.

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output: {'name': 'Rahul', 'age': 20}

**Q6. Check if a Key Exists**

Check whether the key "age" exists in the given dictionary.

**Example:**

- Input: {'name': 'Rahul', 'age': 20}
- Output: Key exists

**Q7. Print All Keys**

Print all the keys present in a dictionary using a loop.

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output:
name
age
city

**Q8. Print All Values**

Print all the values present in a dictionary using a loop.

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output:
Rahul
20
Bhopal

**Q9. Count Key-Value Pairs**

Count the total number of key-value pairs in a dictionary without using len().

**Example:**

- Input: {'a': 10, 'b': 20, 'c': 30}
- Output: 3

**Q10. Calculate the Sum of Values**

Calculate the sum of all numerical values in a dictionary using a loop.

**Example:**

- Input: {'a': 10, 'b': 20, 'c': 30}
- Output: 60
"""


#                                    Dictionary practice sheet :16-10-2026




"""
Q1. Find the Largest Value
Given a dictionary containing numbers, find the largest value without using max().

Example:
Input: {'a': 10, 'b': 25, 'c': 15, 'd': 40}
Output: 40

Q2. Find the Smallest Value
Given a dictionary containing numbers, find the smallest value without using min().

Example:
Input: {'a': 10, 'b': 25, 'c': 5, 'd': 40}
Output: 5

Q3 . Count Even and Odd Values
Count how many values in a dictionary are even and how many are odd.

Example:
Input: {'a': 10, 'b': 15, 'c': 20, 'd': 7}

Output:
Even: 2
Odd: 2

Q4.Sum of Even Values
Find the sum of all even values present in a dictionary.

Example:
Input: {'a': 10, 'b': 15, 'c': 20, 'd': 7}
Output: 30

Q5. Find a Key with a Given Value
Given a dictionary and a value, find the key associated with that value.

Example:
Input: {'a': 10, 'b': 20, 'c': 30}
Value: 20
Output: b

Q6.Update All Values
Increase every value in a dictionary by 5.

Example:
Input: {'a': 10, 'b': 20, 'c': 30}
Output: {'a': 15, 'b': 25, 'c': 35}

Q7.Count Values Greater Than a Number
Count how many dictionary values are greater than a given number.

Example:
Input: {'a': 10, 'b': 25, 'c': 15, 'd': 40}
Number: 20
Output: 2

Q8. Create a Dictionary from Two Lists
Given two lists, create a dictionary where the first list contains keys
and the second list contains values.

Example:
Keys: ['a', 'b', 'c']
Values: [10, 20, 30]

Output:
{'a': 10, 'b': 20, 'c': 30}

Q9.Count Values Equal to a Given Number
Given a dictionary and a number, count how many times that number
appears as a value in the dictionary.

Example:
Input: {'a': 10, 'b': 20, 'c': 10, 'd': 30}
Number: 10
Output: 2

Q10.Count Positive and Negative Values
Given a dictionary containing numbers, count how many values are
positive and how many are negative.

Example:
Input: {'a': 10, 'b': -5, 'c': 20, 'd': -8, 'e': 7}

Output:
Positive: 3
Negative: 2

"""


#                             Set -Tuple practice sheet : 21-10-2026




"""
Q1. Create a Set
Create a set containing 5 numbers and print the set.

Example:
Input: 10, 20, 30, 40, 50
Output: {10, 20, 30, 40, 50}

Q2. Add an Element to a Set
Add the number 60 to the given set.

Example:
Input: {10, 20, 30, 40, 50}
Output: {10, 20, 30, 40, 50, 60}

Q3. Remove an Element from a Set
Remove the number 30 from the given set.

Example:
Input: {10, 20, 30, 40, 50}
Output: {10, 20, 40, 50}

Q4. Check if an Element Exists
Check whether 20 exists in the given set.

Example:
Input: {10, 20, 30, 40}
Output: Element exists

Q5. Find the Length of a Set
Find the number of elements in the given set.

Example:
Input: {10, 20, 30, 40, 50}
Output: 5

Q6. Remove Duplicates from a List
Given a list, remove duplicate elements using a set.

Example:
Input: [1, 2, 2, 3, 4, 3, 5]
Output: {1, 2, 3, 4, 5}

Q7. Create a Tuple
Create a tuple containing 5 numbers and print it.

Example:
Input: 10, 20, 30, 40, 50
Output: (10, 20, 30, 40, 50)

Q8. Access Tuple Elements
Given a tuple, print its first and last element.

Example:
Input: (10, 20, 30, 40, 50)
Output:
First: 10
Last: 50

Q9. Count an Element in a Tuple
Count how many times 20 appears in the given tuple.

Example:
Input: (10, 20, 30, 20, 40, 20)
Output: 3

Q10. Find the Index of an Element
Find the index of 30 in the given tuple.

Example:
Input: (10, 20, 30, 40, 50)
Output: 2

"""



