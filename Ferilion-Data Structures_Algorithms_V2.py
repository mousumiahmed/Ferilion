#String
import binascii

import toolz

# #1.Length of string
# str ="jnjnknkl"
# print(len(str))

# 2.Count characters in string
# str = "hello word"
# count =0
# for x in str:
#     count +=1
#     #print(x,str.count(x))
# print(count)

#3.String slicing
# str = "welcome"
# result = str[2:5]
# print(result)
#4.Replace first occurance character
# str = "welcome"
#
# print(str.replace(str[0],"H"))

# 5.Swapping chars in string
# str ="welcome"
# data = list(str)
# tmp = data[0]
#
# data[0] = data[6]
# data[6] = tmp
# result = ''
# print(result.join(data))


# 6.Append chars to string at end
# str = input("enter the string :")
# char_add = input("enter char to to append end of string :")
# str = str+char_add
# print(str)

#7 .Substring replacement
# rep1 = str[1:3]
# rep2 = str[5:]
#
# result = str.replace(rep1,rep2)
# result = result.replace(rep2,rep1)
# str = result
#
# print(rep1,rep2,str)

#8.Length of longest string in python

# ls = ["fg","java","python","programming"]
# max =0
# for x in ls:
#     if len(x)>max:
#         max=len(x)
# # str ="hellow"
# # larnest_str = max(str)
#
# # print(larnest_str)
# print(max)

# 9.nth index character from string

# str = input("enter the string :")
# n = int(input("enter the nth index :"))
# ch = str[n]
# print(f"nth index character will be : {ch}")

#10 .First last chars swapping

# str =input("enter the String :")
# data = list(str)
# tmp = data[0]
# data[0] = data[len(data)-1]
# data[len(data)-1] = tmp
# res_str =''
# res_str=res_str.join(data)
# print("After Swapping first and last character :",res_str)

# 11. Remove odd index values
# str = input("Enter the String :")
# res=""
# for x in range(len(str)):
#     if x%2 ==0:
#         res += str[x]
# print("After remove odd index value :",res)

#12 .Count words in a string

# str =input("enter the string words seperated by space :")
# res = len(str.split(" "))
# print(f"No of words in the string {res}")

# 13. Upper lower case of a string
# str =input("enter the string :")
# print("Upper case :",str.upper(),"Lower case :",str.lower())

#14 .Sort unique words alphanumerically

# str = input("enter the words seperated by comma :")
#
# print(",".join(sorted(set(str.split(",")))))

# 15. Create html from string


# 16.Insert string in middle of speical chars

# str = input("enter the special characters :")
# str_insert = input("enter the string you want to insert :")
# data = list(str)
# mid=0
# if len(data)%2==0:
#     mid=len(data)/2
# else:
#     mid = (len(data)+1)/2
#
# data.insert(int(mid),str_insert)
#
# print("".join(data))


#List
#---------------------------------------------------------------------------------------------------------------------------------------------
#1.Sum of elements

# def sum(input_list):
#     sum=0
#     for item in input_list:
#         if type(item) == int:
#             sum += item
#
#     print(sum)
# ls = eval(input("enter the list items :"))
# sum(list(ls))

# 2. Mulitply of elements

# def mul(input_list):
#     mul=1
#     for item in input_list:
#         if type(item) == int:
#             mul *= item
#
#     print(mul)
# ls = eval(input("enter the list items :"))
# mul(list(ls))

# 3. Largest number from list

# def largest_Number(input_list):
#     data = sorted(input_list)
#     print(data[len(data)-1])
#
# ls = eval(input("enter the list items :"))
# largest_Number(list(ls))
# 4. Smallest number from list

# def smallest_Number(input_list):
#     print(min(input_list))
#
# ls = eval(input("enter the list items :"))
# smallest_Number((list(ls)))

# 5. Count no of strings whose length is 2

# def count_str(input_list):
#     #print(input_list)
#     count = 0
#     for item in input_list:
#         if len(str(item)) ==2:
#             count = count+1
#     print(count)
#
#
# inp = eval(input("enter the list item :"))
# count_str(list(inp))

# 6.Sort elements in increasing order

# def list_sort(input_list):
#     data = sorted(input_list,reverse=False)
#     print(data)
# ls = eval(input("enter the item of list :"))
# list_sort(list(ls))

