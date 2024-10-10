# name = "bjn"
# print(name)
# import csv

# #procedural

# def greetName(name):
#     print("hii  "+name)

# def calculateSum(a,b):
#     return a+b

# name = input("enter your name:")
# greetName(name)
# num1 = int(input("enter the first number:"))
# num2 = int(input("enter the second number:"))
# print(calculateSum(num1,num2))

#functional
# def Square(x):
#     return x*x

# sq_number=Square(4)
# print(sq_number)
#object oriented
# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def Bark(self):
#         print("baaark!!!!!")

# mydog = Dog("buddy",5)
# # print({mydog.name} +"his age" +{mydog.age}+" is sounds ")
# print(f"{mydog.name} is {mydog.age} years old.")
# mydog.Bark()

# x=10
# x="name"
# x=[3,4,5,6]
# print(x)
# x,y,z = "python",78,[89,56,"jhjh"]
# print(x,y,z)

#local variable scope
# def my_func():
#     loc_Var = "seee"
#     print(loc_Var)
# my_func()

# #enclosing scope
# def outerFun():
#     outer_var="mous"
#     def innerFunc():
#         print(outer_var)
#     innerFunc()
# outerFun()

# p=True
# q=False
# print( not q)
# my_list = [2,3,5,7]
# print(3 not in my_list)
# a = [1, 2, 3]
# b = a
# print(a is b)
# p=5
# q=3

# print(p | q)
# set ={1,2,3}
# set.add(4)
# print(set)
# my_dict = { 'age': 30, 'city': 'London'}
# print(my_dict['name'])
# print(my_dict.get('name'))
# bol_val=3.14
# print(int(bol_val))


# a=1,2,3,4
# n1=100
# n2=False
# res=n1**n2
# print(res)

# ls1=[1,2,3]
# ls2 =[1,2,3,False]
# print(ls1==ls2)
# print(ls1>ls2)
# print(ls1<ls2)
# print(100 or "a")
#ls=["python",23,45]
# ls="python"
# ls={"name":"rajesh","age":67,"salary":75657}
# n1=10
# n2=21
# print(n1//n2)
# n1=(1,)
# n2=()
# print(id(n1))
# print(id(n2))
# print(n1==n2)
# n=2
# print(bin(n))
# a=[2,3,4]
# b=a
# print(a is b)
# print(a is not b)
# a=[]
# b=[]
# print(a is b)
# print(id(a))
# print(id(b))
# print(a==b)
# x= 10
# print(x)
# del x
# print(x)
# str=""
# str1=""
# print(id(str))
# print(id(str1))
# for x in range(-25, -5):
#     print(x)

# ls1=[2,3,5,2]
# for x in ls1:
#     print(ls1.count(x))
#Doubt
# print(10 and 5)
# print(5 and 10)
# print(5 and 10)
#print(bin(65))
# print(1 and 0)
#
# print("A" and "a")
# print("a" and "A")
# print("AA" and "aaa")
# print(dir(list))
# print(10 and "a")
# print("a" & 10)
# print(100 and [100])
# print([100] and 100)
# print(10 or 5)
# print(5 or 10)
# print("a" or "A")
# print("A" or "a")
# print(10 or "a")
# print("a" or 10)

# x=y=z= 10
#
# print(id(x))
# print(id(y))
# print(id(z))
# x, y, z = "pyt"
# print(x)
# print(y)
# print(z)
# print(id(x))
# print(id(y))
# print(id(z))
# n1 = "100"
# n2 = False
# res = n1 ** n2
# print(res)

# print(not 3)
# a = []
# b = []
# print(a is b)
# print(id(a))
# print(id(b))
# print(a==b)
# Flatten a list
# ls = [1,3,20,[3,4,5],56,[18,12,3,[5,6,8]]]

# def flatten(ls_input):
#     result = []
#
#     for item in ls_input:
#         if isinstance(item, list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result
#
#
# ls = [1, 3, 20, [3, 4, 5], 56, [18, 12, 3, [5, 6, 8]]]
# print(flatten(ls))

# def flatten(input,output):
#     for x in input:
#         if type(x) == list:
#             return flatten(x, output)
#         else:
#             output.append(x)
#
#     print(output)
#
# ls = [1, 3, 20, [3, 4, 5], 56, [18, 12, 3, [5, 6, 8]]]
# result = []
# flatten (ls ,result)
# print()

# def flatten (data):
#     result = []
#     for item in data:
#         if isinstance(item, list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result
#
#
# ls = [1, 3, 20, [3, 4, 5], 56, [18, 12, 3, [5, 6, 8]]]
# print(flatten(ls))

#Program to print half pyramid using *

# row=6
# aski =65
# for i in range(row):
#     for j in range(i+1):
#         alp= chr(aski)
#         print(alp,end="")
#     aski +=1
#     print()

#row =6
# for i in range(row,0,-1):
#     for j in range(0,i):
#         print("*",end="")
#     print()

# rows = 3
#
# k = 0
# count = 0
# count1 = 0
#
# # for i in range(rows):
# #     for j in range(rows):
# #         print(count,end=" ")
# #         count+=1
# #     # print()
# row =4
# k=0
# for i in range(1, rows+1 ):
#     print("i",end=" ")
#     for space in range(1, (rows - i)+1):
#         print("x",end="  ")
#
#     while k != (2 * i - 1):
#         print(k, end=" ")
#         k += 1
#
#     k = 0
#     print()

#sorting without sort() method
# ls=[23,4,1,5,45]
# #4,1,5,45
# for x in range(len(ls)):
#     for y in range(x+1,len(ls)):
#         if(ls[x]>=ls[y]):
#             tmp = ls[x]
#             ls[x] =ls[y]
#             ls[y] =tmp
# print(ls)

# Binary search

# def BinarySeach(arr,target):
#
#     #sort the array
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if(arr[i]>=arr[j]):
#                 tmp = arr[i]
#                 arr[i]=arr[j]
#                 arr[j]=tmp
#     print(arr)
#
#     low = 0
#     high = len(arr)-1
#     mid =0
#     while low<=high:
#         mid = high+low//2
#         #print(mid)
#         if arr[mid] > target:
#             high = mid-1
#         elif arr[mid]<target:
#             low = mid+1
#         else:
#             return mid
#     return -1
#
#
#
# ele = 12
# ls =[3,23,7,5,9,12]
# print(BinarySeach(ls,ele))

# str ="hello hello word"
# ls=str.split(" ")
# ds ={x:ls.count(x) for x in ls}
# print(ds)


# collatz Sequence

# num = int(input("enter the number :"))
#
# while num!=1:
#     print(num,end=" ")
#     if num%2!=0:
#         num=3*num+1
#     else:
#         num=num//2
#
# print(num)

# fibonacci

# num = int(input("enter the number :"))
# a=0
# b=1
# count=0
#
# while(count<num):
#     print(a,end=" ")
#     res=a+b
#     a=b
#     b=res
#     count = count+1

# prime number sequence between (10, 50)

# l=10
# up=50
# for num in range(2,up+1):
#     for i in range(2,num):
#         if num%i == 0:
#             break
#     else:
#         print(num,end=" ")

# Transpose of a matrix A

