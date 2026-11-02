#                                               -----> Class 1 <-----
"""
# Q1. Count Numbers Divisible by Both 3 and 5
#
# Take an integer N as input and count how many numbers from 1 to N
# are divisible by both 3 and 5 (multiples of 15).
#
# Example:
# Input: 35
# Output: 2
# (Explanation: The numbers are 15 and 30. Total count = 2)
"""



# n = int(input("enter the number")) 
# count = 0
# #  1 -> N+1
# for i in range(1,n+1):
#     if i % 3 ==0 and i%5==0:
#         count+=1
# print(f"count : {count}")
        
    














"""
# Q2. Factorial of a Number
#
# Take an integer N as input and 
# calculate its factorial.
# Factorial of N (N!) is the
# product of all positive integers from 1 to N.
# (0! = 1, 5! = 5 * 4 * 3 * 2 * 1 = 120)
#
# Example:
# Input: 5
# Output: 120
"""
# n = int(input("enter the num"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print(f"{n}! is {fact}")










"""
# Q3. Check Strong Number 
#
# Take an integer N as input and
# check whether it is a Strong Number.
# A Strong Number is a number
# whose sum of factorials of its
# digits equals the original number.
#
# Example:
# Input: 145
# 1! = 1
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# Sum: 1 + 24 + 120 = 145
# Output: Strong Number
"""

n = int(input("enter the number"))
temp = n
sum = 0
while n >0:  
    digit = n%10
    # digit!
    fact = 1
    for i in range(1,digit+1):
        fact*=i
    sum +=fact
    n = n//10
if temp == sum:
    print("strong number")
else:
    print("not a strong number")
    
    
    
    
    
    













"""
# Q4. Sum of Odd Numbers from 1 to N
#
# Take an integer N as 
# input and calculate the sum of all odd numbers from 1 to N.
#
# Example:
# Input: 10
# Output: 25
# (Explanation: 1 + 3 + 5 + 7 + 9 = 25)
"""

n = int(input("enter the number"))

sum = 0
for i in range(1, n+1):
    if i %2!=0:
        sum+=i
print(f"sum of odd numbers from 1 to {n} is {sum}")





#                                               Class 2

#                                            loopspractice(1)     


"""
# Q5. Print Fibonacci Series up to N Terms
#
# Take an integer N as input and print the first N terms of the Fibonacci series.
# In Fibonacci series, each number is
# the sum of the previous two numbers (starts with 0, 1).
#
# Example:
# Input: 6
# Output:
# 0 1 1 2 3 5
"""

n = int(input("enter the number "))
a = 0
b =1

for i in range(n):
    print(a , end =" ")
    c = a+b
    a =b
    b =c
 
    









"""
# Q6. Count Vowels in a String
#
# Take a string as input 
# and count how many vowels (a, e, i, o, u) are present in it.
# Check both lowercase and uppercase 
# vowels without using any string functions.
#
# Example:
# Input: "AbhiSHEK"
# Output:
# Total vowels: 3  (A, i, E)
"""

text = input("enter the  text")
# AbhiSHEK
count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count +=1
print(f"total vowels : {count}")
    










"""
# Q7. Count Occurrences of a Character in a String
#
# Take a string and a target 
# character as input from the user.
# Count how many 
# times that character appears in the string using a loop.
# (Do not use any built-in functions)
#
# Example:
# Enter string: banana
# Enter character to search: a
# Output:
# 'a' appears 3 times
"""

text = input("enter the string ")
target = input("enter a character")
count = 0
for ch in text:
    if ch == target:
        count+=1
print(count)













#                                  ----------> Class 3 <---------- 
#                                          loopspractice(2)




"""
# Q8. Print All Numbers Ending with 7 from 1 to N
#
# Take an integer N as input and 
# print all numbers from 1 to N that end with the digit 7.
#
# Example:
# Input: 40
# Output:
# 7 17 27 37
"""
# write a function of this code and return me list
# return 
# list [] 
# append 


n = int(input("Enter the number"))
for i in range(1,n+1):
  if i%10==7:
    print(i , end=" ")



# result = []
# def numbers_ending_with_7(n):
#     for i in range (1,n+1):
#         if i%10==7:               #-----> result pehle likhne se store data nahi hatega, isliye function me likhna padega<-----
#             result.append(i)
#     return result

# n = int(input("Enter the number"))
# print(numbers_ending_with_7)
# m = int(input("Enter the number"))
# print(numbers_ending_with_7)        




def numbers_ending_with_7(n):
    result = []
    for i in range (1,n+1):
        if i%10==7:               #-----> (Right way) Isliye function me likhna padega<-----
            result.append(i)
    return result

n = int(input("Enter the number"))
print(numbers_ending_with_7)
m = int(input("Enter the number"))
print(numbers_ending_with_7)

    
    

        