# 7.Remove duplicates
# def remove_duplicate(input_list):
#     # data = set(input_list)
#     # print(list(data))
#     #without using set
#     res = []
#     for item in input_list:
#         if item not in res:
#             res.append(item)
#     print(res)
# ls = eval(input("enter the item of list :"))
# remove_duplicate(list(ls))
# 8. Check list is empty or not

# def check_list(input_list):
#     print(input_list,len(input_list))
#     if len(input_list) == 0:
#         print("empty list")
#     else:
#         print("list is not empty")
#
# ls = eval(input("enter the item of list :"))

# check_list(list(ls))

# n = int(input("enter the no of element in list :"))
# data =[]
# for item in range(n):
#     x = input("enter the item :")
#     data.append(x)
#
# if len(data) ==0:
#     print("empty list")
# else:
#     print("list is not empty")
# #print(data)

# smp_list = [2,3,4,5,6]
# # smp_list.append(89)
# # smp_list.clear()
# copied_list = smp_list.copy()
# copied_list.append(90)
# copied_list.extend([9,0])
# copied_list.insert(1,66)
# copied_list.pop(6)
# copied_list.sort(reverse=False)
# print(copied_list,smp_list)

# 9. Clone or copy
# list =[3,4,5,6]
# new_list = list.copy()
# print(new_list)

# 10. Words that are longer than any element
# list = ["a","ab","python","jnkj","pythoon"]
# print(max(list))

# 11.Find common element from 2 lists
# ls1 = [1,3,23,"str"]
# ls2 = [23,"hi",3]
# res = []
# for x in ls1:
#     for y in ls2:
#         if x==y:
#             res.append(x)
#
# print(res)

# 12. Remove specified index from list and print
# ls = [67,9,34,6]
# ls.remove(ls[0])
# print(ls)

#-----------------------------------------------------------------------------------------------------------------------------------------

# #Dictonary
# # 1.Prints each item and its corresponding type from the following list.
# dc = {"name":"Lee","age":67,"salary":876878}
# print(dc.items())
# for item in dc:
#     print(item,type(item))
# dc["ph_no"] = 876878789
# print("name" in dc)


#-------------------------------------------------------------------------------------------------------------------------------------------
# import copy

# original_list = [1, 2, [3, 4]]
# shallow_copied_list = copy.copy(original_list)
#
# print("id of original_list ", id(original_list))
# print("id of shallow_copied_list ", id(shallow_copied_list))
# print("id of  ", id(original_list[2]))
# print("id of  ", id(shallow_copied_list[2]))
# # Modify the original list
# original_list[2][0]= 99
#
# print(original_list)
# print(shallow_copied_list)
#
# print("id of  ", id(original_list[2]))
# print("id of  ", id(shallow_copied_list[2]))

# original_list = [1, 2, [3, 4]]
# deep_copied_list = copy.deepcopy(original_list)

# print("id of original_list ", id(original_list))
# print("id of deep_copied_list ", id(deep_copied_list))
# print("id of  [3, 4]", id(original_list[2]))
# print("id of  [3, 4]", id(deep_copied_list[2]))


# # Modify the original list
# original_list[2][0] = 99
#
# print(original_list)
# print(deep_copied_list)
#
# print("id of original_list[2]", id(original_list[2]))
# print("id of deep_copied_list[2]", id(deep_copied_list[2]))


#LCM of two number

# num1 = int(input("enter the first number :"))
# num2 = int(input("enter the second number :"))
# greater=0
# lcm = 0
#
#
# if num1>=num2:
#     greater=num1
# else:
#     greater=num2
#
# while(True):
#     if greater % num1 == 0 and greater % num2 == 0:
#         lcm = greater
#         break
#     greater +=1
#
# print(lcm)

#Matrix Multiplication
# matrix1 = [[1,7,3],[3,5,6],[6,8,9]]
# matrix2 = [[1,2,1,2],[6,7,3,0],[4,5,9,1]]
# output = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]
# # print(output)
# # print(matrix2[0])
# # print(matrix1[0])
# for i in range(len(matrix1)):
#     for j in (range(len(matrix2[0]))):
#         for k in (range(len(matrix2))):
#             output[i][j] += matrix1[i][k] * matrix2[k][j]
# print(output)
#
# #occurance of character in a string
#
#str = "helloooooooo"
#out = {item: str.count(item) for item in set(str)}
# output = {item:str.count(item) for item in str}
# print(out)
# print(output)


#Dictionary grouping

