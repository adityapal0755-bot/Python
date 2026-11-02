#                                                        -----> First test <----- 


""" 1. **Prime Numbers from 1 to N (10 marks)**
    
    Take a positive integer N as input and print all prime numbers from 1 to N (inclusive). 
    
    Note: 1 is not a prime number.
    
    **Example:** Input: 10 → Output: 2, 3, 5, 7 """

n = int(input(" Enter your number: "))
count = 0
for i in range (1,n+1):
    if n % i == 0:
        count += 1
    if count == 2:
        print (i)

      





    
""" 2. **Strong Number (10 marks)**
    
    Given a non-negative integer, check whether it is a Strong number. The sum of the factorials of its digits must equal the original number.
    
    **Example:** Input: 145 → Output: Strong Number (1! + 4! + 5! = 145)
    """
""" 3. **Armstrong Number (10 marks)**
    
    Given a non-negative integer, check whether it is an Armstrong number. Raise each digit to the power equal to the number of digits, then check whether the sum equals the original number.
    
    **Example:** Input: 153 → Output: Armstrong Number (1³ + 5³ + 3³ = 153)
    """

""" 4. **Second Largest Digit (10 marks)**
    
    Take an integer N as input and find the second largest distinct digits present in the number.
    
    Example: Input: 58382
    
    Output: Second Largest: 5
    
     Check Palindrome Number
    
n = int ( input (" Enter your number: "))
temp = 0
lar_num = 0
while n > 0:
    for i in range (1,2):
        temp = temp * 10 + n % 10
        n = n // 10
    if temp > n:
        lar_num += temp
    else:
        lar_num += n    
print(n)        
print(lar_num)"""
    






""" #### 5. Check palindrome number (10 marks)

        Take an integer N as input and check whether 
        the number remains the same when its digits               
        are reversed.

      Example:
      Input: 121

      Output : Palindrome

n = int(input("Enter your number: "))
temp = n
rev = 0

while n != 0: 
    rev = rev * 10 + n % 10 # Doubt-----> Yaha pe rev*10 kyu liya hai ?
    n = n//10
print(rev)
if rev == temp:   
    print("Palindrome")
else:
    print("Not a Palindrome")     """
      