# A=[[1,2,3],[4,5,6]]
# #A^T
# AT = [[0 for i in range(len(A))] for j in range(len(A[0]))]
#print(AT)


# for i in range(len(A)):
#     for j in range(len(A[0])):
#         AT[j][i] = A[i][j]
# print(AT)

# i = 0
#
# while i < len(A):
#     j = 0
#     while j < len(A[0]):
#         AT[j][i] = A[i][j]
#         j += 1
#     i += 1
# print(AT)


#pattern matching
# count =0
# row=5
# for i in range(row):
#     for k in range(row-i):
#         print(" ", end=" ")
#
#
#
#     for j in range(2*i-1):
#         print(i,end=" ")
#
#     print()
# row=5
# for i in range(row):
#     a=0
#     for j in range(row+i):
#         if i+j>= row-1:
#             if j>row-1:
#                 a=a-1
#                 print(a, end=" ")
#             else:
#                 a = a + 1
#                 print(a,end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# row =4
#
# for i in range(row):
#     a=0
#     k=0
#     for j in range(row+i):
#         if i+j>row:
#             if j>row:
#                 a=a-1
#                 print(a,end=" ")
#             # if i>row and j<row:
#             #     #j=j-1
#             #     print(a,end=" ")
#             else:
#                 a = a+1
#                 print(a,end=" ")
#         else:
#             print(" ",end =" ")
#
#     print()


# k=0
# n=0
# for i in range(1, row + 1):
#     for j in range(1, k + 1):
#         print(end=" ")
#     k = k + 1
#
#     while n <= (row - i):
#         print("*", end=" ")
#         n = n + 1
#     n = 0
#     print()

# row=3
# for i in range(row):
#     a=0
#     for j in range(row+i):
#         if i+j>= row-1:
#             #print("x",end=" ")
#              if j>row-1:
#                 a=a-1
#                 print(a, end=" ")
#             # if(i+j==row-1):
#             #     print("x")
#             #  # elif i>row-1 and j<row-1:
#             #  #     if i+j==row-1:
#             #  #         print("x")
#             #  #     else:
#             #  #
#             #  #        print(" ",end=" ")
#
#              else:
#                  a = a + 1
#                  print(a,end=" ")
#
#         else:
#             print(" ",end=" ")
#     print()

# row=3
#
# for i in range(1, row+1):
#     a=0
#     for j in range(1,row-i+1):
#         print(" ", end=" ")
#     for j in range(1, 2*i):
#         if j<=row:
#             a=a+1
#             print(a,end=" ")
#         else:
#             a-=1
#             print(a, end=" ")
#         #print(" ", end=" ")
#     print()
#
#
# for i in range(row-1,0, -1):
#     a=0
#     for j in range(1,row-i+1):
#         print(" ", end=" ")
#     for j in range(1, 2*i):
#         if j<row:
#             a+=1
#             print(a, end=" ")
#         else:
#             a-=1
#             print(a,end=" ")
#     print()
#

#Strong Number

# def Strong_Num(num):
#     sum = 0
#     tmp_num =num
#     while tmp_num>0:
#         fact = 1
#         rem = tmp_num%10
#         for i in range(1,rem+1):
#             fact =fact*i
#         sum += fact
#         tmp_num =tmp_num//10
#
#     if num == sum:
#         return "strong Number"
#     else:
#         return "number is not strong"
#
#
# n = int(input("enter the number :"))
# print(Strong_Num(n))

#prime number

# n = int(input("enter the number :"))
# for item in range(2,n):
#     for j in range (2,item):
#         if item%j==0:
#             break
#     else:
#         print(item,end=" ")

#factorial

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *=i
#
#     return fact
# print(factorial(5))

#fiboncci series

# def fibo(num):
#     a=0
#     b=1
#     for i in range(num):
#         print(a)
#         tmp=a+b
#         a=b
#         b=tmp
# fibo(10)


# row = 4


# for i in range(row):
#     a=0
#     #for j in range(row-i,0,-1):
#          #print("*",end=" ")
#     for j in range(i+1):
#         a=a+1
#         print(a,end=" ")
#     print(" ")
#-------------------------
# for i in range(row):
#     a=0
#     for j in range(i,row):
#         print(" ",end=" ")
#     for j in range(i+1):
#         a+=1
#         print(a,end=" ")
#     for j in range(i):
#         a -=1
#         print(a,end=" ")
#     print(" ")
# for i in range(row):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,row-1):
#         print("b",end=" ")
#     for j in range(i,row):
#         print("n",end=" ")
#
#     print(" ")

# tp = (3,4,5,3,"str",4)
# re =[]
# for item in tp:
#     if item not in re:
#         re.append(item)
# print(tuple(re))


# def fuc(*args, **kwargs):
#     print(args)
#     print(kwargs)
# fuc(1, 2, 3, name='John', age=25)
# y = {"name":"rajesh", "age": 30}
# f_set = frozenset(y)
# print(f_set)
# set1 = {1, 2, 3, 4}
#
# set2 = {3, 4, 5, 6}
# result_set = set1.difference(set2)
#
# result_updateset = set1.difference_update(set2)
#
# print(result_set)
# print(result_set)
# list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
# dict_from_list = dict(list_of_tuples)
# print(dict_from_list)
# list_of_lists = [["a", 1], ["b", 2], ["c", 3]]
# dict_from_list = dict(list_of_lists)
# print(dict_from_list)
# ls=[1,2,4,3,6,7,7,8]
# l=set(ls)
# l1=list(l)
#
# for i in range(len(l1)):
#     for j in range(i, len(l1)):
#         if (l1[i] > l1[j]):
#             tmp = l1[i]
#             l1[i] = l1[j]
#             l1[j] = tmp
# print(l1)

# def reverse_list(l1,l2):
#     l1.reverse()
#     l2.reverse()
#     output_sum=int("".join(str(n) for n in l1))+int("".join(str(n) for n in l2))
#     res=[]
#     p = str(output_sum)
#     li = list(p)
#     for item in str(output_sum):
#         res.append(item)
#
#     res.reverse()
#     print(res)
#
#
#     # res= output.split("").reverse()
#     # print(res)
#
# ls1 = eval(input("enter the list1 :"))
# print(list(ls1))
# ls2 = eval(input("enter the list2 :"))
# print(ls2)
# reverse_list(list(ls1),list(ls2))

# lst = []
#
# n = int(input("Enter number of elements : "))
#
# for i in range(0, n):
#     ele = int(input(f"enter the {i+1} elements of first list :"))
#     lst.append(ele)
#
# print(lst)

# def binarytodecimal(num):
#     i=0
#     dec =0
#     while num !=0:
#         rem = num%10
#         dec = dec+rem*pow(2,i)
#         num //=10
#         i=i+1
#     print(dec)
#
# binarytodecimal(1010)

# def fun(*args):
#     print(args)
#
# fun(1,2,3,4,5)
# list_of_lists = [["a", [1,3]], ["b", [7,4]], ["c", [9,0]]]
#
# dict_from_list = dict(list_of_lists)
# re = dict_from_list.pop("a")
# print(re)
#
# for key in dict_from_list.keys():
#     for i in dict_from_list[key]:
#         print(dict_from_list[key])