# dc = {"state1":1,"state2":1,"state3":2,"state4":3,"state5":3}
# original_list = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
# output = {"yellow":[1,3],'blue':[2],"red":1}
# res ={}
# res=defaultdict(list)
# for x,y in original_list:
#     res[x].append(y)
# print(res)

# for item in original_list:
#     if item[0] not in res:
#         res[item[0]] = [item[1]]
#     else:
#         res[item[0]].append(item[1])
# print(res)
#from dictionary
# output = defaultdict(list)
# for x,y in dc.items():
#     output[y].append(x)
# print(output)
# #print(dc.items())

# square = {x:x*x for x in range(10)}
# print(square)
#
# dc={}
# keys = ["a","b","c"]
# values =[1,2,3]
# dc={key:value for key,value in zip(keys,values)}
# print(dc)

# MATRIX,
# LIST INCREASING DECREASING ORDER(SORTING),
# largest number,
# OCCURANCE OF NUMBER AND CHARACTER,
# ARMSTRONG NUMBER,
# DECIMAL TO BINARY WITHOUT USING LIST,
# STRING ANAGRAM OR NOT,
# first 10 rows of Pascal's Triangle,
# gcd AND LCM,
# PRIME NUMBER,
# Collatz sequence for a given starting number,
# perfect number,
# check if a number is a power of two,
# STRONG NUMBER,PRIME,
#BINARY SEARCH

#strong number
# num = int(input("enter the number :"))
# sum=0
#
# rem=0
# #123
# tmp = num
# while(tmp):
#     rem=tmp%10
#     x=1
#     fact=1
#     while x <= rem:
#         fact = fact*x
#         x = x+1
#     sum += fact
#     tmp //=10
#
# print(sum)


#prime number
# num=int(input("enter the number :"))
# res = True
# if num==1:
#     res=False
# elif(num>1):
#     for x in range(2, num):
#         #print(x)
#         if num % x ==0:
#             res = False
#             break
#         else:
#             res = True
# if res==True:
#     print("prime")
# else:
#     print("not prime")

#GCD
# num1 = int(input("enter the first number :"))
# num2 = int(input("enter the second number :"))
# min=0
# gcd=0
# if(num1<num2):
#     min=num1
# else:
#     min=num2
#
# #print(min)
# for i in range(1, min+1):
#     if num1 % i == 0 and num2 % i == 0:
#         #print(i)
#         gcd=i
# print(gcd)

#decimal to binary
# def convertToBinary(n):
#    # if n==0:
#    #     print(0)
#    # elif n==1:
#    #     print(1)
#    if n > 1:
#        convertToBinary(n//2)
#    print(n % 2,end = '')
#
#
# convertToBinary(9)
#prime number

# def prime(num):
#     for item in range(2,num+1):
#         for i in range(2,item):
#             if item % i==0:
#                 break
#         else:
#             print(item,end=" ")
#
#
# prime(50)


#--------------------------------------------------------------------
#Tuple
#create a tuple

#empty tuple

# tp = ()
# print(type(tp))
# tp_fruits = ("mango","banana","cherry")
# print(tp_fruits)

#create a tuple with different data types
# tp= ("mark",56,True,False,8.90)
# print(tp)
#create a tuple with numbers and print one item

# tp = (2,3,4,12,6,8,23)
# print(tp[2],tp.index(12),tp.count(23))

#unpack a tuple in several variables

# tp = ("hii","hello","welcome","hiii")
# x,y,*z =tp
# print(x)
# print(y)
# print(z)

#add an item in a tuple.
#* tuple element canot be added as its immutable.but we can concate with another tuple using + operator
tp = (3,4,5,6)
y=(8,9,7,8,9)
# tp += 8
tp = tp+y
print(tp[3],tp[-4])

# tp = (1,3,"str","word")
# st = ""
# for i in tp:
#     st = st +str(i)
# print(st)

#get the 4th element and 4th element from last of a tuple
# tp = (1,3,"str","word","mango",True)
# print("4th element from begining :",tp[4-1])
# print("4th element from end :",tp[-4])

#create the colon of a tuple
# import copy
# tp = tp = (1,3,[],"str","word","mango",True)
# tp_cpoy = copy.deepcopy(tp)
# tp_cpoy[2].append(78)
# print(tp)
# print(tp_cpoy)

#find the repeated items of a tuple

# tp = (1,3,[],"str","word","mango",3,"word",3)
# # print(tp.count(1))
# res = []
# for i in tp:
#     if tp.count(i) >1:
#         if i not in res:
#             res.append(i)
# print(res)

