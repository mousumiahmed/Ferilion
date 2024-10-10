#1.	Print numbers from 1 to 10 using a for loop

# for x in range(1,11):
#     print(x)

#2.	Calculate the sum of numbers from 1 to 10 using a for loop

# sum=0
# for x in range(1,11):
#     sum +=x
# print(sum)

#3.	Print the elements of a list using a for loop

# ls =[2,3,4,"python"]
# for x in ls:
#     print(x)

#4.	Calculate the product of elements in a list using a for loop

# product=1
# ls=[2,3,4,"python"]
# for x in ls:
#     if type(x)==int:
#         product *=x
# print(product)

#5.	Print characters of a string using a for loop

# str= "string_python"
# for x in range(len(str)):
#     print(str[x])

#6.	Find the largest number in a list using a for loop

# ls = [4,6,23,9,99,1,0,100,56]
# largest_num=ls[0]
# for x in range(1,len(ls)):
#     if ls[x]>largest_num:
#         largest_num=ls[x]
#     else:
#         largest_num=largest_num
# print(largest_num)

#7.	Find the average of numbers in a list using a for loop

# ls = [4,6,23,9,99,1,0,100,56]
# sum=0
# avg=0
# for x in ls:
#     if type(x)==int:
#         sum +=x
# avg = sum/len(ls)
# print(avg)

#8.	Calculate factorial of a number using a while loop

# num=int(input("enter the number :"))
# fact=1
# # while num==0 or 1:
# #     fact=1
# while num>1:
#     fact = fact*num
#     num=num-1
# print(fact)

#9.	Find the first occurrence of a number in a list using a while loop
# ls =[1,2,3,4,5,2,4,3,1]
# for x in ls:
#     if ls.count(x)>1:
#         print(x)
#         break

#10.	Find the common elements in two lists using a for loop
# ls1=[2,4,5,7]
# ls2=[5,7,3,34]
# for x in ls1:
#     for y in ls2:
#         if x==y:
#             print(x)

#11.	Write a program to display the sum of n terms of even natural numbers

# num = int(input("enter the value of nth term :"))
# sum=0
#
# for x in range(1,num+1):
#     sum += x
# print(sum)

#12. Write a program to find the Armstrong number for a given range of number

# num = int(input("enter the number :"))
# sum = 0
# rem = 0
# digit = len(str(num))
# tmp=num
# while tmp>0:
#     rem = tmp % 10
#     sum =sum +rem**digit
#     tmp //= 10
#
# # print(sum,num)
# if num == sum:
#     print(f"{num } is armstrong number")
# else:
#     print(f"{num} is not armstrong number")

#13.	Write a program in to convert a decimal number into binary without using a list

# def binary(num):
#     if num > 1:
#         binary(num//2)
#     print(num % 2,end="")
#
# binary(10)
# if __name__ =="__main__":
#     print("code")
# # print(__name__)






