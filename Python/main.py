# variables 
# number_1 =100
# number1=12
# print(number1)

# 3 data types 
# number 
# a. int -- 1,2,3-1,-2,-8
# name=12625413418848
# print(name)
# # type() 
# # print(type())

# print(type(name))
# # name="aditya"
# # print(name)

# b. float  decimal or p/q
# a=10
# b=5.10
# print(type(b))

# # 3.complex imaginary values are complex numbers 
# a=100j
# print(type(a))

# 2. string anything written inside "" or '' is string
# name="2q3wre4twqfgcdhfukiytghwqsjk!@#$%^"
# print(type(name))

# 3.boolean ->  True or False
# true=True
# b=False
# print(type(true))
# print(b)
# 7 values are falsy value other than these all are truthy values 
# 0,0.0,"",(),[],{},False,None,''
# print(bool(''))   ---> False
# print(bool(0.0))   ---> False
# print(bool([]))   ---> False
# print(bool({}))   ---> False
# print(bool(""))  ---> False
# print(bool(None))  ---> False
# print(bool(()))  ---> False
# print(bool(False)) ---> False

# print(bool("hi")) --> True

# type conversion 
# name="122365"
# print(type(name))
# print(int(name))   

# name="122365.67"
# print(float(name))

# name="a"
# print(bool(name))

# name=True
# print(int(name))


# slicing and indexing 
# indexing 
# s="sheryians"
# print(s[-1])
# print(s[-2])
# print(s[2])
# print(s[4])


# slicing
# s[start index : stop index:step value ]
# s="pythons"
# print(s[::])
# print(s[::-1])

# num=float(input("enter your number : "))
# print(type(num))


# operators
# arithmetic operators 
# +,-,/,*,%,//,**
# a=2
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)


# comparsion operators == , >=,<=,>,<
# a=10
# print(a==10)

# print(a<=20)
# print(a>=20)
# print(a>10)
# print(a<10)

# // --- floor division
# assignment operators 
# +=,-=,*=,/=,//=,%=,**=
# a=10
# a**=2
# print(a)

# logical operators
# and --> if any one of the condition is false it will return false as output otherwise 
# if all are true then only true will be returned as output 
# or -->> if any one of the condition is true then it will return true
#  otherwise all should be false for false as output 
# not --> true ko false and false ko true me convert kr dega 

# print((not(10>20 or 10==10)) or (10>8))

# "f" in python is called fomat string 
name="aditya"
print(f"name is : {name}")
import sys
print(sys.executable)