#check whether an element exists within a tuple
# tp = (1,3,[],"str","word","mango",3,"word",3)
# ele = 3
# if tp.count(ele)>=1:
#     print("element is exist")
# else:
#     print("element does not exist")

#convert a list to a tuple
#
# ls = [1,3,[],"str","word","mango",3,"word",3]
# tp = tuple(ls)
# print(tp)

#remove an item from a tuple
# tp = (1,3,[],"str","word","mango",3,"word",3)
#
# ls=list(tp)
# ls.pop()
# tp1=tuple(ls)
# print(tp1)

#slice a tuple
# tp = (1,3,[],"str","word","mango",3,"word",3)
# print(tp[1:3])
# print(tp)

#find the index of an item of a tuple
# tp = (1,3,[],"str","word","mango",3,"word",3)
#
# print("index of 3 :",tp.index(3))

#find the length of a tuple
# tp = (1,3,[],"str","word","mango",3,"word",3)
# print(len(tp))

#convert a tuple to a dictionary
# tp = (1,3,"str","word","mango",3,"word",3)
# ds ={}
# ds1={}
# for i in tp:
#     ds[i] = i
#     #ds1[tp[i]] = tp.count(tp[i])
# print(ds)

#unzip a list of tuples into individual lists.

ls = [(3, 4), (1, 2), ("str", 3)]
# res = list(zip(*ls))
# print(res)

#or
# a=[]
# b=[]
# res =[]
# res1 =[]
# for i in range(len(ls)):
#     a.append(ls[i][0])
#     b.append(ls[i][1])
# res.append(a)
# res.append(b)
# res1.extend(a)
# res1.extend(b)
# print(res)
# print(res1)

#reverse a tuple

# tp = (1,3,"str","word","mango",3,"word",3)

# print(tp[::-1])

#convert a list of tuples into a dictionary
# tp = (1,3,"str","word","mango",3,"word",3)
# ds={}
#
# for i in tp:
#     ds[i]=tp.count(i)
# print(ds)

#print a tuple with string formatting
# tp = (1,3,"str","word","mango",3,"word",3)
# print("string format{0}".format(tp))

#replace last value of tuples in a list

# ls = [(2,3,4),(7,3,"hii"),(0,"l","w")]
# ls[len(ls)-1] = "python"
# print(ls)

#to remove an empty tuple(s) from a list of tuples
# ls = [(2,3,4),(),(7,3,"hii"),(0,"l","w"),()]
# for item in ls:
#     if len(item)==0:
#         ls.remove(item)
# print(ls)
#sort a tuple by its float element.
# tp =(3,7,7.8,3.5)
# tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),
#     ('anand', '4.256'), ('gaurav', '10.365')]
# print(sorted(tp))
# for i in range(len(tup)):
#print(sorted(tup[i][1]))

#count the elements in a list until an element is a tuple

# ls = [1,1,3,('lucky', '18.265'), 7,('anand', '4.256'), ]
#
# for i in ls:
#     if isinstance(i,tuple):
#         break
#     else:
#         print(ls.count(i))

#------------------------------------------------------------------------------
#Set
#Create a set.
#
# s = {1,2,3,"str"}
# print(s)
#Iteration over sets.
# s = {1,2,3,"str"}
# for item in s:
#     print(item)
#Add member(s) in a set
# s = {1,2,3,"str"}
# s.add("a")
# print(s)
#Remove item(s) from set
# s = {1,2,3,"a","str"}
# s.remove("a") #if item is not in set it will throw key error
# s.discard("b")#if item is not present it will not throw any error
# print(s)
#Remove an item from a set if it is present in the set
# s = {1,2,3,"a","str"}
# s_new = set() // empty set
# s.remove(2)
# print(s)

#Create an intersection of sets
# s1 = {1,2,9}
# s2 = {1,2,3,"a","str"}
# s_new = s1.intersection(s2)
# print(s_new)

#Create a union of sets

# s1 = {1,2,9}
# s2 = {1,2,3,"a","str"}
# s_new = s1.union(s2)
# print(s_new)

#Create set difference
# s1 = {1,2,9}
# s2 = {1,2,3,"a","str"}
# s_new = s1.difference(s2)
# print(s1)
# print(s_new)

#Create a symmetric difference
# s1 = {1,2,9}
# s2 = {1,2,3,"a","str"}
# s_new = s1.symmetric_difference(s2)
# print(s1)
# print(s_new)