#Binary to Decimal
# def binaryToDecimal(binary):
#     decimal=0
#     i=0
#     while (binary != 0):
#         rem = binary % 10
#         decimal = decimal + rem * pow(2, i)
#         binary = binary // 10
#         i += 1
#     return decimal
# print(binaryToDecimal(111))

#longest palindromic substring

# def palindrome(x):
#     if len(x) <= 1:
#         return False
#     return x == x[::-1]
#
#
# def longest_palindrome(s):
#
#     last = len(s)
#     lst = []
#     for i in range(last):
#         for j in range(i, last):
#             b = s[i:j+1]
#             if palindrome(b):
#                 lst.append(b)
#             else:
#                 continue
#     return lst
#
# a = input("Enter the string: ")
# print(longest_palindrome(a))


# class and object
# class Person:
#     # class variable
#     person_age = 30
#     # protected class variable
#     _person_dept = "IT"
#     #protected variable
#     __person_add = "bangalore"
#
#     def __init__(self, name, age1):
#         self.name = name
#         self.age11 = None
#         self.age1 = age1
#
#     #instance method
#     def instancemethod(self):
#         return self.name + " mmmmm" + self.__person_address() + self.classsmethod()
#
#     #class method
#     def person_job(self, office):
#         return f"the person is working as ", office, " ", self.__person_address()
#
#     #protected method
#
#     def _person_department(self):
#         return self.name + " " + self._person_dept + " " + self.__person_add
#
#     def __person_address(self):
#         return "from private method " + self.__person_add
#
#     @classmethod
#     def classsmethod(cls):
#         return f"person name {cls.__person_add},{cls.person_age},{cls._person_dept},{cls.add(3, 7)}"
#
#     @staticmethod
#     def add(x, y):
#         return x + y
#
#     @property
#     def age1(self):
#         return self.age11
#
#     @age1.setter
#     def age1(self, value):
#         if not isinstance(value, int) or value < 0:
#             raise ValueError("age must be a positive int")
#         # self._age1 = value
#         # return self.age1
#         setattr(self, 'age11', value)
#
#
# p1 = Person("hello", 87)


# p1 = Person("John",-9)
# print(o1.age1)
# setattr(p1, '_age', "two")
# print(p1.age11)
# print(p1.age11("vn"))

# print(p1.instancemethod())
# print(p1.person_job("SE"))
# print(p1.person_age)
# print(p1._person_dept)
# print(p1.__person_add)
# print(p1._person_department())
#private method canot call directly by using object
# print(p1.__person_address())
# print(p1.classsmethod())
# print(p1.add(7,8))


#inheritance
#single inheritance
# class A():
#     def method_A(self):
#         return "class A"
# class B(A):
#     def method_B(self):
#         return "class B"
#
# obj = B()
# print(obj.method_A(),obj.method_B())

#multiple inheritance

# class A:
#     def method_A(self):
#         return "class A"
# class B:
#     def method_B(self):
#         return "class B"
# class C(A,B):
#     def method_C(self):
#         return "class C"
# obj =C()
# print(obj.method_C(),obj.method_A(),obj.method_B())

# #multi level inheritance
# class A:
#     def method_A(self):
#         return "class A"
# class B(A):
#     def method_B(self):
#         return "class B"
# class C(B):
#     def method_C(self):
#         return "class C"
# obj = C()
# print(obj.method_C(),obj.method_B(),obj.method_A())

#hierarchical inheritance
# class A:
#     def method_A(self):
#         return "class A"
# class B(A):
#     def method_B(self):
#         return "class B"
# class C(A):
#     def method_C(self):
#         return "class C"
# obj = C()
# print(obj.method_A(),obj.method_C())
# obj1 = B()
# print(obj1.method_B(),obj1.method_A())

#hybrid

# class A:
#     def method_A(self):
#         return "class A"
# class B(A):
#     def method_B(self):
#         return "class B"
# class C(A):
#     def method_C(self):
#         return "class C"
# class D(B,C):
#     def method_D(self):
#         return "class D"
# obj = D()
# print(obj.method_A(),obj.method_B(),obj.method_C(),obj.method_D())


# class A:
#     def __init__(self,name):
#         self.name = name

#     def meth(self):
#         return self.name
# class B(A):
#     def __init__(self,name,age):
#         self.age = age
#         super().__init__(name)
#
#
#     def another_meth(self):
#         return super().meth()
# # ob = A("myname")
# obj = B("mark",7)

# print(obj.meth())
# print(obj.another_meth())

#
# class Animal:
#     def __init__(self,animal_type):
#         self.animal_type = animal_type
#
#
#     def type(self):
#         return self.animal_type
#
#
#     def color(self,code):
#         return code
#
#
# class Mammal(Animal):
#     def __init__(self):
#         super().__init__("mammal")
#         # print(super().color("#df"))
#
#     def code(self):
#         return super().color("#76t87y")
#     # def color(self,code):
#     #     return super().color(code)
#
#     def color(self):
#         return "yellow"
#
#
# dog = Mammal()
#
# print(dog.code(),dog.color())

#super() method

# class Parent:
#     def __init__(self, name):
#         self.name = name
#
#     def display(self):
#         return f"name is {self.name}"
#
#
# class Child(Parent):
#     def __init__(self, name, age):
#         self.age = age
#         super().__init__(name)
#
#     def display(self):
#         super().display()
#         return f"age is {self.age}"
#
#
# obj = Child("bob", 89)
# # print(obj.display())
#
# my_dict = {'name': 'Alice', 'age': 25}
# my_dict["des"] = "developer"
# # my_dict["des"] = "sales"
# # del my_dict["desw"] #throw error if key is not present
# # print(my_dict.pop("des"))
# copy_dic = my_dict.copy()
# copy_dic['desi'] = "sales"
# # print(copy_dic)
# key_list = ["a", "b", "c"]
# print(my_dict.fromkeys(key_list,"abc"))
# print(my_dict.get("a",9))
# print(list(my_dict)[0::])


#Multiple inheritance

# class A:
#     def __init__(self,name):
#         self.name = name
#
#     def funA(self):
#         return self.name
#
# class B:
#     def __init__(self,age):
#         self.age = age
#
#     def funB(self):
#         return self.age
#
# class C(A,B):
#     def __init__(self,name,age):
#         # super().__init__(name),
#         # super().__init__(age)
#         A.__init__(self, name),
#         B.__init__(self, age)
#
#
#     def funC(self):
#         return f"name is {super().funA()} , age is  {super().funB()}"
#
#
# obj = C("abc",9)
# print(obj.funC())
#
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#
#     def speak(self):
#         print(self.name)
#
#
# class Mammal:
#     def __init__(self, fur_color):
#         self.fur_color = fur_color
#
#
#     def breathe(self):
#         print(self.fur_color)
#
#
# class Pet:
#     def __init__(self, owner):
#         self.owner = owner
#
#
#     def play(self):
#         print(self.owner)
#
#
# class Dog(Animal, Mammal, Pet):
#     def __init__(self, name, fur_color, owner, breed):
#
#         Animal.__init__(self, name)
#         Mammal.__init__(self, fur_color)
#         Pet.__init__(self, owner)
#         self.breed = breed
#
#
#     def bark(self):
#         print("Dog barks")
#
#
# my_dog = Dog("Buddy", "Brown", "Alice", "Golden Retriever")
#
#
# my_dog.speak()
# my_dog.breathe()
# my_dog.play()
# my_dog.bark()

