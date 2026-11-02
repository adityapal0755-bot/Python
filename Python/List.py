#                                                  -----> Class 1 <-----
#                                                          list
"""
# Print List Elements in Reverse Order
#
# Reverse the list using the two-pointer approach.
#
# Example:
# Input: [10, 20, 30, 40, 50]
# Output: [50, 40, 30, 20, 10]
"""

# arr = [10, 20, 30, 40, 50]
# n = len(arr)
# mid = n//2
# for i in range(mid):
#     arr[i] , arr[n-i-1] = arr[n-i-1] ,arr[i]






"""
# Print Positive and Negative Elements of a List
#
# Print positive and negative elements separately.
# Ignore zero.
#
# Example:
# Input: [10, -5, 20, -3, 0, 8][10, -5, 20, -3, 0, 8]
# Output:
# Positive: 10 20 8
# Negative: -5 -3
"""
# arr = [10, -5, 20, -3, 0, 8]

# print("positive:")
# for elem in arr:
#     if elem>0:
#         print(elem)
        
# print("negative: ")
# for elem in arr:
#     if elem<0:
#         print(elem)
        








"""
# Mean of List Elements
#
# Calculate the average of all elements in a list.
#
# Example:
# Input: [10, 20, 30, 40]
# Output: Mean = 25.0
"""


# list = [10, 20, 30, 40]
# n = len(list)
# sum =0
# for elem in list:
#     sum+=elem
# print(f"mean is {sum/n}")
    









"""
# Find the Greatest Element and Its Index
#
# Find the greatest element and 
# print its index.
#
# Example:
# Input: [2, 96, 69, 77, 145, 20]
# Output: Max element = 145 
# found at 4 index
"""
# arr =[2, 96, 69, 77, 145, 20]
# max = arr[0]
# index =0
# for i in range(1,len(arr)):
#     elem = arr[i]
#     if elem > max:
#         max = elem
#         index = i
    
# print(f"max is {max} at index {index}")
    











"""
# Find the Smallest Element and Its Index
#
# Find the smallest element and print its index.
#
# Example:
# Input: [2, 96, 69, 77, 145, 20]
# Output: Min element = 2 found at 0 index
"""




"""
# Sum of List Elements
#
# Accept N elements and print their sum in the given format.
#
# Example:
# Input: [10, 20, 30]
# Output: 10 + 20 + 30 = 60
"""





"""
# Find the Second Greatest Element
#
# Find the second-greatest distinct element.
#
# Example:
# Input: [2, 96, 69, 77, 145, 20]
# Output: Second greatest element = 96
"""




"""
# Check Whether a List Is Sorted
#
# Check if the list is sorted in ascending order.
#
# Example:
# Input: [10, 20, 30, 40, 50]
# Output: List is Sorted
"""





"""
# Palindromic List
#
# Check whether the list reads the same forwards and backwards.
#
# Example:
# Input: [2, 3, 15, 15, 3, 2]
# Output: Palindromic List
"""



#                                        -----> Class 2 <-----

#                                                list2





"""
 Q1. Find the missing number 

A list contains numbers from 1 to N, but one number
is missing. Write a program to find the missing number.

Example:
Input: [1, 2, 4, 5]

Output:
Missing Number = 3 
"""

# arr = [1,2,4,5]
# n = len(arr)
# og_n = n+1
# og_sum = ((og_n)*(og_n+1))//2
# real_sum = 0
# for elem in arr:
#     real_sum += elem

# missing = og_sum - real_sum
# print(missing)










"""
Q2. Check whether a list is sorted or not 
Check if the list elements are arranged in ascending order.
 
Example: 
input:[10,30,20,40,50]
Output: 
"""
# arr = [10,30,20,40,50]
# is_sorted = True
# n = len(arr)
# for i in range (0,n-1):
#     if arr[i]>arr[i+1]:
#         is_sorted = False
#         break

# if is_sorted:
#     print("List is shorted")
# else:
#     print("List is unsorted")        











"""
Q3. Palindrome List

Check whether the list reads the same from front and back.

Examples:

Input:[2,3,15,15,3,2]

Output:Palindrome List

"""
# arr = [2, 3, 15, 15, 3, 2]
# n = len(arr)
# is_palindrome = True


# for i in range(n//2):
#     if arr[i] !=arr[n-i-1]:
#         is_palindrome = False
#         break
# if is_palindrome:
#     print("palindrome")
# else:
#     print("not a palindrome")












"""
Q.4 Find the Pair with the Given Sum
#
# Find all pairs of elements whose sum equals a given target.
#
# Example:
# Input: [2, 4, 3, 5, 7, 8]
# Target: 10
#
# Output:
# (2, 8)
# (3, 7)
"""












#                                                     -----> Class 3 <-----
#                                                             list3





"""
Q5. Sort a List in Ascending Order

Write a Python program to sort the elements of a list in
ascending order without using the built-in sort() method.

Example:
Input:  [64, 34, 25, 12, 22, 11, 9]
Output: [9, 11, 12, 22, 25, 34, 64]
"""
 

# arr = [64,34,25,12,22,11,9]
# n = len(arr)

# for i in range (n):
#     for j in range (n-i-1): # isko (n-i-2+1) bhi likh sakte hai
#         if arr[j] > arr [j+1]:
#             arr[j] , arr[j+1] = arr[j+1] , arr[j]