#Issubset and issuperset
# s1 = {1,2,9}
# s2 = {1,2,3,"a","str"}
# s_issub = s1.issubset(s1)
# s_issuper = s1.issuperset(s2)
#
# print(s1)
# print(s_issub,s_issuper)

#Create a shallow copy of sets
# import copy
# s1 = {1,2,9}
# s_copy = copy.copy(s1)
# print(s_copy)

#Clear a set.
# s1 = {1,2,9}
# s1.clear()
# print(s1)

#Use of frozensets
#An immutable version of a Python set object is a frozen set.
#While parts of a set can be changed at any moment, elements of a frozen set don’t change after they’ve been created. As a result, frozen sets can be used as Dictionary keys or as elements of other sets.
# s1 = {1,2,9}
# s_f = frozenset(s1)
# print(s_f)

#Find maximum and the minimum value in a set
# s = {"str",1,2,3,9,False}
# # s_new ={0}
# s_new=set()
# for item in s:
#     if not isinstance(item,(str,bool)):
#         s_new.add(item)
#
# print(s_new)
# print(max(s_new))
# print(min(s_new))

#Find the length of a set
# s = set()
# s1={3,4,"hii"}
# print(len(s))

#-------------------------------------------------------------------------------
#Array
#Create an array of 5 integers and display the array items. Access individual element through indexes.

import array

# arr = array.array("i",[3,5,6,7,8])
# for item in arr:
#     print(item)
# for item in range(len(arr)):
#     print(arr[item],"index: ",item)

# arr1=array.array("i",[])
# arr1.append(9)
# arr1.append(5)
# print(arr1)

#Reverse the order of the items in the array

# arr1=array.array("i",[8,7,2,12,23,4])
# arr1.reverse()
# print(arr1)

#Get the length in bytes of one array item in the internal representation.
arr = array.array("i", [8, 7, 2, 12, 23, 4])

# print(arr.itemsize)
# print("total size",arr.itemsize * len(arr))

#Get the current memory address and the length in elements of the buffer used to hold an arrays? contents and also find the size
# arr=array.array("i",[8,7,2,12,23])

# for item in arr:
#     print(len(str(item)))

# print("total array size :",arr.itemsize * len(arr))

#Get the number of occurrences of a specified element in an array
# arr=array.array("i",[8,7,2,12,23,8])
# occ={}
#
# for i in arr:
#     occ[i]=arr.count(i)
#     # print(i, "=",arr.count(i))
# print(occ)

#Append items from inerrable to the end of the array
# arr=array.array("i",[])
# ls =[8,7,2,12,23,8]
# for item in ls:
#     arr.append(item)
# print(arr)

#Convert an array to an array of machine values and return the bytes representation
# arr=array.array("i",[8,7,2,12,23,8])
# arr_byte =arr.tobytes()
# print(arr_byte)
# print(binascii.hexlify(arr_byte))


#Insert a new item before the second element in an existing array.
# arr=array.array("i",[8,7,2,12,23,8])
# arr.insert(1,56)
# print(arr)

#Remove a specified item using the index from an array
# arr=array.array("i",[8,7,2,12,23,8])
# arr.__delitem__(0)
# print(arr)

#Remove the first occurrence of a specified element from an array.
# arr=array.array("i",[8,7,2,12,23,8])
# arr.remove(8)
# print(arr)
#Convert an array to an ordinary list with the same items.
# arr=array.array("i",[8,7,2,12,23,8])
# ls=list(arr)
# print(ls)

#--------------------------------------------------------------
#table of the given number

# def table(n,add=5):
#     for i in range(1,n+1):
#         print(i,"+",add,"=",i+add)
#
# number = 10
# table(number)

#find the Max of three numbers

# def max_three(a,b,c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
#
# print(max_three(4,7,12))

#fibonacci series?

# def fibo(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a,end=" ")
#         tmp=a+b
#         a=b
#         b=tmp
#
# fibo(10)

#function to display group of strings

# def display_strings(strings):
#     for str in strings:
#         print(str)
#
#
# strings = ["Hello, World!", "This is Pascal's Triangle.", "Python programming is fun!"]
# display_strings(strings)


#----------------------------------------------------------------------------------
#DICTIONARY
#To sort (ascending and descending) a dictionary by value