# LMS

# ls =[]
# ds ={"title":"Don Quixote","author":"Miguel de Cervantes","ISBN":"ISBN_1"}
# ds1 ={"title":"Alice's Adventures in Wonderland","author":"Lewis Carroll","ISBN":"ISBN_2"}
# ds2 ={"title":"The Adventures of Huckleberry Finn","author":"Mark Twain","ISBN":"ISBN_3"}
# ls.append(ds)
#
# ls.append(ds1)
#
#
# def Book_Registration(title,author,isbn,publication_date):
#     book_list =[{"title":"Don Quixote","author":"Miguel de Cervantes","ISBN":"ISBN_1"},
#                 {"title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "ISBN": "ISBN_2"},
#                 {"title": "The Adventures of Huckleberry Finn", "author": "Mark Twain", "ISBN": "ISBN_3"},
#                 {'title': 'abc', 'author': 'jnkjnjk', 'isbn': 7687, 'publication_date': 'gvghbvhj'}]
#     book_details ={}
#     book_details["title"] = title
#     book_details["author"] = author
#     book_details["isbn"] = isbn
#     book_details["publication_date"] = publication_date
#     # return book_details
#
#     for ite in book_list:
#         if ite['title'] == title:
#             return "Book is already exist"
#         else:
#             book_list.append(book_details)
#             return "Book is registered successfully"
#         # if ite not in book_list:
#         #     book_list.append(book_details)
#         #     return book_list
#         # else:
#         #
# while True:
#     title = input("Enter the Book title :")
#     author = input("Enter the Author name :")
#     isbn = int(input("Enter the ISBN number :"))
#     publication_date = input("Enter the publication date :")
#
#     print(Book_Registration(title,author,isbn,publication_date))
#
#     user_input = input("Do you want to add book again? (yes/no): ").strip().lower()
#
#     if user_input != 'yes':
#         operation = input("choose next operation")
#         print("Exiting the loop")
#         break

# def logged_method(method):
#     def wrapper(*args, **kwargs):
#         print(f"Calling method {method.__name__}")
#         result = method(*args, **kwargs)
#         print(f"Method {method.__name__} returned {result}")
#         return result+3
#     return wrapper
#
# class MyClass:
#     @logged_method
#     def my_method(self, x):
#         return x * 2
#
# obj = MyClass()
# print(obj.my_method(5))


# class LogDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print(f"Calling {self.func.__name__} with args: {args} and kwargs: {kwargs}")
#         result = self.func(*args, **kwargs)
#         print(f"{self.func.__name__} returned {result}")
#         return result
#
# @LogDecorator
# def add(a, b):
#     return a + b
#
# print(add(3, 5))

# def my_class_decorator(cls):
#     class NewClass(cls):
#         def new_method(self):
#             return f"This is a new method added by the decorator{cls}"
#
#     return NewClass
#
# @my_class_decorator
# class MyClass:
#     def existing_method(self):
#         return "This is an existing method."
#
# obj = MyClass()
# # print(obj.existing_method())
# print(obj.new_method())

# Read (Extract text)


# from PyPDF2 import PdfReader,PdfWriter,PdfFileReader
#
# pdf_files = ["B13-PythonDataengineeringBootcamp.pdf", "Basic and class python_training_material.pdf"]
#
# pdf_writer = PdfWriter()
#
# for pdf_file in pdf_files:
#     pdf_reader = PdfReader(pdf_file)
#     for page_num in range(len(pdf_reader.pages)):
#         page = pdf_reader.pages[page_num]
#         pdf_writer.add_page(page)
#
# output_filename = "combined.pdf"
# with open(output_filename, "wb") as output_file:
#     pdf_writer.write(output_file)
#
# print(f"Combined PDF saved as {output_filename}")


# def read_pdf(file_name):
#     pdf_reader = PdfReader(file_name)
#     text = []
#
#     for page_num in range(len(pdf_reader.pages)):
#         # page = pdf_reader.pages[page_num]
#         text.append(pdf_reader.pages[page_num].extract_text())
#
#     return text
#
# print(read_pdf('Felilion_lab_data engineers.pdf'))


# def read_pdf(file_path):
#     with open(file_path, 'rb') as file:
#         reader = PdfFileReader(file)
#         text = ''
#         for page_num in range(reader.numPages):
#             page = reader.getPage(page_num)
#             text += page.extract_text()
#         return text
#
#
# file_path = 'Felilion_lab_data engineers.pdf'
# print(read_pdf(file_path))


# def repeat_characters(input_str):
#     result = ""
#     i = 0
#
#     while i < len(input_str):
#         char = input_str[i]
#         i + 1 < len(input_str) and
#         if input_str[i + 1].isdigit():
#             num = int(input_str[i + 1])
#             result += char * num
#             i += 2
#         else:
#             result += char
#             i += 1
#
#     return result
#
#
# print(repeat_characters("s3tlz5"))
# print(3*"h")

# ls = [2,3,4,5,6,4,3,2]
# s ={}
# for c in ls :
#     s[c] = ls.count(c)
#
# print(s)


# def longest_palindromic_substrings(str):
#     substr =[]
#     for i in range(len(str)):
#         for j in range(i+1,len(str)):
#             substr.append(str[i:j])
#
#     pal_rev = []
#     pal_sub = []
#
#     for i in substr:
#         rev = ""
#         for j in i:
#             rev = j + rev
#         # print(rev)
#         pal_rev.append(rev)
#
#     # print(pal_rev)
#
#     pal_len = []
#     for i in range(len(pal_rev)):
#         if pal_rev[i] == substr[i]:
#             pal_sub.append(pal_rev[i])
#             pal_len.append(len(pal_rev[i]))
#     # print(pal_sub)
#
#     for i in range(len(pal_len)):
#         if pal_len[i] == max(pal_len):
#             print(pal_sub[i])
# longest_palindromic_substrings("babadkakabarokakak")

# def longest_palindromic_substring(s):
#     def is_palindrome(sub):
#         return sub == sub[::-1]
#
#     longest = ""
#     length = len(s)
#     for i in range(length):
#         for j in range(i + 1, length ):
#             substring = s[i:j]
#             if is_palindrome(substring) and len(substring) > len(longest):
#                 longest = substring
#     return longest
#
#
# input_string = "babadkakabarokakak"
# longest_palindrome = longest_palindromic_substring(input_string)
# print("Longest palindromic substring:", longest_palindrome)


# def hello():
#     ls =[4,5,6]
#     for i in ls:
#         yield i
# y = hello()
# print(next(y))
# print(next(y))
# gen = (x ** 2 for x in range(5))
# print(gen)
# print(next(gen))
# for each in gen:
#     print(each)