"""
# Q9. Check Harshad (Niven) Number

# Take an integer N as input and 
# check whether it is a Harshad Number.
# A Harshad number is a number 
# that is completely divisible by the sum of its digits.
#
# Example 1:
# Input: 18  -> Sum of digits: 1 + 8 = 9 -> 18 % 9 == 0
# Output: Harshad Number
#
# Example 2:
# Input: 14  -> Sum of digits: 1 + 4 = 5 -> 14 % 5 != 0
# Output: Not a Harshad Number
"""
n = int(input("enter the number"))
temp = n
sum =0
while n >0:
    digit = n %10
    sum +=digit  
    n = n //10
if sum > 0  and temp % sum == 0:
    print("harshad number")
else:
    print("Not a harshad number")












#                                                       -----> Online class 4 <-----
#                                                              loopspractice



"""
# Q10. Digit Frequency

# Take an integer N as input and count how many times
# each digit from 0 to 9 occurs in the number.
#
# Example:
# Input: 122333
#
# Output:
# 1 -> 1
# 2 -> 2
# 3 -> 3

"""



n = int(input("Enter the number: "))

for digit in range (0,10):
    temp = n
    count_digit = 0

    while temp > 0:
        last_digit = temp%10  
        if last_digit == digit:
            count_digit +=1
        temp //=10
    if count_digit > 0:
        print(f"{digit} -> {count_digit}")        












"""

# Q11. Find the Smallest Digit in a Number
#
# Take an integer N as input
# and find the smallest digit present in it.
#
# Example:
# Input: 64825
# Output: 2

"""



n = int(input(" Enter the number "))
temp = n
smallest = 9
while temp > 0:
    digit = temp%10
    if digit < smallest:
        smallest = digit
    temp //=10 
print(f"chota digit in {n} is {smallest}")       










#                                                         -----> Class 5 <-----
#                                                              loopspractice(2)





"""
# Q. ATM Machine Simulation
#
# Write a Python program to simulate an ATM machine with the following rules:
#
# 1. PIN Verification:
#    - Default correct PIN is 1234.
#    - User gets a maximum of 3 attempts to enter the correct PIN.
#    - If entered incorrectly 3 times, print "Card Blocked! Please contact your bank." and terminate.
#
# 2. Main Menu (runs continuously until user exits):
#    - Initial Account Balance = ₹5000. 
#    - If PIN is correct, show the menu options:
#        1. Check Balance
#        2. Deposit Cash
#        3. Withdraw Cash
#        4. Exit
#
# 3. Operations:
#    - Option 1: Display the current balance.
#    - Option 2: Ask for deposit amount, add it to balance, and display updated balance.
#    - Option 3: Ask for withdrawal amount.
#                If amount <= balance, deduct and print "Withdrawal Successful".
#                Otherwise, print "Insufficient Balance!".
#    - Option 4: Print "Thank you for using our ATM. Have a nice day!" and exit the loop.
#    - Any other option: Print "Invalid Choice! Please choose 1 - 4."
"""

"""
user ki attemps ke ander pin check krna hai 
user se pin check krna hai in limits -> pin_real == pin_input
-> incorrect
-> 1st time and 2nd and -> pin is incorrect -> chance dena again
-> 3rd time -> incorrect -> card blocked chor ho appp
1st and 2nd and 3rd ->correct -> main menu and chance stop 
main menu (1,2,3,4)
balance = 5000 +1000-2000

""" 


# input should be taken when user have left out attempts
attempts =3
has_access_mainmenu = False
""" this logic is for checking wheather user have entered pin correct or not"""
while attempts > 0:
    entered_pin = int(input("enter the pin"))
    if entered_pin == 1234:
        # main menu openes
        has_access_mainmenu = True
        break
    else:
        attempts -=1
        if attempts>0:
            print(f"incorrect pin! you have {attempts} attempts remaining")
        else:
            print("card blocked")
            
balance = 50000
if has_access_mainmenu == True:
    while True:
        print("ATM Menu")
        print("1 -> check balance")
        print("2 -> deposit cash")
        print("3-> withdraw cash")
        print("4->exit")
        
        choice = int(input("enter the choice"))
        
        if choice == 1:
            print(f"Balance is {balance} only")
        elif choice ==2:
            depoist_amount = int(input("enter the ammount to deposit"))
            if depoist_amount > 0:
                balance +=depoist_amount
                print(f"updated balance is {balance}")
            else:
                print("invalid depoist ammount")
        elif choice ==3:
            withdraw_ammount = int(input("enter the ammount to withdraw"))
            if withdraw_ammount <=balance:
                balance-=withdraw_ammount
                print(f"withdraw done and updated balance is {balance}")
            else:
                print("insufficient balance")
        elif choice ==4:
            print("thank you for using our atm")
            break
        else:
            print("invalid choice ! please enter number from 1 - 4")
            

            