# def sort_dict_using_loop(original_dict):
#     key_search="m"
#     if key_search in original_dict:
#         return "key exist"
#     else:
#         return "doesnot exist"

# sorted_dict = {}
# for key in sorted(original_dict,key=original_dict.get):
#     print(original_dict.get)
#     sorted_dict[key] = original_dict[key]
# return sorted_dict

# ds = {'a': 3, 'b': 1, 'c': 2}
# print(sort_dict_using_loop(ds))

#Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

# n=10
# ds = {x:x*x for x in range(1,n+1)}
# print(ds)

#Merge two Python dictionaries
# ds1 ={"a":1,"b":2,"c":3}
# ds2 ={"f":5,"g":9}
# ds1.update(ds2)
# print(ds1)
# sum =0
# for item in ds1.values():
#     sum +=item
# print(sum)

# def Merge(dict1, dict2):
#     dict1.update(dict2)
#     return dict1
#
#
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
#
# print(Merge(dict1, dict2))

#Map two lists into a dictionary
# keys = ["a","b","c","d"]
# values = [1,6,9,23]
# ds= dict(zip(keys,values))
# print(ds)

#Match key values in two dictionaries.
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'a': 1, 'b': 3, 'c': 3, 'd': 4}
# match ={}
# for i in dict1:
#     if dict1[i]==dict2[i]:
#         match[i]=dict2[i]
# print(match)

#Replace dictionary values with their sum

ds1 = {"a": 1, "b": 7, "c": 5}
ds2 = {"c": 7, "d": 9, "e": 10}

# s=set(ds1.keys()).union(set(ds2.keys()))
# all_keys = set(ds1.keys()).union(ds2.keys())
#
# result={}
# for key in all_keys:
#     value1 = ds1.get(key, 0)
#     value2 = ds2.get(key, 0)
#     result[key] = value1 + value2
#
# print(result)
#
# ds = {"a":8}
# print(ds.get("b",0))

#create a dictionary from two lists without losing duplicate values.
# keys = ['a', 'b', 'a', 'c', 'b']
# values = [1, 2, 3, 4, 5]
#
# print(list(zip(keys,values)))
#
# result = {}
# for k, v in list(zip(keys, values)):
#     if k in result:
#         result[k].append(v)
#     else:
#         result[k] = [v]
# print(result)

#Count number of items in a dictionary value that is a list
# ds = {'a': [1, 3], 'b': [2, 5], 'c': [4]}
# for item in ds:
#     print("for key ",item," = length of value is ",len(ds[item]))

#Check multiple keys exists in a dictionary
# ds = {'a': [1, 3], 'b': [2, 5], 'c': [4]}
#
# for key in ds.keys():
#     if list(ds.keys()).count(key)>1:
#         print("duplicate key exist")
#         break
# else:
#     print("duplicate key doesnot exist")
#
# for item in ds:
#     print(item,ds[item])

#Get the maximum and minimum value in a dictionary.
# ds = {"a":1,"b":7,"c":5}
# max_value = max(ds.values())
# min_val = min(ds.values())
# print(max_value,min_val)
#
# print("max =", max(ds.items(),key=lambda x:x[1]))
# print("min =",min(ds.items(),key=lambda x:x[1]))


#Remove duplicates from Dictionary
#ds = {"a":1,"b":7,"c":5,"d":7,"e":1}

# unique_res={}
# for key,value in ds.items():
#     if value not in unique_res.values():
#         unique_res[key]=value
# print(unique_res)

#Remove spaces from dictionary keys.

# ds = {"v a":1,"b c":7,"c d":5,"d e":7,"e f":1}
# new_ds={}
# for key,value in ds.items():
#     new_ds[key.replace(" ","")]=value
# print(new_ds)

#Create a dictionary from a string.
# input_string = "a.1, b.2, c.3, d.4"
# ds={}
# for item in input_string.split(", "):
#     ds[item.split(".")[0]] = int(item.split(".")[1])
# print(ds)
#Combine values in python list of dictionaries
# data = [
#     {'a': 1, 'b': 2},
#     {'a': 5, 'b': 1, 'c': 15},
#     {'a': 7, 'c': 8}
# ]
# res_dict = {}
#
# for item in data:
#     for key,val in item.items():
#         if key not in res_dict:
#             res_dict[key]=[val]
#         else:
#             res_dict[key].append(val)
# print(res_dict)
# result ={}
# for k,v in res_dict.items():
#     sum=0
#     for item in v:
#         sum +=item
#         result[k]=sum
# print(result)