# import csv
#
#
#
# def create_csv(file_name, data):
#     with open(file_name, 'w', newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows(data)
#
#
# data = [['Name', 'Age'], ['Rajesh', 30], ['Harish', 25]]
# create_csv('example.csv', data)
#
# import openpyxl
#
#
# # Create (Write)
# def create_excel(file_name, sheet_name, data):
#     wb = openpyxl.Workbook()
#     sheet = wb.active
#     sheet.title = sheet_name
#
#     for row in data:
#         sheet.append(row)
#
#     wb.save(file_name)
#
#
# data = [['Name', 'Age'], ['Rajesh', 30], ['Harish', 25]]
# create_excel('example.xlsx', 'Sheet1', data)


# # Create (Combine PDF files)
# def create_pdf(output_file, input_files):
#     pdf_writer = PdfWriter()
#     for file in input_files:
#         pdf_reader = PdfReader(file)
#         for page_num in range(pdf_reader.numPages):
#             page = pdf_reader.getPage(page_num)
#             pdf_writer.addPage(page)
#     with open(output_file, 'wb') as output_pdf:
#         pdf_writer.write(output_pdf)
# pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']
# output_file = 'combined.pdf'
#
# combine_pdfs(pdf_files, output_file)


# Read (Extract text)
# def read_pdf(file_name):
#     pdf_reader = PdfReader(file_name)
#     text = []
#     for page_num in range(len(pdf_reader.pages)):
#         page = pdf_reader.pages[page_num]
#         text.append(page.extract_text())
#     return text
# print(read_pdf('file1.pdf'))


# Update (Append a page from another PDF)
# def update_pdf(file_name, page_to_add):
#     pdf_reader_main = PdfReader(file_name)
#     pdf_reader_to_add = PdfReader(page_to_add)
#     pdf_writer = PdfWriter()
#
#     for page_num in range(len(pdf_reader_main.pages)):
#         pdf_writer.add_page(pdf_reader_main.pages[page_num])
#
#     pdf_writer.add_page(pdf_reader_to_add.pages[0])
#
#     with open(file_name, 'wb') as output_pdf:
#         pdf_writer.write(output_pdf)
# update_pdf('file1.pdf', 'file1.pdf')
# print(read_pdf('file1.pdf'))

# Delete (Remove a specific page)
# def delete_pdf_page(file_name, page_num_to_delete):
#     pdf_reader = PdfReader(file_name)
#     pdf_writer = PdfWriter()
#
#     for page_num in range(len(pdf_reader.pages)):
#         if page_num != page_num_to_delete:
#             pdf_writer.add_page(pdf_reader.pages[page_num])
#
#     with open(file_name, 'wb') as output_pdf:
#         pdf_writer.write(output_pdf)
# delete_pdf_page('file1.pdf', 0)
# print(read_pdf('file1.pdf'))
#
#

# Try Exception

# try:
#     x= int(input("enter the number :"))
#     result = 10/x
# # except Exception as e:
# #     print(e)
# except ValueError:
#     print("must enter integer")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# else:
#     print(result)
# finally:
#     print("always executes")

# raise[Exception class name (parameter)]
# def divide(x, y):
#     if y == 0:
#         raise ZeroDivisionError("Division by zero")
#     return x / y
# try:
#     result = divide(10, 0)
# except Exception as e:
#     print("Error:", e)
#
# class CustomExceptionError(Exception):
#     pass
#
#
# def validate_input(value):
#     if not isinstance(value, int):
#         raise CustomExceptionError("Input must be an integer")
#
#
# try:
#     validate_input("jnjk")
# except CustomExceptionError as e:
#     print("Error:", e)

# class CustomHTTPException(Exception):
#     def __init__(self, message, status_code):
#         self.message = message
#         self.status_code = status_code
#
# def some(x):
#     if not isinstance(x, int):
#         raise CustomHTTPException("Expected Value is integer", 400)
#     print(x)
# try:
#     some("90")
# except CustomHTTPException as e:
#     print(e.message, e.status_code)

x = set()

x.add(9)
# print(x)
# print(min("python"))
# ds ={"a":1,"b":3}
# print(ds.popitem())
# print(ds)
# file handling
# print("hell".join("jnj"))
ls = ["h", 9, "l"]
ds = {'a': 1, 'b': 20}

# print(ds.setdefault("c",0))
my_list = ["d", "b", "v"]
result = all(my_list)
# print(result)
# num = (8,9,6)
# b = map(lambda x: x ** 2,num)
from functools import reduce

# print(list(b))
# print(reduce(lambda x,y:x*y,num))
# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
#
# result = list(map(lambda x, y: x + y, numbers1, numbers2))
# print(result)
# def GCD(a,b):
#     res = min(a,b)
#     while res:
#         if a % res ==0 and b % res ==0:
#             break
#         res = res -1
#     return res
#
#
#
# print(GCD(24,8))

# def LCM(a,b):
#     res = max(a,b)
#     while res:
#         if res % a ==0 and res % b ==0:
#             break
#         res = res +1
#     return res
#
#
#
# print(LCM(9,8))

# def mul(x,y):
#     return x*y
#
# num =[1,2,3,4]
# re = reduce(mul,num)
# print(re)
s = {9, 8, 5}
# print(s.remove(8))
# print(s)

# list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
# dict_from_list = dict(list_of_tuples)
# print(dict_from_list)
# print(ls.pop())

# file = open("E://Ferilion_Lab//Python//13. File Handling//13. File Handling//_13_File_Handling//file1.pdf","r")
# print(file.readlines())

# import datetime
#
# print(datetime.date.today())
# import datetime
#
# now = datetime.datetime.now()
# today = datetime.date.today()
# date_string = now.strftime('%Y-%m-%d-%Y')
# date_str = today.strftime('%d-%m-%Y')
# print(date_string,"..................",date_str)
#
# date_string = "24-04-04 12:30:00"
# parsed_date = datetime.datetime.strptime(date_string, "%y-%m-%d %H:%M:%S")
# print("Parsed date    :", parsed_date)

# print(datetime.datetime.strptime(date_string,"%d-%m-%Y"))


import re


# design = r'([A-Z]+)([a-z]+)([0-9]+)($|?|!){8}'
# design = r'([A-Z]+[a-z]+[0-9]+[!@#$%^&*()_+\-=\[\]{}]+{8,})'
# r = re.compile(design)
# print(r.match("Aaa90@@@@@"))
# r.match(r'([A-Z]+)([a-z])([0-9]+)($|?|!){8}',password)

# m = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[\$|\?\!])[A-Za-z\d$!&]{8,}$')
# # ^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$
#
# print(m.match('A12M!9oBHJBJ'))


#
# def dec(func):
#     def wrapper(*args, **kwargs):
#         print("Arguments:", args)
#         print("Keyword Arguments:", kwargs)
#         # return func(*args, **kwargs)
#
#     return wrapper
#
# @dec
# def greet(*args,**kargs):
#     print(f"Hello")
#
#
# greet(1, 2, c=3, d=4)

