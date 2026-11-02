"""While Loops 
kaha jana hai---> kab tak jana hai ---> kaise jana hai
while jab tak ye condition true hai:
tab tak yeh code chalega"""

""" Q1. 1 to 50 tak print karna hai using while loop

i =1
while i<=50:
    print(i)
    i=i+1 """






""" Q2. 10 to 1 tak print karna hai using while loop
i =10
while i>=1:
    print(i)
    i=i-1 """





""" Q3. User se password mangte raho jab tak sahi password "Abhishek123nahi mil jaye. """

password=""
while password!="Abhishek123":
        password=input("Enter your password ")
        print("Wrong password")
print("Access granted")


#Take N as a input and print a table.

# n=int(input("Enter a table "))

# i=1
# while i<=10:
#     print("n*i")
#     i=i+1

#Print even number from 2 to 20

# i=2
# while i<=20:
#     if i%2==0:
#      print(i)
#      i=i+2
   
#Print sum of even number from 2 to 20

# i=2
# sum=0
# while i<=20:
#      print(i)
#      sum=sum+i
#      i=i+2
# print(f"Sum of even numbers from 2 to 20 is {sum}")



#Print a number in reverse order 
# % --> Last digit ko print karana
# // --> Last digit ko parmanent remove karna

# n=1234
# while n!=0:
#     print(n%10)
#     n=n//10

#one more mathod to print a number in reverse order

# n=1234
# a=0
# while n>0:
#     last=n%10
#     a=a*10+last
#     n=n//10
# print(a) 
   
"""n=1234
a=0
count=0
while n>0:
    last=n%10
    a=a*10+last
    n=n//10
    count=count+1
print(a)    
print(count)    """

#            Class 2
""" Q1. Number is Armstrong or not

n=135
sum=0
temp=n
length=len(str(n))

while n > 0:
    last = n%10
    sum = sum + last ** length
    n = n//10

if sum == temp:
   print(" The number is Armstrong")    
else:
    print("The number is not Armstrong") """