#Count the values associated with key in a dictionary
# ds = {
#     1: 'a',
#     2: 'b',
#     3: 'a',
#     4: 'o',
#     5: 'b',
#     6: 'a'
# }
# res = {}
# val = list(ds.values())
# for ele in val:
#     if ele not in res:
#         res[ele] = val.count(ele)
# print(res)

#Sort a list alphabetically in a dictionary

# items = {
#     "fruits": ["banana", "apple", "cherry", "date"],
#     "vegetables": ["carrot", "broccoli", "asparagus", "celery"]
# }
# for i in items:
#     print(sorted(items[i]))

#Convert a list into a nested dictionary of keys.
# def nested_dict(ls_input):
#     res = {}
#     if not ls_input:
#         return {}
#     else:
#         return {ls_input[0]: nested_dict(ls_input[1:])}
#
# ls = ["a", "b", "c", "d"]
# print(nested_dict(ls))
#Sort Counter by value
ite = {"apple": 4, "banana": 2, "cherry": 5, "date": 3}

# print(sorted(ite.items(), key = lambda x:x[1],reverse=True))
# print(sorted(ite,key = ite.get))
#Combine two dictionary adding values for common keys.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

combined_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

# print(combined_dict)

#Print all unique values in a dictionary.

# dict1 = {'a': 1, 'b': 2, 'c': 3,'d':2}
# print(set(dict1.values()))

#Create and display all combinations of letters, selecting each letter from a different key in a dictionary
# my_dict = {
#     '1': ['a', 'b'],
#     '2': ['c', 'd'],
#     '3': ['e', 'f']
# }
# list1 = my_dict['1']
# list2 = my_dict['2']
# list3 = my_dict['3']
#
# for i in list1:
#     for j in list2:
#         for k in list3:
#             print(i+j+k)

#
#Find the highest 3 values in a dictionary.

# item = {"apple": 4, "banana": 2, "cherry": 5, "date": 3}
# res = sorted(item.items(),key = lambda x:x[1],reverse=True)
# print(dict(res[:3]))

# to match the item in two dictionaries.
ds1 = {"a": 1, "c": 3, "d": 5}
# ds2 = {"c":1,"d":3,"e":"5"}
ds2 = {"c": 3, "d": 5, "e": "5"}

# print(set(ds1).intersection(set(ds2)))
#
# print(ds1.items() & ds2.items())
# comm = ds1.items() & ds2.items()
# for i in comm:
#     print(i[0],end=" ")

# function to check whether a string is a pangram or not

# def pangram_check():
#     str = "The quick brown fox jumps over the lazy dog"
#     #o(n^2)
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#
#     for char in alphabet:
#         if char in str.lower():
#             return "pangram"
#         return "not pangram"
#
#
#
# print(pangram_check())

# print given Pascal's triangle

# from math import factorial
# n = 5
# for i in range(n):
#     for j in range(n-i+1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
#     # for j in range(i):
#     #     print("f",end="")
#     print(" ")

# takes a list and returns a new list with unique elements of the first list.
# ls = [2,3,4,2,5,6,7,5]
# ds = {}
# for i in ls:
#     ds[i] = ls.count(i)
# print(ds.keys())

# str = "accepts a string and Calculate the Number of upPer case letters and lower case letters"
#
# count_lower = 0
# count_upper = 0
# for i in str:
#     if i.islower() == True:
#         count_lower +=1
#     if i.isupper() == True:
#         count_upper +=1
# print(count_upper,count_lower)
# check whether a number is in a given range
# def BinarySearch():
#     ls = [x for x in range(10)]
#     target =7
#     ls.sort() #if not sorted list
#     low = 0
#     high = len(ls)
#     while low<=high:
#         mid = (low+high)//2
#         if ls[mid] == target:
#             return mid
#         elif ls[mid] < target:
#             low = mid+1
#         elif ls[mid]> target:
#             high = mid-1
#     return -1
#
#
# print(BinarySearch())

#fibonacci

# a = 0
# b = 1
# num = 10
# count = 1
# while count <= num:
#
#     print(a,end=" ")
#     tmp = a + b
#     a = b
#     b = tmp
#     count += 1
#prime number series
# n=50
#
# for ite in range(n+1):
#     for i in range(2,ite):
#         if (ite%i)==0:
#             break
#     else:
#         print(ite,end=" ")

#tuple , set , array