# import mysql.connector
# from datetime import datetime, timedelta
#
# def connect_and_create_database(username, password, host, dbname):
#
#     # global cursor
#     global cursor
#     try:
#         conn = mysql.connector.connect(
#             user=username,
#             password=password,
#             host=host
#         )
#
#         if conn.is_connected():
#             # print("Database connected successfully!")
#             try:
#                 cursor = conn.cursor()
#                 cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")
#
#                 # cursor.execute(query)
#                 # cursor.execute(f"create table if not exists user_list "
#                 #                f"(user_id int primary key auto_increment,"
#                 #                f"user_name varchar(100) not null,"
#                 #                f"user_email varchar(100) unique , "
#                 #                f"user_type int, "
#                 #                f"password varchar(100) ,"
#                 #                f"profile_created_at timestamp default current_timestamp"
#                 #                )
#                 conn.commit()
#                 print("Database created successfully!")
#                 conn.database = dbname
#                 user_table = """create table if not exists user_list (
#                                user_id int primary key auto_increment,
#                                user_name varchar(100) not null,
#                                user_email varchar(100) unique not null,
#                                user_type int not null,
#                                password varchar(100) not null,
#                                profile_created timestamp default current_timestamp)"""
#                 book_table = """create table if not exists book_list (
#                                book_id int primary key auto_increment,
#                                title varchar(200) unique,
#                                author varchar(100) not null,
#                                isbn int ,
#                                publication_date varchar(100),
#                                book_count int check(book_count>=0)) auto_increment = 100"""
#                 # check_in_date = datetime.now()
#                 # due_date = datetime.now()+timedelta(days=15)
#                 book_borrow_table = """create table if not exists book_borrow_record (
#                                borrow_id int primary key auto_increment,
#                                book_id int,
#                                user_id int,
#                                check_in_date date not null,
#                                return_due_date date not null,
#                                return_date date ,
#                                overdue_charges decimal(10,2) default 0,
#                                foreign key(book_id) references book_list(book_id),
#                                foreign key(user_id) references user_list(user_id)
#                                ) auto_increment = 100"""
#                 cursor.execute(user_table)
#                 cursor.execute(book_table)
#                 cursor.execute(book_borrow_table)
#                 print("Table  created successfully")
#             except mysql.connector.Error as e:
#                 print(f"Error creating database: {e}")
#                 conn.rollback()
#             finally:
#                 cursor.close()
#
#     except Exception as e:
#         print(f"Error connecting to MySQL: {e}")
#
#
# connect_and_create_database("root", "root", "localhost", "library_management_system")


# a = [1,2,3]
# b = a
# print(a is b,a is not b)
# a,b = 5,3
# print(a | b,a & b,a^b,~a)
# a = []
# b = []
# print(a is b)
# print(id(a))
# print(id(b))
# print(a==b)

# a = ''
# b = ''
# print(a is b)
# print(id(a))
# print(id(b))
# print(a==b)
# print(~1)
# print(10<<2,10>>2)

# from array import array
# my_array = array("i",[6,8,9,4])
# print(my_array)
# for i in range(3):
#     if i == 1:
#         pass
#     else:
#         print(i)
# list = [3, 7, 4, 10, 8]
# list.insert(1, 67)
# print(list)


# print(list[2:len(list)])
# for i in range(18)[2::3]:
#     print(i)

# str = "string"
# print(str.find("ing"))
# print(str.index("ri"))
#
# print(str.replace("tr","gggg"))

# p = '🚦'
# print(ord(p))
# print(id(p))
# ls = ["f","k","hghj"]
# print("".join(ls))

# s = "python"
# print(s[::-1])

# tuple_of_pairs = (("a", 1), ("b", 2), ("c", 3))
# dict_from_tuple = dict(tuple_of_pairs)
# print(dict_from_tuple)
# keys = ["a", "b", "c"]
# values = [1, 2, 3]
# print(dict(zip(keys,values)))
# import array
# arr = array.array("i",[2,4,6,8])
# arr.append(9)
#
# print(arr)
# y = {"name":"rajesh", "age": 30}
# print(type(frozenset(y)))

# def outer(x):
#     def inner(y):
#         return x + y
#
#     return inner
#
#
# print(outer(3)(5))
#
#
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#
# print(fact(5))
#
# def func(d=4,*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print(d)
#
# name='John'
# age=25
# func(1, 2, 3, name='John', age=25)
# def greet(**kwargs):
#     print(f"{greeting}, {name}!")
#
# # Using keyword arguments
# greet(name="Alice", greeting="Hello")
# greet(greeting="Good morning", name="Bob")

# add = lambda x,y:x+y
# print(add(7,8))
# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# zipped_data = zip(names, ages)
#
# print("zipped_data", zipped_data)
# print(list(zipped_data))
# print(dict(zipped_data))
# print(set(zipped_data))
# print(tuple(zipped_data))
# print(str(zipped_data))
# def add(x:int,y:int)->int:
#     return x+y
# print(add(6,8))

class A:
    color = "red"
    _proc_var = "m protected"
    __pri_var = "m private"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._proc_var = "pppprooo"
        self.__pri_var = "priiiii"

    def myfunc(self):
        return self.name + self.__pri_var + A.color

    @classmethod
    def class_meth(cls):
        return cls.color

    def _prfunc(self):
        return self.__pri_var + self._proc_var + self.__prifun()

    def __prifun(self):
        return self.color

    @staticmethod
    def add(x, y):
        return x * y + 1

    @property
    def display(self):
        return self.name + "jhjj"


class B(A):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age


b = B("hii", 78)

# print(b.name, b.color, b.myfunc(), b._prfunc())


# obj = A("Mark")
# print(obj.name,obj.myfunc())
# print(obj.color,obj._proc_var)
# print(obj._prfunc())
# print(obj.add(3,4))
# print(obj.display)
# namevar = getattr(obj,"name")
# print(namevar)
# setattr(obj,"name","mousumi")
# print(obj.name)

# polimorphism
# class Dog:
#     def speak(self):
#         return "Woof!"
#
# class Cat:
#     def speak(self):
#         return "Meow!"
#
# def animal_sound(animal):
#     print(animal.speak())
#
# dog = Dog()
# cat = Cat()
# class Duck:
#     def disp(self):
#         return "Quack!"
#
# class Dog:
#     def disp(self):
#         return "Woof! But I can quack too!"
#
# def make_it_quack(a):
#     print(a.disp())
#
# duck = Duck()
# dog = Dog()
#
# make_it_quack(duck)
# make_it_quack(dog)


# class A:
#     def read(self):
#         return "rrrrrr"
#
#
# class B:
#     def read(self):
#         return "hhhhhh"
#
#
# def hello(x):
#     print(x.read())
#
#
# a = A()
# b = B()
# hello(a)
# hello(b)

# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
# animals = [Dog(), Cat()]
#
# for animal in animals:
#     print(animal.speak())

# Q. How  to achive method overloading in python
# default arguments,*args and **kwargs,type checking
# class Overloading:
#     def display(self,b = None, *args,**kwargs):
#         # if name is not None:
#         #     return name
#         # else:
#         #     return "name is none"
#
#         # return args,kwargs
#         if b is not None and len(args)==1:
#             return b+args[0]
#
# obj = Overloading()
# print(obj.display("mark",5,"ggg",78,name = "hgbj"))
# print(obj.display(3,2))
#
#
# # Using Multiple Dispatch (Third-Party Library)
#
# from multipledispatch import dispatch
#
#
# class Poly:
#     def __init__(self):
#         pass
#
#     @dispatch(int, int)
#     def add(self,x, y):
#         return x + y
#
#     @dispatch(str, str)
#     def add(self,x, y):
#         return x + " " + y
#
#
# obj = Poly()
#
# print(obj.add("hello", "word"))
# print(obj.add(3,6))

