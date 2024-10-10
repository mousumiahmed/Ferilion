#Decision making task1
#1.Take values of length and breadth of a rectangle from user and check if it is square or not.
# def checkSquare(a,b):

#     if a==b:
#         return "it's a square"
#     else:
#         return "it's not a square"
# leng = int(input("enter the length of rectange:"))
# breath = int(input("enter the breath of rectangle:"))
    
# print(checkSquare(leng,breath))
# #2 Write a program to check whether a entered character is lowercase (a to z) or uppercase (A to Z).


# def checkUpperCaseLoerCase(inp):
#     if inp>='a' and inp<='z':
#         return "Lower case"
#     elif inp>='A' and inp<='Z':
#         return "Upper case"
# inp = input("enter the character:")
# print(checkUpperCaseLoerCase(inp))

#3 Write a program to get a number from the user and print whether it is positive or negative.

# def checkPositiveNegative(num):
#     if num>0:
#         return "Positive"
#     elif num<0:
#         return "Negative"
#     else:
#         return "it's just a 0"
# num = int(input("enter the number :"))
# print(checkPositiveNegative(num))

#4 Write a program that reads a floating-point number and prints "zero" if the number is zero. Otherwise, print "positive" or "negative". Add "small" if the absolute value of the number is less than 1, or "large" if it exceeds 1,000,000.

# def checkFloatingPoint(num):
#     if num>0:
#         #return "positive"
#         if abs(num)>1000000:
#             return "positive and large"
#         if abs(num)<1:
#             return "positive and small"
#         else:
#             return "positive only"
#     elif num<0:
#         #return "negative"
#         if abs(num)>1000000:
#             return "negative and large"
#         if abs(num)<1:
#             return "negative and small"
#         else:
#             return "negative only"
#     else:
#         return "zero"
    
# number=float(input("Enter the floating point number :"))
# print(checkFloatingPoint(number))

#5 Write a program that takes a number from the user and generates an integer between 1 and 7. It displays the weekday name

# def printweekdays(day):
#     if day>0 and day<8:
#         if day==1:
#             return "Monday"
#         elif day==2:
#             return "Tuesday"
#         elif day==3:
#             return "wednesday"
#         elif day==4:
#             return "Thrusday"
#         elif day==5:
#             return "Friday"
#         elif day==6:
#             return "Saturday"
#         elif day==7:
#             return "Sunday"
#     else:
#         return "You must enter number in between 1 to 7"
    
# num = int(input("Enter the number in between 1 to 7 : "))
# print(printweekdays(num))

#6 Write a program that requires the user to enter a single character from the alphabet. Print Vowel or Consonant, depending on user input. If the user input is not a letter (between a and z or A and Z), or is a string of length > 1, print an error message.

# def checkVowelorConsonent(ch):
#     if len(ch)==1:
#         if ch=="a" or ch=="A" or ch=="e" or ch=="E" or ch=="i" or ch=="I" or ch=="o" or ch=="O" or ch=="u" or ch=="U":
#             return "vowel"
#         else:
#             return "consonent"
#     else:
#         return "entered string length must be 1"
#
# str=input("enter the character :")
# print(checkVowelorConsonent(str))

#7 Write a program to display the cube of the given number up to an integer

# num = int(input("enter the number :"))
# print(num*num*num)

#8 Write a program that displays the sum of n odd natural numbers

# num = int(input("enter the value of n:"))
# odd_sum=0
# for x in range(num+1):
#     if x%2 !=0:
#         odd_sum+=x
# print(odd_sum)

#9 Write a program that accepts three numbers from the user and prints "increasing" if the numbers are in increasing order, "decreasing" if the numbers are in decreasing order, and "Neither increasing or decreasing order" otherwise.

# numbers=eval(input("Enter three number :"))
# if len(numbers)==3:
#     if numbers==tuple(sorted(numbers)):
#         print("increasing")
#     elif numbers==tuple(sorted(numbers,reverse=True)):
#         print("decreasing")
#     else:
#         print("Neither increasing or decreasing order")
# else:
#     print("Enter three number")

#10 Write a program that prompts the user to enter three names. Your program should display the names in descending order

# str=eval(input("Enter three Names :"))
#
# if len(str)==3:
#     print(sorted(str,reverse=True))
# else:
#     print("you have to enter three name !!!")

# 11 Write a program to calculate the monthly telephone bills as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.

# Num_call = int(input("enter the number of call :"))
# if Num_call<=100:
#     print("bill = 200")
# elif Num_call>=100 and Num_call<=150:
#     print("bill =",200+(Num_call-100)*0.6)
# elif Num_call>150 and Num_call<=200:
#     print("Bill =",200+50*.6+(Num_call-150)*.5)
# elif Num_call>200:
#     print("Bill =", 200+50*.6+50*.5+(Num_call-200)*.4)

#12 Write a program to determine whether the year is a leap year or not.

# year = int(input("Enter the Year :"))
# if year%4==0:
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")
# #13 Write a program that asks the user to enter 3 numbers in three variables and then displays the largest number.
#
# numbers = eval(input("Enter three numbers in three variables :"))
# print(numbers)

#14 Write a program that asks the user to enter a number and displays whether entered number is an odd number or even number
# num = int(input("enter the number :"))
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

