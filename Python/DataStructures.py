""" 
Data types :
1. Numbers (int ,float , complex )
2. String ("abc")
3.Boolean(True,Fales,(0,1))
"""
#Data Structures
"""
List
1.Square Brakets -->List[]
2.Hetrogenous Data Structures (a list can store different data types together)
3.List allows storing duplicate values.
4.List are ordered - because they have indexing
and indexing starts from 0.
List are Mutable -> we can change any value anytime and anyware. # marks[3] = ModiJi

"""
# marks=[] #empty list
# marks = [80,78,90,65,88,87,75, "Abhishek", 3.14, True,2+1j]
# print([])



#Traversing  -----> select single value and print and again do same
# a = [10,20,30,40,50]
# for i in a :
#     print (i)




"""
Agar kisi line ke aage "."  nahi laga hai to vo function hai. 
Ager "." laga hai to vo Method hai .
"""

#Methods is List 
#1. .append(90) (Add the value at the last list.)
# marks = [10,20,30,40,50]
# marks.append(90)
# print(marks)




# #2. .extend()
# marks2=[70,80,90]
# marks.extend(marks2)
# print(marks)



# marks2=[70,80,90]
# marks2.extend(marks)
# print(marks2)



# 3. .insert(index , value)
# marks.insert (3,90)
# print (marks)

#                                          -----> Class 2 <-----

# 4. .remove()  --> remove any valye from the List. or agar value duplicate hai to first come wali value remove hogi 
# a= [10,20,30,10,40,50]
# a.remove(10)
# print(a)



# 5. .pop() --> remove any value basis of index.
# a= [10,20,30,40,50]
# a.pop(3)
# print(a)



# 6. .clear() --> removes every element and gives empty list.
# a = [10,20,30,40,50]
# a.clear()
# print(a)



# # 7. del --> remove list from the memory, or ye key words is liye "." nahi lagate.
# a = [10,20,30,40,50]
# del a 
# print(a)



# Shallow Copy

# a=[1,2,3,4,5,]
# b=a
# b[3] = 100
# print(a)
# print(b)


# 8. Deep Copy
# a=[1,2,3,4,5,]
# b=a.copy() 
# b[3] = 100
# print(a)
# print(b)



# l = [10,20,30,40,50,60,70,80]

# for i in l:
#     print(i)



# l = [10,20,30,40,50,60,70,80]

# for i in range(len(l)):
#     print(i,l[i])



# l = [10,20,30,40,50,60,70,80]

# for i in range(len(l)-1,-1,-1):
#     print(i,l[i])

"""
l = [10,20,30,40,50,60,70,80]
l_2 =[]

for i in range(len(l)-1,-1,-1):
    l_2.append (l[i])
print(l_2)    



l = [10,20,30,40,50,60,70,80]
l_2 =[]

for i in range(len(l)-1,-1,-1):
    l_2.insert(len(l_2),l[i])
print(l_2) 
"""


#                                           -----> Class 3 <-----
"""
DICTIONARY
1. Dictionary annoted by {Curly brackets}.
2. Dictionary are combination of multiple Keys:Values.
3. Dictionary are Mutable.
4. Dictionary are Hetrogenious.
5. In Dictionary Keys will be unique but values can be Duplicate.
6. Dictionary are ordered.
7. Whenever use dictionary in loop we get keys.

"""

# d = {1:10, 2:20, 3:30}
# print(d[3])


# d = {1:10, 2:20, 3:30}
# d[3] = 100                                       # Mutable
# print(d)


# d = {1:10, 2:20, 3:30}
# d[4] = 100 #      creating a  new key : values pair which never exists.
# print(d)


# d = {1:10,2:20,3:30}
# for i in d:
#     print(i, d[i])



"""
SETS
1. Sets are annoted by {} or set().
2. Stores only unique elements and removes duplicate ones. 
3. Sets are unordered that means there is no indexing in sets.
4. Sets are Hetrogenous. 
5. Sets are Semi-Mutable. 

"""

# s = {}
# s = set() #   EMPTY SET
# print(type(s))


#List to set
# l =[1,1,2,3,4,5]
# print(set(l))

"""

Sets Method

"""

# 1. .add () -> adds an element to set 
# s = {1,2,3,4}
# s.add(5)


# 2. .remove () -> remove an element if the element didn't exists we will get an 
# KEY - ERROR 
# s.remove(100)
# print(s)


 
# 3. .discard () -> Will not show any error if the element is not present in set.
# s.discard(100) 
#print(s)



"""
SET OPERATIONS


"""

# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}


#1. .Union()
# Merge both the sets

# print(f"UNION -> {s1.union(s2)}")

# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f"Union -> {s1|s2}")



#2. INTERSECTION
#Common elements.

# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f"INTERSECTION -> {s1.intersection(s2)}")


# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f"INTERSECCTION -> {s1 & s2}")

#3. .difference 
# elements present in one set but not in other set

# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f" Difference -> {s1.difference(s2)}")
# print(f" Difference -> {s2.difference(s1)}")

# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f"DIFFERENCE -> {s1 - s2}")

#4. .symmetric_difference ()

# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f"symmetric -> {s1.symmetric_difference(s2)}")

# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f"Symmetric -> {s1 ^ s2}")



"""
| -> UNION
& -> INTERSECTION
- -> DIFFERENCE
^ -> SYMMETRIC

"""


# Frozenset  makes any set with of fixed  elements
#  we cannot add element and we cannot remove one.
# s = frozenset([1,2,3,4,5])
# s.add(6)
# print(s)

#                                                           -----------> Class 4 <-----------

"""
TUPLE
1. Annoted by (Paranthesis)
2. Tuples are ordered.
3. tuples are Immutable.
4. Tuples can store duplicate values.
5. Hetrogenous -> can store mixed type of data.
"""

#t = ()# Empty Tuple 

# t =(1,2,[3,4])
# t[2][1] = 100
# print(t)



"""
Methods In TUPLE
1. .index() -> return index of any value.
2. .count() -> count occurence of any value.
3. .

"""

# t = (1,1,2,3,4,1,)
# print(t.count(1))







"""
OPERATIONS

+ -> concatenation 
* -> Repetition
"""

# t1 = (1,2)
# t2 = (3,4)
# print(t1 + t2)


# t1 = (1,2)
# t2 = (3,4)
# print(t1 * 5)

# # Put 100 in end of list in tuple
# t = (1,2,[3,4,5])
# t[2].append(100)# print ke andar nahi likh sakte kyu ye class hai        
# print(t)


# t = (1,2,3,4,5)
# for i in range (len(t)):
#     print(i,t[i])



# t = (1,2,3,4,5)
# print(t[::-1])
    





# print((1,2)*2 +(3,))

    