# from abc import ABC,abstractmethod
#
# class AbstractClass(ABC):
#
#     @abstractmethod
#     def display(self):
#         pass
#
# class Child(AbstractClass):
#     def display(self):
#         return "Hello Abstract"
#
# obj = Child()
# print(obj.display())

# Custom Exceptions

# class CustomException(Exception):
#     def __init__(self,code,message):
#         self.code = code
#         self.message = message
#
# def result(x):
#     if not isinstance(x,int) :
#         raise CustomException("Expected value is integer ", 400)
#     print(x)
#
# try:
#     result("jknkj")
# except CustomException as e:
#     print(e.code,"---------",e.message)


# def func():
#     ls = [3, 4, 5, 6, 7]
#     it = iter(ls)
#     it.__next__()
#     for e in it:
#         print(e)

# default, positional,keyword

#
# def func(nam,b=0,*args,**kwargs):
#     pass
#
#
# func(10,12,132,34,name = "ghghg")
# paremeter preceence
# positional -> default ->*args -> **kwargs
# def func(a, b=2, *args, d=4, **kwargs):
#     print("a:", a)
#     print("b:", b)
#     print("args:", args)
#     print("d:", d)
#     print("kwargs:", kwargs)
#
# # Calling the function with various types of arguments
# func(1,7, 3, 5, 6, d=7, e=8, f=9)


# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(".",end="")
#     for j in range(i, n-1):
#         print("*", end="")
#     for j in range(i,n):
#         print("0", end="")
#     for j in range(i):
#         print("u",end="")
#     print()

# 16
# l1 = [2,4,3]
# l2 = [5,6,4]
# l1.reverse()
# l2.reverse()
# str1 = "".join(str(i) for i in l1)
# str2 = "".join(str(i) for i in l2)
# res = str(int(str1)+int(str2))
# resu = []
# for i in res:
#     resu.append(int(i))
# resu.reverse()
# print(resu)

# 15.
#
# def func():
#     str = ["flower", "flow", "flight"]
#     # str = ["dog","racecar","car"]
#     res = ""
#     for item in range(len(str[0])):
#         # print(str[0][item])
#         for i in str:
#             # print(i[item])
#             if i[item] != str[0][item]:
#                 return res if len(res) > 0 else "Not matching prefix"
#         res += str[0][item]
#
#
# print(func())


#
# ls1 = {"a": 3,"f": 1,"k": 8}
# sorted = sorted(ls1.items(), key = lambda x:x[1],reverse=True)
# print(dict(sorted))

#file handling
# file = open("file.txt","a")
# # print(file.read())
# # print(file.readline())
# # print(file.readlines())
# # file.write("This is new content written to the file.")
# # print(file.readlines())
# file.write("hhhhhhiiiiiiiiiiiiiii")
# file.close()

# import csv
#
# def create_csv(file_name,data):
#     with open(file_name,"w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows(data)
#         # writer.writerow(data)
#
# data = [['Name', 'Age'], ['Rajesh', 30], ['Harish', 25]]
# create_csv('example.csv', data)
# def read_csv(file_name):
#     with open(file_name,"r") as file:
#         reader = csv.reader(file)
#         return list(reader)
#
# print(read_csv("example.csv"))
#
# def update_csv(file_name,index,new_data):
#     data = read_csv(file_name)
#     data[index] = new_data
#     create_csv(file_name,data)
#
#
# update_csv("example.csv",1,["suresh",30])
#
# def delete_csv(file_name,index):
#     data = read_csv(file_name)
#     data.pop(index)
#     create_csv(file_name,data)
#
#
# delete_csv("example.csv",2)
# print(read_csv("example.csv"))

# import openpyxl
#
# def create_excel(file_name,sheet_Name,Data):
#     wb = openpyxl.Workbook()
#     sheet = wb.active
#     sheet.title = sheet_Name
#
#     for row in data:
#         sheet.append (row)
#
#     wb.save(file_name)
#
#
# data = [['Name', 'Age'], ['Rajesh', 30], ['Harish', 25]]
# create_excel("example.xlsx","Sheet1",data)
#
# def read_excel(file_name,sheet):
#     wb = openpyxl.load_workbook(file_name)
#     sheet_data = wb[sheet]
#     return [[Cell.value for Cell in row] for row in sheet_data.iter_rows()]
#
#
# print(read_excel("example.xlsx","Sheet1"))
#
# def update_excel(file_name,sheet,index,new_data):
#     wb = openpyxl.load_workbook(file_name)
#     sheet = wb[sheet]
#
#     for col_index ,value in enumerate(new_data,start=1):
#         sheet.cell(row = index,column=col_index,value=value)
#
#     wb.save(file_name)
#
#
# update_excel("example.xlsx","Sheet1",2, ["Suresh",31])
#
# def delete_excel_row(file_name, sheet_name, row_index):
#     wb = openpyxl.load_workbook(file_name)
#     sheet = wb[sheet_name]
#     sheet.delete_rows(row_index)
#     wb.save(file_name)
#
#
# delete_excel_row('example.xlsx', 'Sheet1', 2)
# print(read_excel('example.xlsx', 'Sheet1'))
#

#Anagram digit
# def digit_anagram(num1,num2):
#     str1 = [int(x) for x in str(num1)]
#     str2 = [int(x) for x in str(num2)]
#     str1.sort()
#     str2.sort()
#     print(str1)
#     print(str2)
#     print([1,2,3] == [2,3,1])
#     print(str1 == str2)
#     if str1 == str2:
#         return "anagram"
#     else:
#         return "not anagram"
#
#
#
#
# n1 = 54275
# n2 = 45572
# print(digit_anagram(n1,n2))

# def perfect_Number(num):
#     sum = 0
#     for i in range(1,num):
#         if num %i == 0:
#             sum += i
#
#     if sum == num:
#         return "perfect"
#     else:
#         return "Not perfect"
#
#
# inp = int(input("enter the number :"))
# print(perfect_Number(inp))

# def longest_palindromic_substrings(str):
#     substr = []
#     for i in range(len(str)):
#         for j in range(i + 1, len(str)):
#             substr.append(str[i:j])
#
#     pal_rev = []
#     pal_sub = []
#
#     for i in substr:
#         rev = ""
#         for j in i:
#             rev = j + rev
#         # print(rev)
#         pal_rev.append(rev)
#
#     # print(pal_rev)
#
#     pal_len = []
#     for i in range(len(pal_rev)):
#         if pal_rev[i] == substr[i]:
#             pal_sub.append(pal_rev[i])
#             pal_len.append(len(pal_rev[i]))
#     # print(pal_sub)
#
#     for i in range(len(pal_len)):
#         if pal_len[i] == max(pal_len):
#             print(pal_sub[i])
#
#
# longest_palindromic_substrings("babab")