# 15 A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

# Num_Class_held = int(input("enter number of class held :"))
# Num_Class_attend = int(input("enter number of class attained :"))
# percentage_class_attended = (Num_Class_attend/Num_Class_held)*100
# print(f"percentage {percentage_class_attended}%")
# if percentage_class_attended>=75:
#     print("student will allow to attend the exam")
# else:
#     print ("student will not allow to attend the exam")

# 16 A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade

# marks = int(input(("Pls enter the marks :")))
# if marks<=25:
#     print("F")
# elif marks>25 and marks<=45:
#     print("E")
# elif marks>45 and marks<=50:
#     print("D")
# elif marks>50 and marks<=60:
#     print("C")
# elif marks>60 and marks<=80:
#     print("B")
# elif marks>80:
#     print("A")
#17 A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.

# year = int(input("Pls enter Year of Experience : "))
#
# if year>5:
#     salary = int(input("pls enter salary :"))
#     print("Net bonus :",salary*(5/100))
# else:
#     print("Employee is not eligible for bonus")
#18 Create a program to check if a number is a perfect number

# num = int(input("enter the number :"))
# sum = 0
# for i in range(1, num):
#     if (num % i == 0):
#         sum = sum + i
#         if (sum == num):
#             print(num,"number is perfect number")
#             break
# else:
#     print(num,"number is not perfect number")

#19 Implement a program to reverse a string without using built-in functions.

# str = input("Enter the string :")
# rev=""
# for x in str:
#     rev=x+rev
# print(rev)
#20 Develop a program to perform matrix multiplication

# Row1 = int(input("Enter the number of row in first matrix :"))
# Col1 = int(input("Enter the number of column in first matrix :"))
# matrix1 = []
# #matrix1 = [[0] * Col1] * Row1
# for i in range(Row1):
#     rowList1 = []
#     for j in range(Col1):
#         rowList1.append(int(input("Enter element row wise for first matrix :")))
#     matrix1.append(rowList1)
# #print(matrix1)

# Row2 = int(input("Enter the number of row in second matrix :"))
# Col2 = int(input("Enter the number of column in second matrix :"))
# matrix2=[]
# for _ in range(Row1):
#     rowList2=[]
#     for _ in range(Col2):
#         rowList2.append(int(input("Enter element row wise for second matrix :")))
#     matrix2.append(rowList2)
#
# #using list comprehension

# if Col1==Row2:
#     # using list comprehension
#     result = [[0 for i in range(Col1)] for j in range(Row2)]
#     for i in range(Row1):
#         for j in range(Col2):
#             for k in range(Row2):
#                 result[i][j]+=matrix1[i][k]*matrix2[k][j]
#     print(result)
#
# else:
#     print("No of column of first Matrix must be equal to no of column of second matrix ")

#21 Implement a Python program to check if a given string is a valid IP address

# ip_address = input("Enter the Ip Address :")
# ip_parts = ip_address.split(".")
# count=0
# if len(ip_parts) == 4:
#     for x in ip_parts:
#         if 0 <= int(x) <= 255:
#             count+=1
# else:
#     print("Invalid Ip Address")
# if count ==4:
#     print("Valid Ip Address")
# else:
#     print("Invalid Ip Address")

#22 Create a program to calculate the average of N numbers.

# n = int(input("Enter the value of N :"))
# sum = 0
# avg = 0
# for x in range(1,n+1):
#     sum +=x
# avg = float(sum /n)
# print(avg)
#23 Create a program to check if a number is a power of two.

#2**n

# num = int(input("Enter the Number :"))
# for x in range(num):
#     if num==2**x:
#         print(f"{num} is power of two")
#         break
# else:
#     print(f"{num} is not power of two")

#24 Create a program to calculate the compound interest.
# CI = A – P
# A=P(1+R/N)**t
# A=P(1+R/100)**t compounded annually
# Principle_amt =float(input("enter the principle amount :"))
# R=float(input("enter the annual interest rate :"))
# T=float(input("enter the time : "))
# compound_interest= Principle_amt*(1+R/100)**T
# print("compound interest :",compound_interest-Principle_amt)

#25 Implement a program to find the reverse of a given number

# num = int(input("Enter the number :"))
# rev = 0
#
# while num != 0:
#     reminder = num % 10
#     rev = rev*10+reminder
#     num //= 10
# print(str(rev))

#26 Write a Python program to check if a given number, is a strong number

# num = int(input("enter a number :"))
# sum_factorial=0
# tmp_num =num
#
# while tmp_num>0:
#     fact=1
#     rem = tmp_num % 10
#     #print(rem)
#     for i in range(1,rem+1):
#         fact = fact * i
#     sum_factorial =sum_factorial + fact
#     tmp_num =tmp_num //10
#
# if num==sum_factorial:
#     print(f"{num} is a strong number")
# else:
#     print(f"{num} is not a strong number")

#27 Implement a program to calculate simple interest
#S.I. = (P × R × T)/100

# P=float(input("Enter the Principle Amount :"))
# R=float(input("Enter Rate of interest per annum :"))
# T=float(input("enter time in years"))
# S_I = (P*R*T)/100
# print("S.I is = ",S_I)





