# print(arr)            








"""
# Find the Pair with the Given Sum
#
# Find all pairs of elements whose sum equals a given target.
#
# Example:
# Input: [2, 4, 3, 5, 7, 8]
# Target: 10
#
# Output:
# (2, 8)
# (3, 7)
"""

# arr = [2, 4, 3, 5, 7, 8]
# target = 10
# n = len(arr)
# for i in range(n):
#     for j in range(i+1, n):
#         if (arr[i] + arr [j]) == target:
#             print(arr[i],arr[j])






"""
Question: Rotate a List to the Right by K Positions

Write a Python program to rotate a list to the right by K positions
using a loop.

Example:
Input:
arr = [1, 2, 3, 4, 5]
k = 2

Output:
[4, 5, 1, 2, 3]
"""






"""
Question: Check Whether a List Is a Sublist of Another List

Write a Python program to check whether all elements of one list
appear consecutively in another list.

Example:
Input:
arr = [10, 20, 30, 40, 50]
sub = [20, 30, 40]

Output:
Sublist Found
"""
# arr =[10, 20, 30, 40, 50]
# n = len(arr)
# sub =[20, 30, 40]
# m = len(sub)
# for i in range(0,n-m+1):
#     if arr[i:i+m] == sub:
#         print("sublist found")
#         break
# else:
#     print("not sublist found")





#                                                    ----------> Class 4 <----------

#                                                                List4




"""
Question: Rotate a List to the Right by K Positions

Write a Python program to rotate a list to the right by K positions
using a loop.

Example:
Input:
arr = [1, 2, 3, 4, 5]
k = 2

Output:
[4, 5, 1, 2, 3]
"""
# arr = [1, 2, 3, 4, 5]
# k =2
# k = k%len(arr)
# for i in range(k):
#     last = arr.pop()
#     arr.insert(0,last)
# print(arr)








"""
Question: Find All Duplicate Elements

Write a Python program to find all elements that appear more than
once in a list. Print each duplicate element only once.

Example:
Input:  [1, 2, 3, 2, 4, 1, 5]
Output: [1, 2]
"""
# arr =[1,2,3,2,4,1,5]
# n = len(arr)
# dup = []
# for i in range(n):
#     count = 1
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             count+=1
#     if count >=2:
#         dup.append(arr[i])
        
# print(dup)






#                                                       ----------> online Class 5 <----------


#                                                                      List5
"""

Question: Merge Two Sorted Lists Without Using sort()

Write a Python program to merge two sorted lists into a single
sorted list without using the sort() function or any Sorting Algo.

Example:
Input:
arr1 = [1, 4, 7, 10]
arr2 = [2, 3, 8, 9]

Output:
[1, 2, 3, 4, 7, 8, 9, 10]

"""


# arr1 = [1,4,7,10]
# arr2 = [2,3,8,9]

# n1 = len(arr1) 
# n2 = len(arr2)

# i=0
# j=0
# ans=[]
# while i < n1 and j < n2:
#     if arr1[i] < arr2[j]:
#         ans.append(arr1[i])
#         i+=1
#     else:
#         ans.append(arr2[j])
#         j+=1
# while i < n1:
#         ans.append(arr1[i])
#         i+=1
# while j < n2:
#     ans.append(arr2[j])
#     j+=1
# print(ans)        










#                                                       ----------> online Class 6 <----------
#                                                                    ques2.py






"""
Question: Find Duplicate Words in a Sentence

Find all words that appear more than once.
Ignore uppercase and lowercase differences.

Input:
"Python is easy and python is powerful and easy"

Output:
['python', 'is', 'easy', 'and']
"""
sen = "Python.is.easY.and.python.is.powerfuL.and.Easy"
sen = sen.lower()
# print(sen)
words = [] 
# words = sen.split(" ") # Ye kar sakte hai easy wala -> words [ ] ke jagha
# # word =""

# for ch in sen:
#     if ch!=".":
#         word+=ch
#     else:
#         words.append(word)
#         word =""
# words.append(word)
# print(word)
# print(words)

# ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful', 'and' ,'easy]
dup = []

for i in range(len(words)):
    count =0
    for j in range(len(words)):
        if words[i] == words[j]: # List ko set me bhi convert kar sakte hai dupilicate hatane ke liye magar orderd nahi ayega kyuki sets orderd nahi hota hai 
            count +=1
    if count>=2 and words[i] not in dup:
        dup.append(words[i])
print(dup)
    








#                                                       ----------> online Class 7 <----------
#                                                                    ques3.py


"""
Question: Group Words of a Sentence by Their Length

Given a sentence, group all unique words by their length into a
dictionary. Ignore uppercase and lowercase differences.

Example:
Input:  "Eat sleep code and repeat code and eat clean"
Output: {3: ['eat', 'and'], 5: ['sleep', 'clean'], 4: ['code'], 6: ['repeat']}
"""

sen = "Eat sleep code and repeat code and eat clean"
res = ""
for ch in sen:
    if  ord('a') <= ord(ch) <=ord('z'):
        res += chr(ord(ch)-32)
    else:
        res +=ch
print(res)
        





# ans = {}
# words = sen.split(" ")
# for word1  in words:
#     l = len(word1)
#     temp = []
#     for word2 in words:
#         if  len(word2) == l and word2 not in temp:
#             temp.append(word2)
#     ans[l] = temp
# print(ans)