# def dec_class(func):
#     def wrapper(*args,**krargs):
#         print(args)
#         print(krargs)
#         # return func(*args)
#
#     return wrapper
#
#
# @dec_class
# def greater(x, y,k=0,s=0):
#     print(x if x > y else y)
#
#
# greater(5, 8,k=2,s=3)
#
#
# def print_args_kwargs(func):
#     def wrapper(*args):
#         # action part
#         print("Arguments:", args)
#         # print("Keyword Arguments:", kwargs)
#         # return func(*args, **kwargs)
#
#     return wrapper
#
#
# # return print_args_kwargs
#
#
# @print_args_kwargs
# def example_function(a, b):
#     print("Inside example_function")
#
#
# #
# #
# example_function(1, 2)


# class Hello:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return self.func(*args, **kwargs)
#
#
# @Hello
# def Function(*args, **kwargs):
#     print(args)
#
#
# Function(2, 3, z=9, k=8)

#
# class HelloClass:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         return self.func(*args, **kwargs), "Hello from class decorator"
#
#
# @HelloClass
# def hello(x, y):
#     return x + y
#
#
# print(hello(2, 3))

# ds1 = {"a":1,"b":2,"c":3}
# print(dict(zip(ds1.values(),ds1.keys())))


# s = set({})
# s.add(("b",2))
# s.add(8)
# # print(s)
#
# # print(sum([8, 7, 6]))
# def func(pos, p=4, *args, **kargs):
#     print(args)
#     print(kargs)
#
#
# func(9, 7, 8, 9, 4, k=4, d=6, u=9)


# using count() functions
# ls = [1,2,3,2,2,3,4,4,0]
#
# ds = {}
# for i in ls:
#     ds[i] = ls.count(i)
#
# occ_list = sorted(list(set(ds.values())),reverse=True)
# second_occ_count_val = occ_list[1]
#
# for key in ds.keys():
#     if ds.get(key) == second_occ_count_val:
#         print(key)

# without using count() functions
# ls = [1,2,3,2,2,3,4,4,0]
#
# ds = {}
# unique = list(set(ls))
# for i in unique:
#     count = 0
#     for j in ls:
#         if i == j:
#             count += 1
#     ds[i] = count
#
# occ_list = sorted(list(set(ds.values())), reverse=True)
# second_occ_count_val = occ_list[1]
#
# for key in ds.keys():
#     if ds.get(key) == second_occ_count_val:
#         print(key)

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# # Email setup
# sender_email = "mousumiara.ahmed@gmail.com"
# receiver_email = "mousumiara.ahmed@gmail.com"
# subject = "Test Email"
# body = "This is a test email sent from Python."
#
# # Create a MIME object
# msg = MIMEMultipart()
# msg['From'] = sender_email
# msg['To'] = receiver_email
# msg['Subject'] = subject
#
# # Attach the body to the email
# msg.attach(MIMEText(body, 'plain'))
#
# # SMTP server setup (e.g., Gmail's SMTP server)
# smtp_server = "smtp.gmail.com"
# smtp_port = 587
# smtp_user = "mousumiara.ahmed@gmail.com"
# smtp_password = ""
#
# try:
#     # Create a secure connection with the server and send the email
#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()  # Secure the connection
#     server.login(smtp_user, smtp_password)
#     text = msg.as_string()
#     server.sendmail(sender_email, receiver_email, text)
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"Failed to send email: {e}")
# finally:
#     server.quit()

# ls = [2,3,4,5,8]
# # print(ls[2:3])
# for i in ls:
#     print(i)
# from array import array
# arr = array("i",[1,2,3,4])
# print(arr)
# single = "This string variable's contains\n 'single' quotation marks."
# double = 'This string's variable contains "double"  quotation marks.'
# triple = '''this is's triple quote'''
# print(single)

# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# except Exception as e:
#     print("jjk", e)
# else:
#     print(result)
# finally:
#     print("hi i am finally !")

#custom exception
# class CustomException(Exception):
#     def __init__(self,mess,code):
#         self.mess = mess
#         self.code = code
#
#     def ValueCheck(self,val):
#         if not isinstance(val, int):
#             # print(self.mess,self.code)
#             raise CustomException("must be integer",500)
#
#
# obj1 = CustomException("hjnhj",899)
# try:
#     obj1.ValueCheck("hhh")
# except CustomException as e:
#     print(e.mess, e.code)

#
# s ={1,7,2,3,0,4}
# s.pop()
# # s.pop()
# print(s)

# import pdb
#
#
# def add(x, y):
#     # pdb.set_trace()
#     print("hbj")
#     print("hhhhhhhhhhhhhhhhhhhhhhhh")
#     print("hbj")
#     # pdb.set_trace()
#     print("hjbkjnil")
#     print("dstdty")
#     print("nhbjhnioio")
#     # pdb.set_trace()
#     # breakpoint()
#
#     return x + y
#
#
# print(add(7, 8))
# from datetime import datetime,timedelta
#
# print(datetime.now())
# # print(datetime.today())
# # print(datetime.utcnow())
# # print(datetime.now().strftime("%d-%m-%Y"))
# print(datetime.now() + timedelta(weeks=3, days=4))

# MultiTreading

# import threading
# import time
#
#
# def print_Number():
#     for i in range(10):
#         time.sleep(1)
#         print(i)
#
#
# def print_letters():
#
#     for letter in "abcghjnshs":
#         time.sleep(1)
#         print(letter)
#
#
# thread1 = threading.Thread(target=print_Number)
# thread2 = threading.Thread(target=print_letters)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
# import logging
#
#
# def func(ls):
#     # Configure the logging system
#     logging.basicConfig(level=logging.DEBUG)
#
#     logging.debug("This is a debug message")
#     logging.info("This is an info message- before ")
#     # logging.warning("This is a warning message")
#     # logging.error("This is an error message")
#     # logging.critical("This is a critical message")
#
#     try:
#         div = 10 / 0
#         logging.info("This is an info message- inside try")
#     except Exception as e:
#         print(e)
#         logging.error(e)
#         logging.info("This is an info message- inside exception")
#
#     else:
#         print(div)
#         logging.info("This is an info message- inside else")
#
#     # print(logging.info("this is the info message"))
#     logging.info("..........This is an info message")
#
#
# func([])

# ls=[{"name":"mousumi"}]
# ls1=[{"name":"mousumi"}]
# print(ls == ls1)

#
# import urllib.parse
#
# url = "https://reqres.in/api/users;1?page=2"
# # url = "https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#create-the-tables"
# # url = "https://www.example.com/path/to/page;param=value?query=query_example#fragmentAnchor"
# # Get res with parts of url
# res = urllib.parse.urlparse(url)
#
# # Display contents
# print(res)
# print("Scheme : ", res.scheme)
# print("Netloc : ", res.netloc)
# print("Params : ", res.params)
# print("Port   : ", res.port)
# print("Query   : ", res.query)
# print("URL    : ", res.geturl())
# print("Path,suffix url   : ", res.path)
import json
import pickle

from flask import Flask, render_template
import mysql.connector


app = Flask(__name__)
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'classicmodels'
}


def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn


@app.route('/')
def index():
    return "hello"


@app.route("/users")
def users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM customers')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    data = []
    final_data ={}
    for item in rows:
        data.append(str(item))
    final_data["data"] = data
    return final_data



if __name__ == '__main__':
    app.run(debug=True)



